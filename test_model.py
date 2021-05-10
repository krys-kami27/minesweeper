from model import Board
from pytest import raises
from _pytest.monkeypatch import MonkeyPatch


def test_create_correct_smallest_board():
    board = Board(8, 8, 49)
    assert board._size_x == 8
    assert board._size_y == 8
    assert board._num_bombs == 49
    assert board._num_flags == 49
    assert board._discovered_fields == 0
    assert board._board == [[0 for _ in range(8)] for _ in range(8)]
    assert board._print_board == [['.' for _ in range(8)] for _ in range(8)]


def test_create_correct_biggest_board():
    board = Board(30, 24, 667)
    assert board._size_x == 30
    assert board._size_y == 24
    assert board._num_bombs == 667
    assert board._num_flags == 667
    assert board._discovered_fields == 0
    assert board._board == [[0 for _ in range(30)] for _ in range(24)]
    assert board._print_board == [['.' for _ in range(30)] for _ in range(24)]


def test_create_correct_some_board():
    board = Board(17, 13, 119)
    assert board._size_x == 17
    assert board._size_y == 13
    assert board._num_bombs == 119
    assert board._num_flags == 119
    assert board._discovered_fields == 0
    assert board._board == [[0 for _ in range(17)] for _ in range(13)]
    assert board._print_board == [['.' for _ in range(17)] for _ in range(13)]


def test_create_board_too_small_size_x():
    with raises(ValueError):
        Board(7, 24, 10)


def test_create_board_too_big_size_x():
    with raises(ValueError):
        Board(31, 24, 10)


def test_create_board_too_small_size_y():
    with raises(ValueError):
        Board(10, 7, 10)


def test_create_board_too_big_size_y():
    with raises(ValueError):
        Board(10, 25, 10)


def test_create_board_too_small_number_bombs():
    with raises(ValueError):
        Board(10, 25, 9)


def test_create_board_too_big_number_bombs():
    with raises(ValueError):
        Board(10, 20, 200)


def test_create_board_size_x_is_string():
    with raises(ValueError):
        Board('20', 20, 10)


def test_create_board_size_y_is_string():
    with raises(ValueError):
        Board(20, '20', 10)


def test_create_board_number_of_bombs_is_string():
    with raises(ValueError):
        Board(20, 20, '10')


def test_create_board_number_of_bombs_is_empty():
    with raises(ValueError):
        Board(20, 20)


def test_set_random_mines(monkeypatch):
    def return_numbers_list(f, t):
        return [1, 5, 15, 20, 30, 37, 39, 54, 59, 60]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    assert board._board[0] == [0, '*', 0, 0, 0, '*', 0, 0]
    assert board._board[1] == [0, 0, 0, 0, 0, 0, 0, '*']
    assert board._board[2] == [0, 0, 0, 0, '*', 0, 0, 0]
    assert board._board[3] == [0, 0, 0, 0, 0, 0, '*', 0]
    assert board._board[4] == [0, 0, 0, 0, 0, '*', 0, '*']
    assert board._board[5] == [0, 0, 0, 0, 0, 0, 0, 0]
    assert board._board[6] == [0, 0, 0, 0, 0, 0, '*', 0]
    assert board._board[7] == [0, 0, 0, '*', '*', 0, 0, 0]


def test_set_random_mines_more_than_once_error(monkeypatch):
    def return_numbers_list(f, t):
        return [1, 5, 15, 20, 30, 37, 39, 54, 59, 60]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.set_random_mines()


def test_set_all_values(monkeypatch):
    def return_numbers_list(f, t):
        return [1, 5, 15, 20, 30, 37, 39, 54, 59, 60]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    assert board._board[0] == [1, '*', 1,  0,   1, '*', 2,  1]
    assert board._board[1] == [1,  1,  1,  1,   2,  2,  2, '*']
    assert board._board[2] == [0,  0,  0,  1,  '*', 2,  2, 2]
    assert board._board[3] == [0,  0,  0,  1,   2,  3, '*', 2]
    assert board._board[4] == [0,  0,  0,  0,   1, '*', 3, '*']
    assert board._board[5] == [0,  0,  0,  0,   1,  2,  3, 2]
    assert board._board[6] == [0,  0,  1,  2,   2,  2, '*', 1]
    assert board._board[7] == [0,  0,  1, '*', '*', 2,  1, 1]


def test_set_all_values_two_points_with_value_eight(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 8, 10, 16, 17, 18, 24, 25, 26, 32, 34, 40, 41, 42]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 16)
    board.set_random_mines()
    board.set_values()
    print(board._board)
    assert board._board[0] == ['*', '*', '*', 2, 0, 0, 0, 0]
    assert board._board[1] == ['*', 8, '*', 3, 0, 0, 0, 0]
    assert board._board[2] == ['*', '*', '*', 3, 0, 0, 0, 0]
    assert board._board[3] == ['*', '*', '*', 3, 0, 0, 0, 0]
    assert board._board[4] == ['*', 8, '*', 3, 0, 0, 0, 0]
    assert board._board[5] == ['*', '*', '*', 2, 0, 0, 0, 0]
    assert board._board[6] == [2,    3,   2, 1, 0, 0, 0, 0]
    assert board._board[7] == [0, 0, 0, 0, 0, 0, 0, 0]


def test_set_all_values_all_possible_values_exist(monkeypatch):
    def return_numbers_list(f, t):

        return [
                0, 1, 8, 10, 11, 12, 16, 17, 18, 24, 25, 26,
                32, 34, 40, 41, 42, 46, 47, 48, 56, 57, 62, 63]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 24)
    board.set_random_mines()
    board.set_values()
    lista = [
        ['*', '*',  3,   3,   2,  1,  0,   0],
        ['*',  7,  '*', '*', '*', 1,  0,   0],
        ['*', '*', '*',  5,   2,  1,  0,   0],
        ['*', '*', '*',  3,   0,  0,  0,   0],
        ['*',  8,  '*',  3,   0,  1,  2,   2],
        ['*', '*', '*',  2,   0,  1, '*', '*'],
        ['*',  6,   3,   1,   0,  2,  4,   4],
        ['*', '*',  1,   0,   0,  1, '*', '*']
        ]
    for number in range(8):
        assert board._board[number] == lista[number]


def test_set_values_before_set_mines_error():
    board = Board(8, 8, 10)
    with raises(ValueError):
        board.set_values()


def test_get_value_at_some_points(monkeypatch):
    def return_numbers_list(f, t):
        return [1, 5, 15, 20, 30, 37, 39, 54, 59, 60]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    for line in board._board:
        print(line)
    assert board.get_value_at_indexes(1, 1) == 1
    assert board.get_value_at_indexes(1, 7) == 0
    assert board.get_value_at_indexes(6, 1) == 2
    assert board.get_value_at_indexes(4, 6) == 2
    assert board.get_value_at_indexes(1, 0) == '*'


def test_get_value_too_small_x_index():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes(-1, 0)


def test_get_value_too_small_y_index():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes(0, -1)


def test_get_value_too_big_x_index():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes(8, 0)


def test_get_value_too_big_y_index():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes(0, 8)


def test_get_value_x_index_is_string():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes('4', 0)


def test_get_value_y_index_is_string():
    board = Board(8, 8, 10)
    board.set_random_mines()
    with raises(ValueError):
        board.get_value_at_indexes(0, '5')


def test_get_numbers_line():
    board = Board(8, 8, 20)
    line = '    1  2  3  4  5  6  7  8  \n\n'
    assert board.get_numbers_line() == line


def test_get_numbers_line_to_some_two_decimal_num():
    board = Board(12, 8, 20)
    line = '    1  2  3  4  5  6  7  8  9  10 11 12 \n\n'
    assert board.get_numbers_line() == line


def test_get_board_to_show_while_playing():
    board = Board(8, 8, 10)
    lines = """    1  2  3  4  5  6  7  8  \n
1   .  .  .  .  .  .  .  .
2   .  .  .  .  .  .  .  .
3   .  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    assert board.get_board() == lines


def test_get_flags():
    board = Board(8, 8, 20)
    assert board.get_flags() == 20


def test_set_field_where_is_mine(monkeypatch):
    def return_numbers_list(f, t):
        return [
                0, 1, 8, 10, 11, 12, 16, 17, 18, 24, 25, 26,
                32, 34, 40, 41, 42, 46, 47, 48, 56, 57, 62, 63]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 24)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(3, 1, 'd') is False
    board_get = """    1  2  3  4  5  6  7  8  \n
1   .  .  3  .  .  .  .  .
2   .  .  .  .  .  .  .  .
3   .  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    print(board.get_board())
    assert board.get_board() == board_get


def test_set_field_where_is_mine(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(1, 1, 'd') is True
    board_get = """    1  2  3  4  5  6  7  8  \n
1   *  *  *  *  *  *  *  *
2   *  *  .  .  .  .  .  .
3   .  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    assert board.get_board_with_mines() == board_get


def test_set_field_first_good_second_mine(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(1, 3, 'd') is False
    assert board.set_field(1, 2, 'd') is True
    board_get = """    1  2  3  4  5  6  7  8  \n
1   *  *  *  *  *  *  *  *
2   *  *  .  .  .  .  .  .
3   2  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    assert board.get_board_with_mines() == board_get


def test_set_field_not_discover_where_is_flag(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(1, 2, 'f') is False
    assert board.set_field(1, 2, 'f') is False
    assert board.set_field(1, 2, 'd') is True
    board_get = """    1  2  3  4  5  6  7  8  \n
1   *  *  *  *  *  *  *  *
2   *  *  .  .  .  .  .  .
3   f  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    assert board.get_board_with_mines() == board_get


def test_set_field_not_discover_where_is_flag(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(1, 3, 'f') is False
    assert board.set_field(1, 3, 'd') is False
    board_output = """    1  2  3  4  5  6  7  8  \n
1   .  .  .  .  .  .  .  .
2   .  .  .  .  .  .  .  .
3   f  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    assert board.get_board() == board_output


def test_set_field_invalid_choice(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    with raises(ValueError):
        board.set_field(1, 3, 's')


def test_set_field_invalid_x_argument(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    with raises(ValueError):
        board.set_field(-1, 3, 's')


def test_set_field_invalid_y_argument(monkeypatch):
    def return_numbers_list(f, t):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 10)
    board.set_random_mines()
    board.set_values()
    with raises(ValueError):
        board.set_field(2, 300, 's')


def test_set_field_which_is_already_discovered(monkeypatch):
    def return_numbers_list(f, t):
        return [
                0, 1, 8, 10, 11, 12, 16, 17, 18, 24, 25, 26,
                32, 34, 40, 41, 42, 46, 47, 48, 56, 57, 62, 63]
    monkeypatch.setattr('model.sample', return_numbers_list)
    board = Board(8, 8, 24)
    board.set_random_mines()
    board.set_values()
    assert board.set_field(3, 1, 'd') is False
    assert board.set_field(3, 1, 'd') is False
    board_get = """    1  2  3  4  5  6  7  8  \n
1   .  .  3  .  .  .  .  .
2   .  .  .  .  .  .  .  .
3   .  .  .  .  .  .  .  .
4   .  .  .  .  .  .  .  .
5   .  .  .  .  .  .  .  .
6   .  .  .  .  .  .  .  .
7   .  .  .  .  .  .  .  .
8   .  .  .  .  .  .  .  .\n"""
    print(board.get_board())
    assert board.get_board() == board_get