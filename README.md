# AlgoNum Guessing Game

## Description
This simple smart contract was created for a Decentralized App - The AlgoNum Guessing Game.
It has global and local states to store , check , and update data. The player will be guessing a random number with the given limited number of  chances.
This smart contract demonstrates what I have learned on PyTeal course especially on counter-app and Subroutines.



## Global and Local State

### Global State :

#### Global_players_count #uint64
<li>This will count the number of total players</li>

### Local State :

#### local_play_count #uint64
 <li>This will count on how many times a user plays .</li>

#### local_chances #uint64
<li> This stores the number of chances (The default value is 5) .</li>

#### local_points #uint64

<li> This is where the points of a user are stored.</li>

#### isGuessOver #uint64
<li> if the chances runs out , then isGuessOver will be set to 1 if (isGuessOver==1) means you
failed to guess the random secret number and then the game will end.</li>


#### regNumGame #uint64
<ul>
<li>
    when the player enters the game for the first time, the player will be automatically
    registered. regNumGame will be set to 1 and it cannot be changed because registration
    happens only once.
</li>
<li>
    This helps us to count the total number of players. we can get the specific number of players
    who join (or register) and play the game.
</li>
<li>
    Although there are no credentials needed like name, age to input just to make the player
    registered in the game but only through clicking the "PLAY" Button (see my front-end).
</li>
<li>
    Without regNumGame, the global_players_count will always be incremented or increasing
    like local_play_count when a player(for example : Ben) enters the game for many times.
</li>


</ul>

## Subroutines in Smart Contracts and their uses
### join_and_play :
<p>
    In this Subroutine, it will count the number of players(global_players_count), how many times does a
    player play (play_count) and register the user that will enter the Number Guessing Game for the first
    time (regNumGame).
</p>

<p>
Next time the player enters the game , the Subroutine will evaluate whether if the player had
registered in the past or not, if regNumgame is equal to 1 then only play_count will be incremented
to 1 .
</p>
<p>
If regNumgame is 0 ,it will proceed to the next condition where the global_players_count will be
increased to one and also the play_count and set the regNumgame to 1 , Meaning the player has
successfully joined the game and they can now play.
</p>

ADDITIONAL : The chances default value will be set to 5 as the player enters the game

### guess :
This Subroutine has local_chances (in which the default value is 5) and isGuessOver (default is 0) .
If the local_chances is equal to 0, then the isGuessOver will be set to 1 (Meaning the game is over).
If not, then the player can still have the opportunity to guess the secret random number until the
chances runs out

### add_points :
The time that the user guessed the secret number correctly, the points (local_points) will be
incremented to 1

### play_again :
This Subroutine will set the number of chances(local_chances) back to 5 and isGuessOver will be
set to 0 (Meaning you can now play the game again).




### Application ID

<p>252279791</p>
https://testnet.algoexplorer.io/application/252279791 

### Front-end
 This is the repository of the front - end :<br>
 https://github.com/ramdio12/number_guessing_game.git
 
### Demo Website
Here is the [link](https://algo-num-guessing-game.vercel.app/) to the website.

### Smart Contact
Here's the  to the dApp's smart contract.
[link](https://github.com/ramdio12/Algonum_Smart_Contract.git)

### Video Demonstration
To see the video demonstration:<br>
[link](https://drive.google.com/drive/folders/1YIQh065mkMfQ3LQDkXXJmKZg5eR7Nczw?usp=sharing)
