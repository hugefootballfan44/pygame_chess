Before Running Code:

Navigate to this page to download the appropriate version of Stockfish for your device: https://stockfishchess.org/download/
Then move the .exe file to the folder containing the Python code and rename it to 'stockfish' (case-sensitive).
This will allow for the chess engine Stockfish to be loaded into the program.

Also necessary will be installing the following Python libraries to allow for their import:
1. pygame
2. chess
3. random
4. pygame_widgets
5. stockfish

While Running Code:

Note that with every textbox, inputs are case-sensitive. For example, if 'Yes' is an accepted answer, 'yes' will not be.
Moreover, there is no need to press ENTER with these textboxes. Merely typing in a response is sufficient.

When beginning the program, the pygame screen will first display a series of prompts within textboxes. The user's responses to these prompts help construct the game.

The first textbox will ask which board theme the user would like to play with. The possible answers are:
1. 'Wood', which colors the board squares brown and tan
2. 'Ice', which colors the board squares light blue and white
3. 'Forest', which colors the board squares dark green and light green

The second textbox will ask the user which color pieces they will be playing with. The possible answers are:
1. 'White', giving the user the white pieces and therefore the first move of the game
2. 'Black', giving the user the black pieces and therefore giving the computer the first move of the game

The third textbox will ask the user if they are to play against the strong open-source chess engine Stockfish. The possible answers are:
1. 'Yes', which will enable Stockfish as the computer opponent if possible.
2. 'No', which will set the computer opponent to an alternative that makes random legal moves

If Stockfish is inaccessible despite the user entering 'Yes', a subsequent textbox will appear informing the user of that fact.
The opponent will be set to the aforementioned alternative as though the user responded 'No', and the user would need to enter anything into the textbox to proceed.

If Stockfish is accessible and the user entered 'Yes', the next textbox will ask which skill level Stockfish should be set to. The options are any number from 0 to 20, with single digits listed with a leading 0. For instance, if the user desires to set Stockfish's skill level to 7, they would enter '07' into the textbox.

From here, the board will appear and the game will begin. Each time it is the user's turn to make a move, a textbox will appear for the user to enter their move.
All moves must be made in algebraic notation. For instance, if the user wishes to move their knight to f3 on their first move, they should enter 'Nf3'.
For more information on algebraic notation, see the article here: https://www.chess.com/terms/chess-notation

One major exception to this arises in certain situations when attempting to castle. Because the textbox registers legal moves automatically without requiring any submission action, it becomes impossible to make the move O-O-O when O-O is also legal. For this reason, when O-O is entered when O-O-O is also a legal move, a follow-up prompt will appear in the textbox asking the user which type of castle they would like to execute. The options are:
1. 'Long', when seeking to make the move O-O-O
2. 'Short', when seeking to make the move O-O

Two other special options can be entered into the textbox when asked to make a move. They are:
1. 'Resign', which ends the game as a loss for the user. This is to be used when the user no longer wishes to continue with the game, presumably because they are losing.
2. 'Draw', which ends the game as a draw if a draw is able to be claimed by either threefold repetition or the 50-move rule.
More information can be found here on the drawing rules: https://www.chess.com/terms/draw-chess

Note that if there is fivefold repetition, the 75-move rule is reached, there is stalemate, or there is insufficient material, the game will be ended as a draw without any input from the player. Moreover, checkmate will automatically end the game as well.

When the game concludes, a textbox will appear filled with a message describing the result of the game.
The user must enter anything into the textbox to exit the game. 

