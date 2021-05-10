def write_to_file(filename, board):
    # writing actual board to file
    size_x = len(board[0])
    text = ''
    num_bombs = 0
    for line in board:
        if len(line) != size_x:
            raise ValueError('Size x of board must be const')
        for field in line:
            if field == '*':
                text += '*'
                num_bombs += 1
            else:
                text += '.'
        if line != board[-1]:
            text += '\n'
    if num_bombs not in range(10, (size_x-1)*(len(board)-1)+1):
        raise ValueError('Invalid amount of mines in board')
    try:
        file = open(f"{filename}", "w")
        file.write(text)
        file.close()
    except PermissionError:
        print('File permission error')
        return -1
    except IsADirectoryError:
        print('given path is a directory')
        return -1
    except Exception:
        print('Problem with file')
        return -1


def open_file(filename):
    # read board from file
    try:
        file = open(filename, "r")
        file_board = file.readlines()
        file.close()
        return file_board
    except FileNotFoundError:
        print("File not find")
        return -1
    except PermissionError:
        print('File permission error')
        return -1
    except IsADirectoryError:
        print('given path is a directory')
        return -1
    except Exception:
        print('Problem with file')
        return -1


def filehandle_board(file_board):
    # check if the file_handle file_board
    # is invalid
    # return board list
    board = []
    mine_counter = 0
    try:
        board_x = len(file_board[0]) - 1
        if board_x not in range(8, 31) or len(file_board) not in range(8, 25):
            print('board size out of range in file\n')
            return -1
        for line in range(len(file_board)):
            board_line = []
            if len(file_board[line]) - 1 != board_x and line != board_x - 1:
                print('Length of lines are not const in file\n')
                return -1
            for element in file_board[line]:
                if element == "\n":
                    break
                if element not in ['.', '*']:
                    print(f'{element} can not exist in file in file\n')
                    return -1
                if element == '*':
                    mine_counter += 1
                board_line.append(element)
            board.append(board_line)
        if mine_counter not in range(10, (board_x - 1)*(len(file_board)-1)):
            print('invalid number of mines in board in file\n')
            return -1
        return board
    except Exception:
        print('Data file is not correct\n')
        return -1
