# <b>Memory Game</b>

Write a program that shows a number for a small period of time and then ask the user for the exact number. The game starts with a one-digit number, and with each round the number must increase one digit. The game ends when the user fails in write the number. Each digit written correctly gives 1 point to the score.

## <b>Requeriments:</b>

1. The game starts when the user press 'Enter'.
2. The number is random-generated.
3. The time the number is displayed starts at 1 second, and increases 0.2 seconds each round.
4. When the number is hidden, should be replaced with the ```*``` character. <i>Example:</i> the program shows ```Memorize: 156``` and after the time delay <b>THE SAME LINE</b> shows ```Memorize: ***```.
5. After the user writes the answer, the program must inform if the number is correct or if the user has lost.
6. If the number is incorrect, must calculate how many digits the user got right and add them to the score.
7. When the game is over must print a message with the final score.


## <b>Example:</b>

<pre>
WELCOME TO MEMORIZE!
Press enter to start...

LEVEL 1
        Memorize:   *
        Your turn:  3
        CORRECT...

LEVEL 2
        Memorize:   **
        Your turn:  25
        CORRECT...

LEVEL 3
        Memorize:   ***
        Your turn:  985
        CORRECT...

LEVEL 4
        Memorize:   ****
        Your turn:  3234
        YOU LOST... 3144 was the correct number.

 Level Reached = 4
   Final Score = 8
</pre>

### <b>Required concepts (_Hints_):</b>

> - <span style="color:lightblue">While:</span> for the program remain running until the user loses.
> - <span style="color:lightblue">For:</span> To generate $n$ random digits and for character-by-character string comparations.
> - <span style="color:lightblue">Return carriage:</span> When using the ```print``` function, the ```end='\r'``` argument allows to overwrite the next ```print``` on the same line.
> - <span style="color:lightblue">Libraries:</span> Use the ```random``` library to generate random integers. Use the ```time``` library to add time delays to show the number for a period of time.