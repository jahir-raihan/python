import time

"""This whole file contains space eater messages and designs .
You can make this on your own"""


def message():
    print()
    print('If you want to play with three grids enter 3 ,\nElse enter 5 to play with 5 grids')
    print()
    print("Also if you want to play with your friend using your and your friend's name\n"
          "then you can enter 'player' in the player input section.")
    print()


def win():
    print()
    print('Final result:')
    print()


def win1():
    print()
    print("Holaa match Finished!")
    print()


def board5():
    print()
    print('                 BOARD   ')
    print('             -------------- ')
    print()
    print()


def board3():
    print()
    print('    BOARD   ')
    print('-------------- ')
    print()


def hint5():
    print()
    print('Please read the text below: ')

    print()
    print("""The index start from 1 and end with 25.
Every new line is separated by 5 spaces. Enjoy.......""")
    time.sleep(2)


def hint3():
    print()
    print('Please read the text below: ')

    print()
    print("""The index start from 1 and ends with 9.
Every new line is separated by 3 spaces. Enjoy.......""")
    time.sleep(2)


def wrong_index():
    print('The space is  already filled or wrong index please Enter another number.')
    print()


def wrong_input():
    print("You've entered wrong input. Please enter correct one.")
    print()


def choose():
    cho = input(f'What do you want to choose (Head)-> h or (Tail)-> t : ').upper()
    return cho


def board_system3():
    print()
    print('                     This 3s grid is being initialized from index 1 to 9 .')
    print("          If you want to choose a particular position you've to enter index as shown below.")
    print()
    print()
    print('                                 |          |         ')
    print('                              1  |     2    |   3     ')
    print('                           -------------------------  ')
    print('                                 |          |         ')
    print('                             4   |     5    |   6     ')
    print('                           -------------------------  ')
    print('                                 |          |         ')
    print('                             7   |     8    |   9     ')


def board_system5():
    print()
    print('                     This 5s grid is being initialized from index 1 to 25 .')
    print("          If you want to choose a particular position you've to enter index as shown below.")
    print()
    print()
    print('                                 |          |          |          |       ')
    print('                              1  |     2    |    3     |     4    |    5  ')
    print('                          ------------------------------------------------')
    print('                                 |          |          |          |       ')
    print('                              6  |     7    |    8     |     9    |   10  ')
    print('                          ------------------------------------------------')
    print('                                 |          |          |          |       ')
    print('                             11  |    12    |    13    |    14    |   15  ')
    print('                          ------------------------------------------------')
    print('                                 |          |          |          |       ')
    print('                             16  |    17    |    18    |    19    |   20  ')
    print('                          ------------------------------------------------')
    print('                                 |          |          |          |       ')
    print('                             21  |    22    |    23    |    24    |   25  ')

import os
os.system('/Users/nazrulislam/Desktop/python/pythonProject/tic toc toe/boardsys')
