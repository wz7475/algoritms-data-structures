from typing import List


class BoardTool:
    def __init__(self, filename: str) -> None:
        self.__board = self.__read_board(filename)

    def get_board(self) -> List[str]:
        return self.__board

    def get_board_str(self) -> str:
        result_str = ""

        for line in self.__board:
            result_str += line
            result_str += "\n"

        return result_str

    def convert_board(self) -> dict:
        result_graph = {}
        node_counter = 0

        line_length = len(self.__board[0])

        for line_id in range(len(self.__board)):
            for character_id in range(line_length):
                # check left
                if character_id > 0:
                    if node_counter - 1 not in result_graph:
                        result_graph[node_counter - 1] = {}

                    result_graph[node_counter - 1][node_counter] = int(self.__board[line_id][character_id])

                # check up
                if line_id > 0:
                    result_graph[node_counter - line_length][node_counter] = int(self.__board[line_id][character_id])

                # check right
                if character_id < line_length - 1:
                    if node_counter + 1 not in result_graph:
                        result_graph[node_counter + 1] = {}

                    result_graph[node_counter + 1][node_counter] = int(self.__board[line_id][character_id])

                # check bottom
                if line_id < len(self.__board) - 1:
                    if node_counter + line_length not in result_graph:
                        result_graph[node_counter + line_length] = {}

                    result_graph[node_counter + line_length][node_counter] = int(self.__board[line_id][character_id])

                node_counter += 1

        return result_graph

    def show_shortest_path(self, vertices: List[int]) -> str:
        result_str = ""
        new_lines = []
        line_length = len(self.__board[0])
        current_vertex = 0

        for line in self.__board:
            new_line = ""

            for char in line:
                if current_vertex in vertices or char == "0":
                    new_line += line[current_vertex % line_length]
                else:
                    new_line += " "

                current_vertex += 1
            
            new_lines.append(new_line)

        for line in new_lines:
            result_str += line + "\n"

        return result_str

    def save_shortest_path(self, out_filename: str, vertices: List[int]) -> None:
        with open(out_filename, mode="w") as f:
            f.write(self.show_shortest_path(vertices))

    def __read_board(self, filename: str) -> List[str]:
        with open(filename) as f:
            lines =  f.readlines()

        new_lines = []

        for line in lines:
            if line[-1] == "\n":
                new_lines.append(line[:-1])
            else:
                new_lines.append(line)

        return new_lines