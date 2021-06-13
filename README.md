# THE 2048 GAME IN PYTHON
##The platform used is windows 

## Sample gif displaying the gameplay:
user enters initial game conditions:


![gameplay](https://user-images.githubusercontent.com/64685403/82234061-7f45c880-994e-11ea-8b8d-7d96fd252ad3.PNG)

gif:


![1stgif](https://user-images.githubusercontent.com/64685403/82232527-62a89100-994c-11ea-8165-5d47f5509d56.gif)
## Libraries used:
- numpy: for matrices
- os: to clear screen
- random:
  - to select random location in the matrix
  - to allocate random number (2 or 4) after every move
- time:to clear screen after 1 second
- msvcrt:to take input without pressing enter

## GAMEPLAY:
Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4.

Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. 

If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.

If a move causes three consecutive tiles of the same value to slide together, only the two tiles farthest along the direction of motion will combine. 

If all four spaces in a row or column are filled with tiles of the same value, a move parallel to that row/column will combine the first
two and last two.

The game is won when a tile with a value of 2048(winning number) appears on the board, hence the name of the game.

When the player has no legal moves (there are no empty spaces and no adjacent tiles with the same value), the game ends.


## Actions:(using wasd keys)
- w:slide up

- a:slide left

- s:slide down

- d:slide right
