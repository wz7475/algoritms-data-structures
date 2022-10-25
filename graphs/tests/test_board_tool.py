from board_tool import BoardTool


def test_read_matrix():
    tool = BoardTool("testmatrix.txt")
    assert tool.get_board() == ["12", "34"]


def test_convert_matrix():
    tool = BoardTool("testmatrix.txt")
    assert tool.convert_board() == {
        0: {1: 2, 2: 3},
        1: {0: 1, 3: 4},
        2: {0: 1, 3: 4},
        3: {2: 3, 1: 2}
    }


def test_show_shortest_path():
    tool = BoardTool("testmatrix2.txt")
    assert tool.show_shortest_path([2, 5]) == tool.show_shortest_path([1, 2, 5, 8]) == " 03\n  3\n  0\n"
    tool.save_shortest_path("shortestresult.txt", [2, 5])