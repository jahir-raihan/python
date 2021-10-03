import random

"""This whole file is also same as the five_spaces.py file . Just modified few thing to work finely."""


class TicTacToe:
    def __init__(self, msg):
        self.__list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.__dic = lambda x: (x - 1) % 3
        self.__divide = lambda p: (p - 1) // 3
        self.msg = msg

    def __print_asset(self):
        for k in range(len(self.__list)):
            lines = '__'
            print(*self.__list[k], sep='  |  ')
            if k < 2:
                print(lines * 7)

    def __check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.__list[i][j] == ' ':
                    return False
        return True

    def __check_row(self, c):
        c_b = [c, c, c]
        for i in self.__list:
            if i == c_b:
                return True
        return False

    def __check_col(self, c):
        c_b = [c, c, c]
        temp = []
        for i in range(3):

            for j in range(3):
                temp.append(self.__list[j][i])
            if temp == c_b:
                return True
            temp = []
        return False

    def __check_cross(self, c):
        c_b = [c, c, c]
        temp = [self.__list[0][0], self.__list[1][1], self.__list[2][2]]
        temp1 = [self.__list[0][2], self.__list[1][1], self.__list[2][0]]
        return temp == c_b or temp1 == c_b

    def __is_match(self, c):
        return self.__check_cross(c) or self.__check_col(c) or self.__check_row(c)

    def __validity(self, idx):
        if 9 < idx < 0:
            return False

        return self.__list[self.__divide(idx)][self.__dic(idx)] == ' '

    def __win(self, name):
        self.msg.win()
        self.__print_asset()
        self.msg.win1()
        print(f'{name} is  winner of the match.')

    def players(self):
        player1 = input('Enter First Player name: ')
        player2 = input('Enter Second Player name: ')

        choose = input(f'What do you want to choose {player1} (Head)-> h or (Tail)-> t : ').upper()
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

    def __board(self):
        self.msg.board3()
        self.__print_asset()
        print()

    def main(self, player1=None, player2=None):
        for i in range(5):
            if i == 0:
                self.msg.hint3()
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
                return

            self.__board()

    def print_board(self):
        self.__board()


# To start the game you can call the players method or main method.
# If you call the player method you've to enter your name and make a choice for toss.
# If you directly call the main method nothing to do you play as it is.The first player sing will always 'X' .
