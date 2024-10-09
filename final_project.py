# Hayden C. Epinette

import pygame
import chess
import random
import pygame_widgets
from pygame_widgets.textbox import TextBox
from stockfish import Stockfish

# Each of the 12 piece image files can be found here:
# https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent
# These files are licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license
# This license can be found here: https://creativecommons.org/licenses/by-sa/3.0/deed.en.

# Stockfish and its source code is available for download here: https://stockfishchess.org/download/
# The license for Stockfish is included in this folder as Copying.txt

# Load each of the piece images and resize them appropriately

rook_white = pygame.image.load("rook_white.png")
rook_white = pygame.transform.scale(rook_white, (100, 100))

knight_white = pygame.image.load("knight_white.png")
knight_white = pygame.transform.scale(knight_white, (100, 100))

bishop_white = pygame.image.load("bishop_white.png")
bishop_white = pygame.transform.scale(bishop_white, (100, 100))

queen_white = pygame.image.load("queen_white.png")
queen_white = pygame.transform.scale(queen_white, (100, 100))

king_white = pygame.image.load("king_white.png")
king_white = pygame.transform.scale(king_white, (100, 100))

pawn_white = pygame.image.load("pawn_white.png")
pawn_white = pygame.transform.scale(pawn_white, (100, 100))

rook_black = pygame.image.load("rook_black.png")
rook_black = pygame.transform.scale(rook_black, (100, 100))

knight_black = pygame.image.load("knight_black.png")
knight_black = pygame.transform.scale(knight_black, (100, 100))

bishop_black = pygame.image.load("bishop_black.png")
bishop_black = pygame.transform.scale(bishop_black, (100, 100))

queen_black = pygame.image.load("queen_black.png")
queen_black = pygame.transform.scale(queen_black, (100, 100))

king_black = pygame.image.load("king_black.png")
king_black = pygame.transform.scale(king_black, (100, 100))

pawn_black = pygame.image.load("pawn_black.png")
pawn_black = pygame.transform.scale(pawn_black, (100, 100))

def draw_board(window, board, color, dark, light):
    '''
    This function draws the chess board and sets the pieces.
    :param window: The pygame window to draw the board in
    :param board: The internal chess board containing the current position
    :param color: The color of pieces the user is playing with
    :param dark: The color of the dark squares
    :param light: The color of the light squares
    '''

    # Wipe the screen clean by coloring it black
    window.fill(pygame.Color("black"))

    # Loop through all 64 square locations
    for i in range(1,65):

        # If the square ought to be a dark square of the chess board...
        if i % 2 + ((i-1) // 8) % 2 == 1:
            # Fill the appropriate square location with the dark color
            pygame.draw.rect(window, dark, [100*(((i-1)%8)+1), 800-100*((i-1)//8), 100, 100], 100)
        else:
            # Otherwise do the same but with the light color
            pygame.draw.rect(window, light, [100*(((i-1)%8)+1), 800-100*((i-1)//8), 100, 100], 100)

        # If the player has the white pieces,
        # check each square in order to place piece images on the board as necessary
        # If the player has the black pieces,
        # check each square in reverse order, effectively rotating the board 180 degrees
        # This rotation is necessary because the internal board is oriented from white's perspective
        if color == 'White':
            try:
                if board.piece_at(i-1).symbol() == 'R':
                    window.blit(rook_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'N':
                    window.blit(knight_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'B':
                    window.blit(bishop_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'Q':
                    window.blit(queen_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'K':
                    window.blit(king_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'P':
                    window.blit(pawn_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'r':
                    window.blit(rook_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'n':
                    window.blit(knight_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'b':
                    window.blit(bishop_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'q':
                    window.blit(queen_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'k':
                    window.blit(king_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(i-1).symbol() == 'p':
                    window.blit(pawn_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
            except AttributeError:
                pass
        else:
            try:
                if board.piece_at(64-i).symbol() == 'R':
                    window.blit(rook_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'N':
                    window.blit(knight_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'B':
                    window.blit(bishop_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'Q':
                    window.blit(queen_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'K':
                    window.blit(king_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'P':
                    window.blit(pawn_white, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'r':
                    window.blit(rook_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'n':
                    window.blit(knight_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'b':
                    window.blit(bishop_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'q':
                    window.blit(queen_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'k':
                    window.blit(king_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
                elif board.piece_at(64-i).symbol() == 'p':
                    window.blit(pawn_black, (100*(((i-1)%8)+1), 800-100*((i-1)//8)))
            except AttributeError:
                pass
def main():

    # Create the pygame object and window and generate the initial internal board
    pygame.init()
    board = chess.Board()
    window = pygame.display.set_mode((1000, 1000))

    # Create the textbox to ask the player for the board theme
    theme_box = TextBox(window, 100, 900, 800, 50, placeholderText='Which theme: Wood, Ice, or Forest?', fontSize=30)

    # Initialize theme as the empty string
    theme = ''

    # While the entered text is not an option,
    # continue looping through and changing theme to be the new entered text
    valid_choice = False
    while not valid_choice:
        theme = theme_box.getText()
        if theme in ['Wood', 'Ice', 'Forest']:
            valid_choice = True
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                valid_choice = True
                quit()

        pygame_widgets.update(events)
        pygame.display.update()

    # Set the colors to be used to fill the board
    if theme == 'Wood':
        light = 'tan'
        dark = 'brown'
    elif theme == 'Ice':
        light = 'white'
        dark = 'light blue'
    else:
        light = 'light green'
        dark = 'dark green'

    # Textbox for asking the user which color of pieces they will be playing with
    textbox_1 = TextBox(window, 100, 900, 800, 50, placeholderText='Please enter desired piece color.', fontSize=30)

    # Initialize color as the empty string
    color = ''

    # While the entered text is not an option,
    # continue looping through and changing color to be the new entered text
    valid_color = False
    while not valid_color:
        color = textbox_1.getText()
        if color == "White" or color == "Black":
            valid_color = True
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                valid_color = True
                quit()

        pygame_widgets.update(events)
        pygame.display.update()

    # This sets which side will be making the first move
    # Odd numbers mean the human player will make the next move
    # Even numbers mean the computer will make the next move
    if color == "White":
        ply = 1
    else:
        ply = 2

    # Textbox for asking the user if they will be playing against Stockfish
    opponent_box = TextBox(window, 100, 900, 800, 50, placeholderText='Play against Stockfish?', fontSize=30)

    # Initialize opponent as the empty string
    opponent = ''

    # While the entered text is not an option,
    # continue looping through and changing opponent to be the new entered text
    valid_choice = False
    while not valid_choice:
        opponent = opponent_box.getText()
        if opponent == "Yes" or opponent == "No":
            valid_choice = True
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                valid_choice = True
                quit()

        pygame_widgets.update(events)
        pygame.display.update()

    # If the user would like to play against Stockfish, attempt to load Stockfish
    if opponent == "Yes":
        try:
            stockfish = Stockfish(path="stockfish")

            # If the loading of Stockfish is successful
            # There will be a textbox asking which skill level of Stockfish the user will face
            skill_box = TextBox(window, 100, 900, 800, 50, placeholderText="Which skill level to face? (00-20)",
                                fontSize=30)

            # Initialize skill to the empty string
            skill = ''
            valid_skill = False

            # While the entered text is not an option,
            # continue looping through and changing skill to be the new entered text
            # Convert the entered skill to an int as well
            while not valid_skill:
                skill = skill_box.getText()
                if skill in ['00', '01', '02', '03', '04', '05', '06',
                             '07', '08', '09', '10', '11', '12', '13',
                             '14', '15', '16', '17', '18', '19', '20']:
                    valid_skill = True
                    int_skill = int(skill)
                    stockfish.set_skill_level(int_skill)
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        game_done = True
                        quit()

                pygame_widgets.update(events)
                pygame.display.update()

        except:
            # If the loading of Stockfish is unsuccessful,
            # a textbox will appear asking the user to enter anything to continue
            opponent = "No"
            error_textbox = TextBox(window, 100, 900, 800, 50, placeholderText="Stockfish is unavailable.",
                                    fontSize=30)
            ok = False
            while not ok:
                entered = error_textbox.getText()
                if len(entered) > 0:
                    ok = True
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        game_done = True
                        quit()

                pygame_widgets.update(events)
                pygame.display.update()

    # Initialize game_done as false to start while loop
    game_done = False

    # Initialize exit_message as false
    exit_message = False

    # While the game is not over, keep looping through moves
    while not game_done:

        # Prevents pygame from crashing
        pygame.event.get()

        # Draw and display the board
        draw_board(window, board, color, dark, light)
        pygame.display.flip()

        # If it is the user's move
        if ply % 2 == 1:

            # Create a textbox asking the user for their move
            textbox_2 = TextBox(window, 100, 900, 800, 50, placeholderText='Please enter your move.',
                                fontSize=30)

            # Initialize move to the empty string and castle to False
            move = ''
            castle = False

            # Get list of all legal moves in the position
            candidate_moves = str.split(str(board.legal_moves)[38:-2], ', ')

            # While the entered text is not a legal move,
            # continue looping through and changing move to be the new entered text
            valid_move = False
            while not valid_move:
                move = textbox_2.getText()
                if move in candidate_moves:
                    # If both O-O and O-O-O are legal moves,
                    # if the user enters O-O stop loop and set castle = True
                    # In any other scenario, if the user has entered a legal move, play the move
                    # and advance to the computer's move
                    if move == 'O-O' and 'O-O-O' in candidate_moves:
                        valid_move = True
                        castle = True
                    else:
                        valid_move = True
                        board.push_san(move)
                        print("Player played move " + move)
                        ply = ply + 1
                # If the user resigns, stop the loop and go to the exit message
                elif move == 'Resign':
                    valid_move = True
                    exit_message = True
                # If the user successfully claims a draw, stop the loop and go to the exit message
                elif move == 'Draw':
                    if board.can_claim_threefold_repetition():
                        valid_move = True
                        exit_message = True
                    elif board.can_claim_fifty_moves():
                        valid_move = True
                        exit_message = True
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        valid_move = True
                        quit()

                pygame_widgets.update(events)
                pygame.display.update()

            # In the special castling scenario, generate a textbox
            # that asks the user if they would like to castle long or short
            if castle:

                castle_box = TextBox(window, 100, 900, 800, 50, placeholderText='Long or Short?',
                                    fontSize=30)

                # Initialize distance as the empty string
                distance = ''

                # While the entered text is not an option,
                # continue looping through and changing distance to be the new entered text
                # Once a valid option has been entered, make the move and advance to the computer's move
                valid_castle = False
                while not valid_castle:
                    distance = castle_box.getText()
                    if distance == 'Long':
                        board.push_san('O-O-O')
                        print("Player played move O-O-O")
                        ply = ply + 1
                        valid_castle = True
                    elif distance == 'Short':
                        board.push_san('O-O')
                        print("Player played move O-O")
                        ply = ply + 1
                        valid_castle = True
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            valid_move = True
                            quit()

                    pygame_widgets.update(events)
                    pygame.display.update()

        # If it is the computer's move and the computer is not Stockfish,
        # get all legal moves, select a random one from the list, make the move, and advance to the user's move
        elif opponent == 'No':
            candidate_moves = str.split(str(board.legal_moves)[38:-2], ', ')
            i = random.randint(0,len(candidate_moves)-1)
            board.push_san(candidate_moves[i])
            print("Computer played move " + candidate_moves[i])
            ply = ply + 1

        # If it is the computer's move and the computer is Stockfish,
        # set Stockfish to analyze the current position, think for 1 second,
        # make what it deems to be the best move, then advance to the user's move
        else:

            stockfish.set_fen_position(board.fen())
            move = stockfish.get_best_move_time(1000)
            board.push_san(move)
            print("Computer played move " + move)
            ply = ply + 1

        # If the game has ended, advance to the exit message
        if board.is_game_over():
            exit_message = True

        # If the exit message has been reached
        if exit_message:
            draw_board(window, board, color, dark, light)

            # Create a textbox that shows the appropriate message for how the game ended
            if board.is_checkmate():
                outcome = 'Checkmate! Enter anything to exit.'
            elif board.is_stalemate():
                outcome = 'Stalemate! Enter anything to exit.'
            elif board.is_insufficient_material():
                outcome = 'Insufficient material! Enter anything to exit.'
            elif board.is_fivefold_repetition():
                outcome = 'Fivefold repetition! Enter anything to exit.'
            elif board.is_seventyfive_moves():
                outcome = '75-move rule! Enter anything to exit.'
            elif move == 'Resign':
                outcome = 'You resigned! Enter anything to exit.'
            elif move == 'Draw':
                outcome = 'Draw claimed! Enter anything to exit.'
            else:
                outcome = 'Game over! Enter anything to exit.'

            textbox_3 = TextBox(window, 100, 900, 800, 50, placeholderText=outcome,
                                fontSize=30)

            # Entering anything to continue will stop the loop and end the program
            while not game_done:
                entry = textbox_3.getText()
                if len(entry) > 0:
                    game_done = True
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        game_done = True
                        quit()

                pygame_widgets.update(events)
                pygame.display.update()

main()