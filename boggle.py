#####################################################################
# Authors: Yonatan Frohlich, Elhanan Hanel
# file name: boggle.py
# description: a program which runs the game of boggle
# using the files gui.py (graphic interface), ex11_utils.py (logic)
# to run it.
#####################################################################


import tkinter as tk
from gui import *
from ex11_utils import *

WORDS = open("boggle_dict.txt", "r").read().split('\n')
TIME_LEFT = 180
NEW_RECORD = False


class Start_button:
    """this class is a start button for the game,
    the start button starts an application (the start button), and 
    when it is clicked the boggle game is launched. (this class also determines
    all of the starting parameters for the game."""

    def __init__(self, root: tk.Tk) -> None:
        """Has a few attributes, the first if the root for the button and
        later for the board.
        teh second the board itself
        and finally a list of words."""
        self.__root = root
        image = tk.PhotoImage(file="text.gif")
        gif_label = tk.Label(
            root, image=image, text="welcome to Boggle!\nPress to start game")
        start_button = tk.Button(
            root, text="Start",
            command=self.start_command,
            font=("Helvetica", 50))

        gif_label.pack()
        start_button.pack()
        start_button.image = image
        start_button.pack()
        self.__board = None
        self.__list_words = []
        self.__high_score = 0

    def create_button_action(self, button, texts: str, row: int, col: int,
                             board: Boggle_board) -> callable:
        """creates a function used for a button. (the 16 letter buttons)."""

        def a():
            next_cor = (row, col)
            last_cor = board.get_last_coordinate()
            if last_cor == () or can_move(last_cor,
                                          next_cor) and next_cor not in \
                    board.get_all_moves():
                board.update_last_cor(next_cor)
                board.update_list_cor(next_cor)
                board.update_label(texts)
                button.configure(bg="red")

        return a

    def enter_command(self) -> str:
        """This is the function the button enter is binded to.
        it resets the label, checks the word, and updates the
        score."""
        board = self.__board
        word = board.get_label()
        score = board.get_score()
        for button in board.get_button_info_list():
            button[0].configure(bg="cyan")

        # checking if word is scorable.
        if word in WORDS and word not in self.__list_words:
            board.update_list_words(word)
            self.__list_words.append(word)
            score += len(word) ** 2
            board.set_score(score)

        # updating all parameters.
        board.set_label("")
        board.set_list_cor([])
        board.update_last_cor(())

    def start_time(self):
        """starts the time"""
        self._countdown()

    def _countdown(self):
        """this is the time countdown - careful TIME_LEFT is a global
        variable!"""
        global TIME_LEFT
        global NEW_RECORD
        board = self.__board

        if TIME_LEFT > 0:
            if TIME_LEFT <= 10:
                board.flash_time()
            TIME_LEFT -= 1
            # update the time left label
            min = str(TIME_LEFT//60)
            second = str(TIME_LEFT % 60)
            if int(second) < 10:
                second = "0" + str(second)
            board.update_time(min+":"+second)

            # run the function again after 1 second.
            board.get_root().after(1000, self._countdown)
        else:
            # end the game and ask for rerun.
            board.get_root().destroy()
            score = board.get_score()
            if score > self.__high_score:
                string = "Out of time! \n New High score! \n your new high " \
                         "score is: " + \
                         str(score) + "\n press to play again."
                self.high_score(score)
            else:
                string = "Out of time! \n your score was: " + str(
                    score) + "\n your high score is: " + str(
                    self.high_score(
                        board.get_score())) + "\n press to play again"
            self.__root = tk.Tk()
            image = tk.PhotoImage(file="score4.png")
            png_label = tk.Label(
                self.__root, image=image,
                text="welcome to Boggle!\nPress to start game")
            png_label.image = image
            if NEW_RECORD:
                png_label.pack()
            play_again = tk.Button(
                self.__root, text=string, command=self.start_command,
                height=20, width=30, font=('Helvetica', 12))
            play_again.pack()

    def high_score(self, score: int) -> int:
        global NEW_RECORD
        if score > self.__high_score:
            self.__high_score = score
            NEW_RECORD = True
            return score
        NEW_RECORD = False
        return self.__high_score

    def _play_again(self):
        """this function asks if the player wants to play again.
        the function terminates the current root and starts a new one.
        is also updates the time."""
        self.__root.destroy()
        root = tk.Tk()
        b = randomize_board(LETTERS)
        self = Boggle_board(root, b)
        c = self.get_button_info_list()
        for tuple in c:
            action = self.create_button_action(tuple[0],
                                               tuple[1], tuple[2], tuple[3],
                                               self)
            self.set_button_command(tuple[0], action, [])
        global TIME_LEFT
        TIME_LEFT = 180
        self.start_time()

    def start_command(self):
        """this function is the command for both the start button and the
        play again button, the function resets all of the parameters for the 
        game and starts a new session."""
        self.__list_words = []
        self.__root.destroy()
        b = randomize_board(LETTERS)
        self.__root = tk.Tk()
        board = Boggle_board(self.__root, b)
        self.__board = board
        c = board.get_button_info_list()
        board.config_enter_cmd(self.enter_command)
        for tuple in c:
            action = self.create_button_action(tuple[0],
                                               tuple[1], tuple[2], tuple[3],
                                               self.__board)
            board.set_button_command(tuple[0], action, [])
        global TIME_LEFT
        TIME_LEFT = 180
        self.start_time()
        board.run()

    def run(self):
        self.__root.mainloop()


if __name__ == "__main__":
    a = tk.Tk()
    b = Start_button(a)
    b.run()
