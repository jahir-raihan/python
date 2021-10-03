from main_files import five_spaces, three_spaces # imported the needed files to work with
import texts # This one is  full with needed texts and decorations.


d = {'3': three_spaces, '5': five_spaces}


class Predict:
    def __init__(self, mode, players=None):
        self.__p = mode.TicTacToe(texts) # Initializing the Tic Tac Toe class with  texts file for further use cases.
        if players is None or players == 'main' or players == '': # Predicting  program by the parameter given.
            self.__c = self.__p.main()
        elif players == 'player' or players == 'p':
            self.__c = self.__p.players()

    """This class is the main driver program.
        I've used little bit of polymorphism in this class"""


texts.message()
while True: # If any kind of error occur this program will rerun unless you select n in again input section.
    try: # Try block for caching errors

        spaces = input('Enter number of grids e.g(3 or 5): ').strip()
        player = input('Enter "player" or "p" to play using names: ').strip()
        p = Predict(d[spaces] if spaces else three_spaces, player)
        print()
        again = input('Want to play again enter [y / n] : ').lower()
        if again and again == 'y':
            continue
        break
    except KeyError as e:
        texts.wrong_input()

# This is a commant line game.