#####################################################################
# Authors: Yonatan Frohlich, Elhanan Hanel
# file name: gui.py
# description: the logic part for the boggle game with a few 
# function for exercise 11.
#####################################################################


from typing import List, Tuple, Iterable, Optional
import re

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[
    str]:
    """the function gets a path and checks if:
      1) the current block alredy been checked.
      2) the path is in the board.
      3) the path can continue to the block.
      4) if so, add the block to the uses.
      5) after finishing all the blocks, check if the word exists."""

    alredy_check = []
    word = ""
    last_loc = None
    for i in path:
        if i in alredy_check:
            return None
        else:
            alredy_check.append(i)
        if len(board) <= i[0] or i[0] < 0:
            return None
        if len(board[0]) <= i[1] or i[1] < 0:
            return None
        if last_loc != None:
            if not can_move(i, last_loc):
                return None
        word += board[i[0]][i[1]]
        last_loc = i
    if word in words:
        return word
    return None


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    """the fucntion calls a recursin function that return all the paths with
    the
    length of 'n', of exsiting words"""
    result_words = []  # type: List[str]
    result_way = []  # type: List[Path]
    used = []  # type: List[tuple[int,int]]
    dict_word = {}  # type:dict[str,Path]
    loc = None
    word = ""
    counter = 0
    recursian_helper(n, board, sorted(words), used, loc, word, counter,
                     result_way, result_words, "path", dict_word)
    if "ABCBA" in result_words:
        print(result_way)
    return result_way


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    """the fucntion calls a recursin function that returns all the paths of
    words in length n, of existing words"""
    result_words = []  # type: List[str]
    result_way = []  # type: List[Path]
    used = []  # type: List[tuple[int,int]]
    dict_word = {}  # type:dict[str,Path]
    loc = None
    word = ""
    counter = 0
    recursian_helper(n, board, sorted(words), used, loc, word, counter,
                     result_way, result_words, "words", dict_word)
    return result_way


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """the function return the path of max point of every word"""
    result_words=[] # type: List[str]
    result_way= []  # type: List[Path]
    used = [] # type: List[tuple[int,int]]
    dict_word = {}  # type:dict[str,Path]
    loc = None
    word = ""
    counter = 0
    n = 16
    recursian_helper(n, board, sorted(words), used, loc, word, counter,
                     result_way, result_words, "max", dict_word)
    # print(result_way)
    result_way = []
    for i in dict_word:
        result_way.append(dict_word[i])
    return result_way


def recursian_helper(n: int, board: Board, words: list[str],
                     used: list[tuple[int, int]],
                     loc: Optional[tuple[int, int]], word: str, counter: int,
                     result_way: list[Path],
                     result_words: Optional[list[str]], opthion: str,
                     dict_word: dict[str,Path]) ->None:
    """the funciton check every possible way on the board to creat path,
    but skip on words that can't exist"""

    if (opthion == "path" and counter == n) or (
            opthion == "words" and n == len(word)) or opthion == "max":
        if binary_search(words, word, True):
            way = []
            for i in used:
                way.append(i)
            if opthion == "max":
                dict_word[word] = way
            else:
                result_way.append(way)
        if opthion != "max":
            return
        elif counter == 16:
            return

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) in used:
                continue
            if loc is not None:
                if not can_move((i, j), loc):
                    continue
            if not binary_search(words, word + board[i][j], False):
                continue

            recursian_helper(n, board, words, used + [(i, j)], (i, j),
                             word + board[i][j], counter + 1, result_way,
                             result_words,
                             opthion, dict_word)


def binary_search(words: list[str], word: str, end_word: bool) -> bool:
    """the fucntion chcks if a word is in a list of words with binary search"""
    lb, ub = 0, len(words) - 1
    found = False
    while lb <= ub:
        mid = (lb + ub) // 2
        if end_word and words[mid] == word:
            found = True
            break
        elif not end_word and words[mid][:len(word)] == word:
            found = True
            break
        elif words[mid][:len(word)] < word:
            lb = mid + 1
        else:
            ub = mid - 1
    return found


def can_move(last_loc: tuple[int, int],
             loc: tuple[int, int]) -> bool:
    """the fucntion check if the range between to cordinate is good for the
    game"""
    result = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1),
              (1, -1)]
    check = (last_loc[0] - loc[0], last_loc[1] - loc[1])
    if check in result:
        return True
    else:
        return False
