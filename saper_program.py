from model import Board
import time
from model_io import write_to_file, filehandle_board, open_file


def set_level():
    # function to set start option/level
    print("Select number")
    print('1. Beginner')
    print('2. Advanced')
    print('3. Expert')
    print('4. Set own board, random mines')
    print('5. Set board from file')
    print('6. Exit the game')
    level = input("Select difficult level: ")
    while level not in [str(num) for num in range(1, 7)]:
        print("Invalid selection, try again!")
        level = input("Select difficult level: ")
    print(f'You choosed {level} option\n')
    return int(level)


def set_selection(size_x, size_y):
    # function to set x, y, and option to discover/set flag
    list_x = [str(x) for x in range(1, size_x + 1)]
    list_y = [str(y) for y in range(1, size_y + 1)]
    x = input(f'Select x value in {range(1, size_x)}: ')
    while x not in list_x:
        x = input(f'Bad value, select x in {range(1, size_x)}: ')
    y = input(f'Select y value in {range(1, size_y)}: ')
    while y not in list_y:
        y = input(f'Bad value, select y in {range(1, size_y)}: ')
    info = "Select 'f' to flag option or 'd' to discover field: "
    option = input(info)
    while option not in ['f', 'd']:
        option = input(f"Invalid option, {info}")
    return (int(x), int(y), option)


def set_own_board():
    # set board with your own parameters from these allowed
    width = input('Set width of board from 8 to 30: ')
    while width not in [str(num) for num in range(8, 31)]:
        width = input('invalid value, Set width of board from 8 to 30: ')
    high = input('Set high of board from 8 to 24: ')
    while high not in [str(num) for num in range(8, 25)]:
        high = input('invalid value, Set high of board from 8 to 24: ')
    width = int(width)
    high = int(high)
    mines = input(f'Set amount mines from 10 to {(width-1)*(high-1)}: ')
    while mines not in [str(num) for num in range(10, (width-1)*(high-1)+1)]:
        mines = input(f'Set amount mines from 10 to {(width-1)*(high-1)}: ')
    return Board(width, high, int(mines))


def level_from_file():
    # possibility to set board from file
    filename = input('Input name of the file with correct board: ')
    file_handle = open_file(filename)
    if file_handle == -1:
        return -1
    file_board = filehandle_board(file_handle)

    if file_board == -1:
        return -1
    num_bombs = 0
    for y in file_board:
        for point in y:
            if point == '*':
                num_bombs += 1
    return file_board, num_bombs


def chance_to_save_board(board):
    # possibility to save random board to file
    namefile = input('Select namefile: ')
    while write_to_file(namefile, board._board) == -1:
        if input('if you dont want to save board type 1: ') == '1':
            namefile = 0
        if namefile != 0:
            namefile = input('Incorrect namefile, try again: ')


def main():
    # main function
    level = set_level()
    if level == 1:
        board = Board(8, 8, 10)
    elif level == 2:
        board = Board(16, 16, 40)
    elif level == 3:
        board = Board(30, 16, 99)
    elif level == 4:
        board = set_own_board()
    elif level == 5:
        from_file_info = level_from_file()
        if from_file_info == -1:
            return main()
        file_board, num_bombs = from_file_info
        board = Board(len(file_board[0]), len(file_board), num_bombs)
        board.set_board_from_file(file_board)
    elif level == 6:
        print('Thanks for game, bye')
        exit()
    if level != 5:
        board.set_random_mines()
    board.set_values()
    print(f'There are {board.get_flags()} flags to use')
    print(board.get_board())
    selection = set_selection(board._size_x, board._size_y)
    end_game = board.set_field(selection[0], selection[1], selection[2])
    board.set_timer()
    while end_game is not True:
        print(f'There are {board.get_flags()} flags to use')
        print(board.get_board())
        selection = set_selection(board._size_x, board._size_y)
        end_game = board.set_field(selection[0], selection[1], selection[2])
    print(f'The game lasted {int(time.time() - board.get_timer())} seconds.\n')
    print(board.get_board_with_mines())
    save_option = input("Type 1 if you want to save it to file: ")
    if level != 5 and save_option == '1':
        chance_to_save_board(board)


if __name__ == "__main__":
    while True:
        main()
