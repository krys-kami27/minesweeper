from model_io import write_to_file, filehandle_board, open_file
from pytest import raises
from io import StringIO


def test_write_to_file_not_const_size_rows():
    board = [
        ['*', '*',  3,   3,   2,  1,  0,   0],
        ['*',  7,  '*', '*', '*', 1,  0,   0],
        ['*', '*', '*',  5,   2,  1,  0,   0],
        ['*', '*', '*',  3,   0,  0,  0],
        ['*',  8,  '*',  3,   0,  1,  2,   2],
        ['*', '*', '*',  2,   0,  1, '*', '*'],
        ['*',  6,   3,   1,   0,  2,  4,   4],
        ['*', '*',  1,   0,   0,  1, '*', '*']
        ]
    with raises(ValueError):
        write_to_file('test_saper_board.txt', board)


def test_write_to_file_invalid_amount_of_mines():
    board = [
        ['*', '*',  2,   1,   0,  0,  0,   0],
        ['*',  7,  '*',  2,   0,  0,  0,   0],
        ['*', '*', '*',  2,   0,  0,  0,   0],
        [2,   3,   2,   1,   0,  0,  0,   0],
        [0,   0,   0,   0,   0,  0,  0,   0],
        [0,   0,   0,   0,   0,  0,  0,   0],
        [0,   0,   0,   0,   0,  0,  0,   0],
        [0,   0,   0,   0,   0,  0,  0,   0]
        ]
    with raises(ValueError):
        write_to_file('test_saper_board.txt', board)


def test_open_file_not_exist():
    assert open_file('random_name_jdknewercfjk.txt') == -1


def test_open_file_is_directory():
    assert open_file('/') == -1


def test_open_file_empty_name():
    assert open_file('') == -1


def test_filehandle_check_correct_board():
    file_board = """...*....
........
..*.....
..*.*...
......**
*.......
.*.*....
.....*.."""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == [
        ['.', '.', '.', '*', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '*', '.', '*', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '*', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '*', '.', '*', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '*', '.', '.']]


def test_filehandle_check_too_less_mines():
    file_board = """...*....
...*....
...*....
...*....
...*....
...*....
...*....
...*...."""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1


def test_filehandle_check_invalid_char_in_board():
    file_board = """...*....
...*...*
...*...*
...*...1
...*....
...*....
...*....
...*...."""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1


def test_filehandle_check_too_much_mines():
    file_board = """........
**......
********
********
********
********
********
********"""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1


def test_filehandle_check_size_y_invalid():
    file_board = """...*....
...*...*
...*...*
...*....
...*....
...*....
...*...."""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1


def test_filehandle_check_size_x_is_not_const():
    file_board = """...*....
...*...*
...*...*
...*....
...*..
...*....
...*....
...*...."""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1


def test_filehandle_check_size_x_is_invalid():
    file_board = """..*....
...*...
...*...
...*...
...*...
...*...
...*..*
...*..*"""
    file_handle = StringIO(file_board).readlines()
    assert filehandle_board(file_handle) == -1
