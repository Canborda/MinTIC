# <b>Minigame</b>

Write a code for a simple game where the user must reach a goal using different keys to move a token around a squared board.

> <b>Example:</b><br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . X . . . . . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . O . .```<br>
> ```. . . . . . . . . .```<br>
> ```. . . . . . . . . .```<br>

## <b>Requeriments:</b>

1. Use __W, A, S, D__ keys as options to move the token Up, Left, Down and Right respectively. The menu also must have an _Exit_ option.

2. The size of the board must be an user input.

3. The initial token and goal positions must be random-generated.

4. If the token crashes a wall must appear on the opposite side.

5. When the token reaches the goal should print a message ```CONGRATULATIONS! You reached the goal```, and should display a new menu with two options: (1) Play again and (2) Exit program.

## <b>Improvements:</b>

<b>Minigame 2.0: </b>Once finished the game, now develop another program where the token reaches the goal by itself following the closest path. Use time delays to see the steps.

### <b>Required concepts (_Hints_):</b>

> - <span style="color:lightblue">While:</span> for the program remain running until the user selects the _Exit_ option.
> - <span style="color:lightblue">Nested for:</span> To print a 2 dimension matrix must use a for inside another for (see example below).
> - <span style="color:lightblue">Print:</span> Use the ```end``` argument in the ```print``` function to print in the same line (see the example below).
> - <span style="color:lightblue">Libraries:</span> Use the ```random``` library to generate random integers. Use the ```time``` library to add time delays for the Minigame 2.0.
> 
> Example:
> <pre>for i in num_rows:
>     for j in num_cols:
>         print(matrix[i][j], end=' ')</pre>

---