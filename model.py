from random import sample
import time


class Board:
    """
    A class used to represent Board


    Attributes
    -----------
    board : list
        list with the fields to calculations
    print_board : list
        board list used to represent to user
    size_x : int
        x dimension of board
    size_y : int
        y dimension of board
    num_bombs : int
        amount of mines in board
    num_flags : int
        amount of fields to set flag
    discovered_fields : int
        discovered fields in board
    timer : time
        after starting game timer is initialized
    """

    def __init__(self, size_x=0, size_y=0, num_bombs=0):
        """
        Parameters
        ---------
        size_x : int
            x dimension of board
        size_y : int
            y dimension of board
        num_bombs : int
        amount of mines in board
        """
        if size_x not in range(8, 31):
            raise ValueError('Bad value of size x')
        if size_y not in range(8, 25):
            raise ValueError('Bad value of size y')
        if num_bombs not in range(10, (size_x - 1) * (size_y - 1) + 1):
            raise ValueError('Bad value of number bombs')
        range_x = range(size_x)
        range_y = range(size_y)
        self._board = [[0 for _ in range_x] for _ in range_y]
        self._print_board = [['.' for _ in range_x] for _ in range_y]
        self._size_x = size_x
        self._size_y = size_y
        self._num_bombs = num_bombs
        self._num_flags = num_bombs
        self._discovered_fields = 0

    def set_random_mines(self):
        """
        Generate mines on board
        """
        for y in range(self._size_y):
            if '*' in self._board[y]:
                raise ValueError('You can not set again same board')
        for index in sample(range(self._size_x*self._size_y), self._num_bombs):
            self._board[int(index / self._size_x)][index % self._size_x] = '*'

    def set_board_from_file(self, board):
        """
        set board file using secure read function
        """
        self._board = board

    def set_values(self):
        """
        function sets all fields values in boards
        """
        range_x = range(self._size_x)
        range_y = range(self._size_y)
        if self._board == [[0 for _ in range_x] for _ in range_y]:
            raise ValueError('You cant set values before set mines')
        for index_y in range(self._size_y):
            for index_x in range(self._size_x):
                point_value = self.get_value_at_indexes(index_x, index_y)
                self._board[index_y][index_x] = point_value

    def get_value_at_indexes(self, index_x=0, index_y=0):
        """
        Function to get value of one field
        """
        if index_x not in range(self._size_x):
            raise ValueError('Index x is invalid')
        if index_y not in range(self._size_y):
            raise ValueError('Index y is invalid')
        if self._board[index_y][index_x] == '*':
            return '*'
        point_value = 0
        for q in range(1, 4):
            for r in range(1, 4):
                if index_y + 2 - r not in range(self._size_y):
                    continue
                elif index_x + 2 - q not in range(self._size_x):
                    continue
                elif self._board[index_y+2-r][index_x+2-q] == '*':
                    point_value += 1
        return point_value

    def get_numbers_line(self):
        """
        function used to print first line of numbers
        """
        line = '    '
        for number in range(1, self._size_x + 1):
            line += str(number)
            if len(str(number)) == 2:
                line += ' '
            else:
                line += '  '
        line += '\n\n'
        return line

    def get_board(self):
        """
        Function give us a output board
        """
        board = self.get_numbers_line()
        number = 1
        for dim_y in self._print_board:
            if len(str(number)) == 1:
                board += str(number) + ' '
            else:
                board += str(number)
            number += 1
            for dim_x in dim_y:
                if dim_x == 0:
                    board += '   '
                else:
                    board += '  ' + str(dim_x)
            board += '\n'
        return board

    def get_board_with_mines(self):
        """
        Function used to show board with mines
        """
        board = self.get_numbers_line()
        number = 1
        for dim_y in range(self._size_y):
            if len(str(number)) == 1:
                board += str(number) + ' '
            else:
                board += str(number)
            number += 1
            for dim_x in range(self._size_x):
                if self._print_board[dim_y][dim_x] == 'f':
                    board += '  f'
                elif self._board[dim_y][dim_x] == '*':
                    board += '  *'
                elif self._print_board[dim_y][dim_x] == 0:
                    board += '   '
                else:
                    board += '  ' + str(self._print_board[dim_y][dim_x])
            board += '\n'
        return board

    def set_field(self, x, y, option):
        """
        Function to discover/set flag on some field
        """
        x -= 1
        y -= 1
        end_game = False
        if x not in range(self._size_x + 1):
            raise ValueError('Incorrect value of size x')
        if y not in range(self._size_y + 1):
            raise ValueError('Incorrect value of size y')
        if option not in ['f', 'd']:
            raise ValueError("Incorrect value of field option")
        if self._print_board[y][x] not in ['.', 'f']:
            print('This field is already used\n')
            return end_game
        elif self._print_board[y][x] == 'f':
            if option == 'f':
                self._print_board[y][x] = '.'
                self._num_flags += 1
                return end_game
            else:
                print('You can not discover field where is flag\n')
                return end_game
        else:
            if option == 'f':
                self._print_board[y][x] = 'f'
                self._num_flags -= 1
                return end_game
            else:
                if self._board[y][x] == '*':
                    print('Game is over, you lost\n')
                    end_game = True
                    return end_game
                else:
                    self._print_board[y][x] = self._board[y][x]
                    if self._print_board[y][x] == 0:
                        self._set_fields_near_zeros(y, x)
                    self._discovered_fields += 1
                    empty_field = self._size_x * self._size_y - self._num_bombs
                    if self._discovered_fields == empty_field:
                        print("You win the game!\n")
                        end_game = True
                        return end_game
                    return end_game

    def _set_fields_near_zeros(self, y, x):
        """
        Function to set empty spaces near zeros
        """
        for r in range(1, 4):
            for q in range(1, 4):
                if y + 2 - r < 0 or y + 2 - r >= self._size_y:
                    continue
                elif x + 2 - q < 0 or x + 2 - q >= self._size_x:
                    continue
                elif self._print_board[y + 2 - r][x + 2 - q] != '.':
                    continue
                elif self._board[y + 2 - r][x + 2 - q] != 'f':
                    point = self._board[y + 2 - r][x + 2 - q]
                    self._print_board[y + 2 - r][x + 2 - q] = point
                    self._discovered_fields += 1
                    if self._print_board[y + 2 - r][x + 2 - q] == 0:
                        self._set_fields_near_zeros(y + 2 - r, x + 2 - q)

    def set_timer(self):
        """
        timer setter
        """
        self._timer = time.time()

    def get_timer(self):
        """
        timer getter
        """
        return self._timer

    def get_flags(self):
        """
        flags getter
        """
        return self._num_flags
