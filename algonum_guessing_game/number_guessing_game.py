from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program

UINT64_MAX = 0xFFFFFFFFFFFFFFFF


def approval():

    global_players_count = Bytes("players_count")  # uint64
    local_play_count = Bytes("play_count")  # uint64
    local_chances = Bytes("chances")  # uint64
    local_points = Bytes("points")  # uint64

    isGuessOver = Bytes("isGuessOver") # uint64
    regNumGame = Bytes("register") # uint64

    op_add_points = Bytes("add_points")
    op_play_again = Bytes("play_again")
    op_guess = Bytes("guess")
    op_join_play = Bytes("join_and_play")

    scratch_players_count = ScratchVar(TealType.uint64)
    scratch_chances = ScratchVar(TealType.uint64)
    scratch_points = ScratchVar(TealType.uint64)
    scratch_play_count = ScratchVar(TealType.uint64)

    @Subroutine(TealType.none)
    def join_and_play():
        return Seq(
            
            scratch_players_count.store(App.globalGet(global_players_count)),
            scratch_play_count.store(App.localGet(Int(0), local_play_count)),

            If(App.localGet(Int(0), regNumGame) == Int(1))
            .Then(
                App.localPut(Int(0), local_play_count,scratch_play_count.load()+Int(1)),
            ).Else(
                Seq(
                    App.globalPut(global_players_count,scratch_players_count.load()+Int(1)),
                    App.localPut(Int(0), local_play_count,scratch_play_count.load()+Int(1)),
                    App.localPut(Int(0), regNumGame, Int(1)),
                ),
            ),
            App.localPut(Int(0), local_chances, Int(5)),
            Approve(),
        )

    @Subroutine(TealType.none)
    def guess():
        return Seq(
            program.check_self(
                group_size=Int(1),
                group_index=Int(0),
            ),
            program.check_rekey_zero(1),

            scratch_chances.store(App.localGet(Int(0), local_chances)),

            If(Eq(scratch_chances.load(), Int(0)))
            .Then(
                Seq(
                    App.localPut(Int(0), isGuessOver, Int(1)),
                    App.localPut(Int(0), local_chances, Int(0)),
                )
            ).Else(
                App.localPut(Int(0), local_chances,scratch_chances.load()-Int(1)),
            ),
            Approve()
        )

    @Subroutine(TealType.none)
    def add_points():
        return Seq(
            program.check_self(
                group_size=Int(1),
                group_index=Int(0),
            ),
            scratch_points.store(App.localGet(Int(0), local_points)),
            App.localPut(Int(0), local_points,scratch_points.load()+Int(1)),
            Approve()
        )

    @Subroutine(TealType.none)
    def play_again():
        return Seq(
            # basic sanity checks
            program.check_self(
                group_size=Int(1),
                group_index=Int(0),
            ),
            App.localPut(Int(0), isGuessOver, Int(0)),
            App.localPut(Int(0), local_chances, Int(5)),
            Approve(),
        )

    return program.event(
        init=Seq(
            [
                App.globalPut(global_players_count, Int(0)),
                Approve(),
            ]
        ),
        opt_in=Seq(
            App.localPut(Int(0), local_points, Int(0)),
            App.localPut(Int(0), isGuessOver, Int(0)),
            App.localPut(Int(0), local_chances, Int(5)),
            App.localPut(Int(0), local_play_count, Int(0)),
            Approve(),
        ),
        no_op=Seq(
            Cond(
                [Txn.application_args[0] == op_join_play, join_and_play()],
                [Txn.application_args[0] == op_guess, guess()],
                [Txn.application_args[0] == op_add_points, add_points()],
                [Txn.application_args[0] == op_play_again, play_again()],

            ),
            Reject(),
        ),
    )


def clear():
    return Approve()
