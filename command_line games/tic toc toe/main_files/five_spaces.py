import random



class TicTacToe:
    """This is the main class of five grids tic tac toe ."""
    def __init__(self, msg):
        self.__list = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']] # Initializing grid layout as matrix.
        self.__dic = lambda x: (x - 1) % 5 # This line is for indexing the grid by row.
        self.__divide = lambda p: (p - 1) // 5 # This is for indexing the grid by column.
        self.msg = msg

    """This program just print the grid in a nice way."""
    def __print_asset(self):
        for k in range(len(self.__list)):
            lines = '__'

            print(*self.__list[k], sep='    |    ')
            if k < 4:
                print(lines * 21)

    """This one checks if the board is draw or not."""
    def __check_draw(self):
        for i in range(5):
            for j in range(5):
                if self.__list[i][j] == ' ':
                    return False
        return True

    """This program find a match by column """
    def __check_col(self, c):
        c_b = [c, c, c, c, c]
        for i in self.__list:
            if i == c_b:
                return True
        return False

    """This one find match by row"""
    def __check_row(self, c):
        c_b = [c, c, c, c, c]
        temp = []
        for i in range(5):

            for j in range(5):
                temp.append(self.__list[j][i])
            if temp == c_b:
                return True
            temp = []
        return False

    """This program checks the grid cross wise if any match found it'll return True"""
    def __check_cross(self, c):
        c_b = [c, c, c, c, c]
        temp = [self.__list[0][0], self.__list[1][1], self.__list[2][2], self.__list[3][3], self.__list[4][4]]
        temp1 = [self.__list[0][4], self.__list[1][3], self.__list[2][2], self.__list[3][1], self.__list[4][0]]
        return temp == c_b or temp1 == c_b

    """Driver program of finding match in the grid"""
    def __is_match(self, c):
        return self.__check_cross(c) or self.__check_col(c) or self.__check_row(c)

    """This program checks the validity of given index in main method/function"""
    def __validity(self, idx):
        if idx <= 0 or idx > 25:
            return False

        return self.__list[self.__divide(idx)][self.__dic(idx)] == ' '

    """This's just a collaboration method"""
    def __win(self, name):
        self.msg.win()
        self.__print_asset()
        self.msg.win1()
        print(f'{name} is  winner of the match.')

    """This method is  for playing with your opponent or friend by randomly generated toss [H/T] """
    def players(self):
        player1 = input('Enter First Player name: ')
        player2 = input('Enter Second Player name: ')

        choose = self.msg.choose()
        res = random.choice(['H', 'T'])
        if res == choose:
            print()

            print(f'{player1} , You have own the toss . Your Sing is "X" ')
            print()
            print(f'{player2} , You lose the toss . Your sing is "O"')
            self.main(player1, player2)
        else:
            print()

            print(f'{player2} has own the toss . {player2}\'s sing is "X" ')
            print()
            print(f'{player1} , You lose the toss . Your sing is "O"')
            print()
            self.main(player2, player1)

    """This method is responsible for your move in the grid"""
    def __move(self, player, val='X'):
        while True:
            try:
                p = int(input(f'{player} Enter your move: '))
                break
            except ValueError:
                self.msg.wrong_input()

        if not self.__validity(p):
            while True:
                self.msg.wrong_index()
                p = int(input(f'{player} Enter your move: '))
                if self.__validity(p):
                    break

        self.__list[self.__divide(p)][self.__dic(p)] = val

    """This method print's the board"""
    def __board(self):
        self.msg.board5()
        self.__print_asset()
        print()

    """Main driver function of this whole class .Takes input's checks it's validity make moves predict win or not.
        Also predicts draw ."""
    def main(self, player1=None, player2=None):
        for i in range(5):
            if i == 0:
                self.msg.hint5()
                self.__board()

            if player1 is None or player2 is None:
                player1 = 'Player1'
                player2 = 'Player2'
            self.__move(player1)

            if self.__check_draw():
                self.__board()
                print('Match Draw')

                return

            if self.__is_match('X'):
                self.__win(player1)
                return

            self.__board()

            self.__move(player2, 'O')

            if self.__check_draw():
                self.__board()
                print('Match Draw')

                return
            if self.__is_match('O'):
                self.__win(player2)

            self.__board()

    """This one just print's the grid  in a regular way."""
    def print_list(self):
        return self.__list


# To start the game you can call the players method or main method.
# If you call the player method you've to enter your name and make a choice for toss.
# If you directly call the main method nothing to do you play as it is.The first player sing will be always 'X' .
