#####################################################################
# Authors: Yonatan Frohlich, Elhanan Hanel
# file name: gui.py
# description: the graphic interface for the boggle game.
#####################################################################

import tkinter as tk
from boggle_board_randomizer import *
from PIL import ImageTk, Image

SIZE = 4
TIME_LEFT = 180


class Boggle_board:
    """this class represents the graphic interface of a board of boggle.
    the class methods are:
    1. set methods for: score, main label, last_cor, all_coordinates, button_commands
    2. get methods for all attributes.
    3. update methods for: list_of_words, time, coordinates.
    """

    def __init__(self, root: tk.Tk, letter_list: list[list]) -> None:
        """the initiator:
        has many attributs: root, score, all labels (time, score, word), all buttons (letters, enter), a list of all coordinates
        in current session, and a tuple containging the last coordinate.
        there is also variable containing all word approved words."""
        self.__root = root
        self.__root.configure(width=400, height=300)
        self.__letters = letter_list
        self.__var_score = 0
        self.__score_label = self._score_label()

        top = tk.Frame(self.__root)
        top.pack(side=tk.TOP, expand=True,)

        # frameof_found_word
        self.__scrollbar = tk.Scrollbar(self.__root)
        self.__scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.__scrollbar.config(width=20, relief=tk.SUNKEN)
        self.__scroller = self._find_word_label()

        bottom = tk.Frame(self.__root)
        bottom.pack(side=tk.LEFT, expand=True)
        self.__button_list = self._create_buttons(self.__letters, bottom)
        self.__label = self._create_label(top)
        self._var = ""
        self.__var_list_words = []
        self.__timeLabel = tk.Label(
            root, text="Time left: " + str(TIME_LEFT), font=('Helvetica', 12), bg="#000fff000")
        self.__timeLabel.pack(side=tk.RIGHT)
        self.__enter = self._create_enter_button()
        self.__last_coordinate = ()
        self.__all_coordinates = []

    def get_root(self) -> tk.Tk:
        """returns the root."""
        return self.__root

    def flash_time(self):
        if self.__timeLabel.cget("bg") == "white":
            self.__timeLabel.configure(bg="red")
        else:
            self.__timeLabel.configure(bg="white")

    def update_list_words(self, word: str):
        """updates the list containing all approved words."""
        self.__var_list_words.append(word)
        self.__scroller.insert(tk.END, str(word))
        self.__scrollbar.config(command=self.__scroller.yview)

    def get_all_moves(self) -> list:
        """returns the current list of moves"""
        return self.__all_coordinates

    def _score_label(self):
        """creates the score label."""
        score_label = tk.Label(
            self.__root, text=("your score is: " + str(self.__var_score)), font=('Helvetica', 12))
        score_label.pack(side=tk.BOTTOM)
        return score_label

    def _find_word_label(self):
        """create the find words list label"""

        listbox = tk.Listbox(self.__root, yscrollcommand=self.__scrollbar.set)
        listbox.pack(side=tk.LEFT)
        listbox.config(font=("Arial", 20))
        return listbox

    def update_list_cor(self, cor: tuple):
        self.__all_coordinates.append(cor)

    def set_list_cor(self, list: list):
        self.__all_coordinates = list

    def update_last_cor(self, cor: tuple):
        self.__last_coordinate = cor

    def get_last_coordinate(self) -> tuple:
        """returns last coordinate pressed."""
        return self.__last_coordinate

    def set_score(self, score: int):
        """sets the score."""
        self.__var_score = score
        self.__score_label.configure(
            text=("your score is: " + str(self.__var_score)))

    def get_score(self) -> int:
        """returns the current score."""
        return self.__var_score

    def update_time(self, time: str):
        self.__timeLabel.configure(text="Time left: " + time)

    def _create_enter_button(self) -> tk.Button:
        """This function creates the enter button which has two
        utilites:
        1. deleting the string in the label
        2. sending the string to the logic class.
        """
        # enter button
        enter_frame = tk.Frame(self.__root)

        enter_frame.pack(side=tk.RIGHT, expand=True)
        button = tk.Button(enter_frame, text="Enter", bg="orange",
                           width=8, height=30, fg="white")
        button.grid(column=0)
        return button

    def config_enter_cmd(self, commands):
        """This is the functin the button enter is binded to."""
        self.__enter.configure(command=commands)

    def _create_buttons(self, letter_list: list[list], frame: tk.Frame) -> None:
        """this function creates all the buttons for the board."""
        button_list = []
        for list in range(len(letter_list)):
            for letter in range(len(letter_list[list])):
                button = tk.Button(
                    frame, text=letter_list[list][letter], bg="cyan", width=9, height=7, fg="black")
                button_list.append(
                    (button, letter_list[list][letter], list, letter))
                button.grid(column=letter, row=list)
        return button_list

    def _create_label(self, frame: tk.Frame):
        """creates the labels for the game"""
        label_text = tk.Label(frame, width=20, height=2, text="Your word: ", font=(
            "Helvetica", 20))
        label_text.grid(column=0, row=0)
        return label_text

    def set_label(self, texts: str):
        """updates both the label and the variable holding the label infomation."""
        self._var = texts
        self.__label.configure(text="Your word: "+self._var)

    def get_label(self):
        return self._var

    def update_label(self, texts: str):
        """updaets the main label"""
        self._var += texts
        self.__label.configure(text="Your word: "+self._var)

    def set_button_command(self, button: tk.Button, command: callable, list_buttons: list[tuple]) -> None:
        """configures the command a button does."""
        for tuple in self.__button_list:
            if tuple[0] == button:
                list_buttons.append(list_buttons)
                button.configure(command=command)

    def get_button_info_list(self) -> tuple:
        return self.__button_list

    def run(self):
        """run the boggle board."""
        self.__root.mainloop()
