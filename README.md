# Design TicTacToe (Low Level Design)

## **OVERVIEW**

TicTacToe is a X/O game that two people play on 3x3 grid and three consecutive Xs or Os in a straight line determines the winner of the game. 

This seems like a software system thats takes input. No need to persist data.

## Requirements and Clarifications

_**Should I restrict the size of grid to 3x3?**_

_No, Lets do it nXn_

_**Should this game has only two players?**_

_n-1_

_**We want to support bots with varying difficulty level**_

_At max keep one bot per game._.

_**Every player has a different symbol. Probably a char/string. Validate this.**_

_**Are we supporting tounaments or keeping a leaderboard?**_

_No_

_**Can a player do UNDO?**_

_Yes, its a global undo that any player can do._

_**Do we want to keep a time limit on the move?**_

_No_

_**When/how will the game start?**_

_Suppose, we have five players A,B,C,D,E. Then we randombly order these players say D,B,A,C,E and they will follow this order for their turn._

_**When/how will the game end?**_

_We will end the game when someone has won or there is a draw. And not when all but one has won._

_**What decides a victory in the game?**_

_We should allow to add new ways in which can someone can win. Like all corners of the grid have same symbol. And when we start the game, we configure ways in which a player can win._

_**What to do if someone exits?**_

_End the game, or remove their symbols, replace them by bot. Dont support this._

_**Should we allow replay?**_

_Yes_

![Image](./679478.jpg "RED")


## Classes

### Board
- Size
- Grid (2D list of Cell)

### Cell
- row
- col
- CellState
- Player

### CellState
- EMPTY/FILLED/BLOCKED

### Player
- Symbol
- Name
- PlayerType

### Symbol
- char

### PlayerType
- HUMAN/BOT/GUEST
 
### Bot (Player)
- DifficultyLevel

### DifficultyLevel
- EASY/MEDIUM/HARD

### Move
- Player
- Cell

### GAME
- Board
- Moves (list of Move)
- Players (list of Player)
- currentPlayerindex (We already have a list of players)
- WinningStrategies (list of WinningStrategy)
- GameStatus 
- Winner

### GameStatus
- INPROGRESS/ENDED/DRAW

### WinningStrategy

- ### RowWinningStrategy (WinningStrategy)
- ### ColumnWinningStrategy (WinningStrategy)
- ### DiagonalWinningStrategy (WinningStrategy)

### BotPlayingStrategy

- ### EASYBotPlayingStrategy (BotPlayingStrategy)
- ### MEDIUMBotPlayingStrategy (BotPlayingStrategy)
- ### HARDBotPlayingStrategy (BotPlayingStrategy)

### GAMEBuilder {for Validation}

## Notes

1. When UNDO happens, clear cell, remove move from list of moves and 
move turn to the previous player. But UNDO moves in games like Chess is complicated.

2. 
