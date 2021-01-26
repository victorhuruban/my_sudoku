import sqlite3
import tkinter
from tkinter.font import Font
from tkinter import ttk

class Sudoku(object):

    holder = []

    game_state = False

    def __init__(self):
        
        ### MAIN FRAME ###
        self.main_window = tkinter.Tk()
        self.main_window.title("Sudoku")
        self.main_window.geometry("800x600")
        self.main_window.configure(bg="#E4E4E4")

        ### SUDOKU GRID FRAME ###
        sudoku_frame = tkinter.Frame(self.main_window, bg="#E4E4E4", highlightbackground="black", highlightthickness=2, relief="sunken")
        sudoku_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            padx=20,
            pady=20
            )

        ### FRAME FOR EACH 9x9 MATRIX FOR THE BORDER IN BETWEEN ###
        sudoku_test_frame_0_0 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_0_3 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_0_6 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")

        sudoku_test_frame_3_0 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_3_3 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_3_6 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")

        sudoku_test_frame_6_0 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_6_3 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")
        sudoku_test_frame_6_6 = tkinter.Frame(sudoku_frame, bg="#E4E4E4", highlightbackground="black", highlightthickness=1, relief="sunken")

        sudoku_test_frame_0_0.grid(row=0, column=0)
        sudoku_test_frame_0_3.grid(row=0, column=1)
        sudoku_test_frame_0_6.grid(row=0, column=2)

        sudoku_test_frame_3_0.grid(row=1, column=0)
        sudoku_test_frame_3_3.grid(row=1, column=1)
        sudoku_test_frame_3_6.grid(row=1, column=2)

        sudoku_test_frame_6_0.grid(row=2, column=0)
        sudoku_test_frame_6_3.grid(row=2, column=1)
        sudoku_test_frame_6_6.grid(row=2, column=2)

        for col in range(0,3):
            for row in range(0,3):
                sudoku_frame.rowconfigure(row, weight=1)
            sudoku_frame.columnconfigure(col, weight=1)

        for col in range(0,3):
            for row in range(0,3):
                sudoku_test_frame_0_0.rowconfigure(row, weight=1)
                sudoku_test_frame_0_3.rowconfigure(row, weight=1)
                sudoku_test_frame_0_6.rowconfigure(row, weight=1)
                sudoku_test_frame_3_0.rowconfigure(row, weight=1)
                sudoku_test_frame_3_3.rowconfigure(row, weight=1)
                sudoku_test_frame_3_6.rowconfigure(row, weight=1)
                sudoku_test_frame_6_0.rowconfigure(row, weight=1)
                sudoku_test_frame_6_3.rowconfigure(row, weight=1)
                sudoku_test_frame_6_6.rowconfigure(row, weight=1)
            sudoku_test_frame_0_0.columnconfigure(col, weight=1)
            sudoku_test_frame_0_3.columnconfigure(col, weight=1)
            sudoku_test_frame_0_6.columnconfigure(col, weight=1)
            sudoku_test_frame_3_0.columnconfigure(col, weight=1)
            sudoku_test_frame_3_3.columnconfigure(col, weight=1)
            sudoku_test_frame_3_6.columnconfigure(col, weight=1)
            sudoku_test_frame_6_0.columnconfigure(col, weight=1)
            sudoku_test_frame_6_3.columnconfigure(col, weight=1)
            sudoku_test_frame_6_6.columnconfigure(col, weight=1)

        ### THE SUDOKU GAME HOLDER ###
        self.sudoku_sample = []
            
        db = sqlite3.connect("sudoku_db.sqlite")
        cursor = db.cursor().execute("SELECT * FROM s_easy ORDER BY RANDOM() LIMIT 1")
        gen_sudoku = []
        for _, s_game in cursor:
            self.sudoku_sample = self.sudoku_loader(s_game)
        cursor.close()
        db.close()

        ### FONT FOR THE VALUES IN THE SUDOKU FRAMES / BUTTON ###
        font_test = Font(family="Times New Roman", size=20, weight="bold")

        ### INITIALIZATION OF THE BUTTONS VALUES WHEN THE GAME IS STARTED ###
        self.pos_0_0 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[0][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 0", self.pos_0_0))
        self.pos_0_0.grid(row=0, column=0, sticky="news")
        self.pos_0_1 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[0][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 1", self.pos_0_1))
        self.pos_0_1.grid(row=0, column=1, sticky="news")
        self.pos_0_2 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[0][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 2", self.pos_0_2))
        self.pos_0_2.grid(row=0, column=2, sticky="news")
        self.pos_0_3 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[0][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 3", self.pos_0_3))
        self.pos_0_3.grid(row=0, column=0, sticky="news")
        self.pos_0_4 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[0][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 4", self.pos_0_4))
        self.pos_0_4.grid(row=0, column=1, sticky="news")
        self.pos_0_5 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[0][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 5", self.pos_0_5))
        self.pos_0_5.grid(row=0, column=2, sticky="news")
        self.pos_0_6 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[0][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 6", self.pos_0_6))
        self.pos_0_6.grid(row=0, column=0, sticky="news")
        self.pos_0_7 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[0][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 7", self.pos_0_7))
        self.pos_0_7.grid(row=0, column=1, sticky="news")
        self.pos_0_8 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[0][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("0 8", self.pos_0_8))
        self.pos_0_8.grid(row=0, column=2, sticky="news")
            
        self.pos_1_0 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[1][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 0", self.pos_1_0))
        self.pos_1_0.grid(row=1, column=0, sticky="news")
        self.pos_1_1 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[1][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 1", self.pos_1_1))
        self.pos_1_1.grid(row=1, column=1, sticky="news")
        self.pos_1_2 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[1][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 2", self.pos_1_2))
        self.pos_1_2.grid(row=1, column=2, sticky="news")
        self.pos_1_3 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[1][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 3", self.pos_1_3))
        self.pos_1_3.grid(row=1, column=0, sticky="news")
        self.pos_1_4 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[1][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 4", self.pos_1_4))
        self.pos_1_4.grid(row=1, column=1, sticky="news")
        self.pos_1_5 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[1][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 5", self.pos_1_5))
        self.pos_1_5.grid(row=1, column=2, sticky="news")
        self.pos_1_6 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[1][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 6", self.pos_1_6))
        self.pos_1_6.grid(row=1, column=0, sticky="news")
        self.pos_1_7 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[1][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 7", self.pos_1_7))
        self.pos_1_7.grid(row=1, column=1, sticky="news")
        self.pos_1_8 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[1][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("1 8", self.pos_1_8))
        self.pos_1_8.grid(row=1, column=2, sticky="news")

        self.pos_2_0 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[2][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 0", self.pos_2_0))
        self.pos_2_0.grid(row=2, column=0, sticky="news")
        self.pos_2_1 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[2][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 1", self.pos_2_1))
        self.pos_2_1.grid(row=2, column=1, sticky="news")
        self.pos_2_2 = tkinter.Button(sudoku_test_frame_0_0, text=self.displayButton(self.sudoku_sample[2][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 2", self.pos_2_2))
        self.pos_2_2.grid(row=2, column=2, sticky="news")
        self.pos_2_3 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[2][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 3", self.pos_2_3))
        self.pos_2_3.grid(row=2, column=0, sticky="news")
        self.pos_2_4 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[2][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 4", self.pos_2_4))
        self.pos_2_4.grid(row=2, column=1, sticky="news")
        self.pos_2_5 = tkinter.Button(sudoku_test_frame_0_3, text=self.displayButton(self.sudoku_sample[2][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 5", self.pos_2_5))
        self.pos_2_5.grid(row=2, column=2, sticky="news")
        self.pos_2_6 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[2][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 6", self.pos_2_6))
        self.pos_2_6.grid(row=2, column=0, sticky="news")
        self.pos_2_7 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[2][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 7", self.pos_2_7))
        self.pos_2_7.grid(row=2, column=1, sticky="news")
        self.pos_2_8 = tkinter.Button(sudoku_test_frame_0_6, text=self.displayButton(self.sudoku_sample[2][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("2 8", self.pos_2_8))
        self.pos_2_8.grid(row=2, column=2, sticky="news")

        self.pos_3_0 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[3][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 0", self.pos_3_0))
        self.pos_3_0.grid(row=0, column=0, sticky="news")
        self.pos_3_1 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[3][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 1", self.pos_3_1))
        self.pos_3_1.grid(row=0, column=1, sticky="news")
        self.pos_3_2 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[3][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 2", self.pos_3_2))
        self.pos_3_2.grid(row=0, column=2, sticky="news")
        self.pos_3_3 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[3][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 3", self.pos_3_3))
        self.pos_3_3.grid(row=0, column=0, sticky="news")
        self.pos_3_4 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[3][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 4", self.pos_3_4))
        self.pos_3_4.grid(row=0, column=1, sticky="news")
        self.pos_3_5 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[3][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 5", self.pos_3_5))
        self.pos_3_5.grid(row=0, column=2, sticky="news")
        self.pos_3_6 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[3][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 6", self.pos_3_6))
        self.pos_3_6.grid(row=0, column=0, sticky="news")
        self.pos_3_7 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[3][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 7", self.pos_3_7))
        self.pos_3_7.grid(row=0, column=1, sticky="news")
        self.pos_3_8 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[3][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("3 8", self.pos_3_8))
        self.pos_3_8.grid(row=0, column=2, sticky="news")

        self.pos_4_0 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[4][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 0", self.pos_4_0))
        self.pos_4_0.grid(row=1, column=0, sticky="news")
        self.pos_4_1 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[4][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 1", self.pos_4_1))
        self.pos_4_1.grid(row=1, column=1, sticky="news")
        self.pos_4_2 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[4][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 2", self.pos_4_2))
        self.pos_4_2.grid(row=1, column=2, sticky="news")
        self.pos_4_3 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[4][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 3", self.pos_4_3))
        self.pos_4_3.grid(row=1, column=0, sticky="news")
        self.pos_4_4 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[4][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 4", self.pos_4_4))
        self.pos_4_4.grid(row=1, column=1, sticky="news")
        self.pos_4_5 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[4][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 5", self.pos_4_5))
        self.pos_4_5.grid(row=1, column=2, sticky="news")
        self.pos_4_6 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[4][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 6", self.pos_4_6))
        self.pos_4_6.grid(row=1, column=0, sticky="news")
        self.pos_4_7 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[4][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 7", self.pos_4_7))
        self.pos_4_7.grid(row=1, column=1, sticky="news")
        self.pos_4_8 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[4][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("4 8", self.pos_4_8))
        self.pos_4_8.grid(row=1, column=2, sticky="news")

        self.pos_5_0 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[5][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 0", self.pos_5_0))
        self.pos_5_0.grid(row=2, column=0, sticky="news")
        self.pos_5_1 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[5][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 1", self.pos_5_1))
        self.pos_5_1.grid(row=2, column=1, sticky="news")
        self.pos_5_2 = tkinter.Button(sudoku_test_frame_3_0, text=self.displayButton(self.sudoku_sample[5][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 2", self.pos_5_2))
        self.pos_5_2.grid(row=2, column=2, sticky="news")
        self.pos_5_3 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[5][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 3", self.pos_5_3))
        self.pos_5_3.grid(row=2, column=0, sticky="news")
        self.pos_5_4 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[5][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 4", self.pos_5_4))
        self.pos_5_4.grid(row=2, column=1, sticky="news")
        self.pos_5_5 = tkinter.Button(sudoku_test_frame_3_3, text=self.displayButton(self.sudoku_sample[5][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 5", self.pos_5_5))
        self.pos_5_5.grid(row=2, column=2, sticky="news")
        self.pos_5_6 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[5][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 6", self.pos_5_6))
        self.pos_5_6.grid(row=2, column=0, sticky="news")
        self.pos_5_7 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[5][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 7", self.pos_5_7))
        self.pos_5_7.grid(row=2, column=1, sticky="news")
        self.pos_5_8 = tkinter.Button(sudoku_test_frame_3_6, text=self.displayButton(self.sudoku_sample[5][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("5 8", self.pos_5_8))
        self.pos_5_8.grid(row=2, column=2, sticky="news")

        self.pos_6_0 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[6][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 0", self.pos_6_0))
        self.pos_6_0.grid(row=0, column=0, sticky="news")
        self.pos_6_1 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[6][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 1", self.pos_6_1))
        self.pos_6_1.grid(row=0, column=1, sticky="news")
        self.pos_6_2 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[6][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 2", self.pos_6_2))
        self.pos_6_2.grid(row=0, column=2, sticky="news")
        self.pos_6_3 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[6][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 3", self.pos_6_3))
        self.pos_6_3.grid(row=0, column=0, sticky="news")
        self.pos_6_4 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[6][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 4", self.pos_6_4))
        self.pos_6_4.grid(row=0, column=1, sticky="news")
        self.pos_6_5 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[6][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 5", self.pos_6_5))
        self.pos_6_5.grid(row=0, column=2, sticky="news")
        self.pos_6_6 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[6][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 6", self.pos_6_6))
        self.pos_6_6.grid(row=0, column=0, sticky="news")
        self.pos_6_7 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[6][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 7", self.pos_6_7))
        self.pos_6_7.grid(row=0, column=1, sticky="news")
        self.pos_6_8 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[6][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("6 8", self.pos_6_8))
        self.pos_6_8.grid(row=0, column=2, sticky="news")

        self.pos_7_0 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[7][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 0", self.pos_7_0))
        self.pos_7_0.grid(row=1, column=0, sticky="news")
        self.pos_7_1 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[7][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 1", self.pos_7_1))
        self.pos_7_1.grid(row=1, column=1, sticky="news")
        self.pos_7_2 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[7][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 2", self.pos_7_2))
        self.pos_7_2.grid(row=1, column=2, sticky="news")
        self.pos_7_3 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[7][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 3", self.pos_7_3))
        self.pos_7_3.grid(row=1, column=0, sticky="news")
        self.pos_7_4 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[7][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 4", self.pos_7_4))
        self.pos_7_4.grid(row=1, column=1, sticky="news")
        self.pos_7_5 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[7][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 5", self.pos_7_5))
        self.pos_7_5.grid(row=1, column=2, sticky="news")
        self.pos_7_6 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[7][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 6", self.pos_7_6))
        self.pos_7_6.grid(row=1, column=0, sticky="news")
        self.pos_7_7 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[7][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 7", self.pos_7_7))
        self.pos_7_7.grid(row=1, column=1, sticky="news")
        self.pos_7_8 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[7][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("7 8", self.pos_7_8))
        self.pos_7_8.grid(row=1, column=2, sticky="news")

        self.pos_8_0 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[8][0]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 0", self.pos_8_0))
        self.pos_8_0.grid(row=2, column=0, sticky="news")
        self.pos_8_1 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[8][1]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 1", self.pos_8_1))
        self.pos_8_1.grid(row=2, column=1, sticky="news")
        self.pos_8_2 = tkinter.Button(sudoku_test_frame_6_0, text=self.displayButton(self.sudoku_sample[8][2]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 2", self.pos_8_2))
        self.pos_8_2.grid(row=2, column=2, sticky="news")
        self.pos_8_3 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[8][3]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 3", self.pos_8_3))
        self.pos_8_3.grid(row=2, column=0, sticky="news")
        self.pos_8_4 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[8][4]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 4", self.pos_8_4))
        self.pos_8_4.grid(row=2, column=1, sticky="news")
        self.pos_8_5 = tkinter.Button(sudoku_test_frame_6_3, text=self.displayButton(self.sudoku_sample[8][5]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 5", self.pos_8_5))
        self.pos_8_5.grid(row=2, column=2, sticky="news")
        self.pos_8_6 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[8][6]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 6", self.pos_8_6))
        self.pos_8_6.grid(row=2, column=0, sticky="news")
        self.pos_8_7 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[8][7]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 7", self.pos_8_7))
        self.pos_8_7.grid(row=2, column=1, sticky="news")
        self.pos_8_8 = tkinter.Button(sudoku_test_frame_6_6, text=self.displayButton(self.sudoku_sample[8][8]), width=3, height=1, bg='white', font=font_test, command=lambda: self.onClickSudoku("8 8", self.pos_8_8))
        self.pos_8_8.grid(row=2, column=2, sticky="news")

        ### GENERATOR FRAME ###
        generate_frame = tkinter.Frame(self.main_window, bg="#E4E4E4")
        generate_frame.grid(
            row=3,
            column=0,
            ipady=50,
            pady=0,
            sticky="n"
            )
        
        # GENERATE FRAME / BUTTON    
        option_list = [
            "easy",
            "medium",
            "hard",
            "expert"
            ]

        self.variable = tkinter.StringVar(self.main_window)
        self.variable.set(option_list[0])
        
        generate_button = tkinter.Button(generate_frame, text="           GENERATE           ", command=lambda: [self.popUp()])
        generate_button.grid(
            row=0,
            column=0
            )

        # GENERATE FRAME / DROPDOWN
        dropdown_list = tkinter.OptionMenu(generate_frame, self.variable, *option_list)
        dropdown_list.config(width=6)
        dropdown_list.grid(
            row=0,
            column=1,
            )

        ### KEYPAD FRAME ###
        keypad_frame = tkinter.Frame(self.main_window, bg="#E4E4E4")
        keypad_frame.grid(
            row=0,
            column=1,
            rowspan=2,
            ipadx=10,
            padx=52,
            pady=50,
            sticky="nw"
            )

        # GENERATE KEYPAD AND LABEL BELOW TO KEEP TRACK OF WHAT IS SELECTED
        for col in range(0,3):
            for row in range(0,4):
                keypad_frame.rowconfigure(row, weight=1)
            keypad_frame.columnconfigure(col, weight=1)
        keypad_frame.rowconfigure(4, weight=2)

        one_button = tkinter.Button(keypad_frame, text="1", width=3, height=2, command=lambda: self.onClickKeypadNums("1")).grid(row=2, column=0, sticky="news")
        two_button = tkinter.Button(keypad_frame, text="2", width=3, height=2, command=lambda: self.onClickKeypadNums("2")).grid(row=2, column=1, sticky="news")
        three_button = tkinter.Button(keypad_frame, text="3", width=3, height=2, command=lambda: self.onClickKeypadNums("3")).grid(row=2, column=2, sticky="news")
        four_button = tkinter.Button(keypad_frame, text="4", width=3, height=2, command=lambda: self.onClickKeypadNums("4")).grid(row=1, column=0, sticky="news")
        five_button = tkinter.Button(keypad_frame, text="5", width=3, height=2, command=lambda: self.onClickKeypadNums("5")).grid(row=1, column=1, sticky="news")
        six_button = tkinter.Button(keypad_frame, text="6", width=3, height=2, command=lambda: self.onClickKeypadNums("6")).grid(row=1, column=2, sticky="news")
        seven_button = tkinter.Button(keypad_frame, text="7", width=3, height=2, command=lambda: self.onClickKeypadNums("7")).grid(row=0, column=0, sticky="news")
        eight_button = tkinter.Button(keypad_frame, text="8", width=3, height=2, command=lambda: self.onClickKeypadNums("8")).grid(row=0, column=1, sticky="news")
        nine_button = tkinter.Button(keypad_frame, text="9", width=3, height=2, command=lambda: self.onClickKeypadNums("9")).grid(row=0, column=2, sticky="news")
        del_button = tkinter.Button(keypad_frame, text="DELETE", command=lambda: self.onClickKeypadDelete("Delete")).grid(row=3, column=0, columnspan=3, sticky="news")
        self.holder_label = tkinter.Label(keypad_frame, text="Nothing yet", relief="groove")
        self.holder_label.grid(row=4, column=0, columnspan=3, sticky="ews", pady=25)

        ### SOLVE / CHECK BUTTONS ###
        cs_frame = tkinter.Frame(self.main_window, bg="#E4E4E4")
        cs_frame.grid(
            row=2,
            column=1,
            sticky="nw",
            padx=62,
            )
           
        solve_button = tkinter.Button(cs_frame, text="SOLVE", command=lambda: self.solveGame()).grid(
            row=0,
            column=0
            )
        check_button = tkinter.Button(cs_frame, text="CHECK", command=lambda: self.checkGame()).grid(
            row=0,
            column=1
            )

        ### CANVAS FOR DISPLAYING IF SUDOKU GAME IS SOLVED CORRECTLY OR INCORRECTLY ###
        self.canvas_frame = tkinter.Frame(self.main_window)
        self.canvas_frame.grid(
            row=2,
            column=1,
            rowspan=2
            )

        self.c_canvas = tkinter.Canvas(self.canvas_frame, bg="#E4E4E4", relief="raised")
        self.oval = self.c_canvas.create_oval(60,30,160,130, fill="green")
        self.c_canvas.grid(
            row=0,
            column=0,
            )
        
        self.main_window.mainloop()

    ### METHOD THAT CONTROLS THE BEHAVIOUR OF BUTTONS FROM THE SUDOKU FRAME ###
    def onClickSudoku(self, text, btn):
        if btn['text'] == "" or btn['bg'] == '#E4E4E4': # IF THE BUTTON IS NOT BLANK, YOU ARE ABLE TO INTERACT WITH IT/ IF NOT, YOU CANNOT MODIFY THE SELECTED BUTTON #
            print(btn['text'])
            split_l = text.split(" ")
            val = self.sudoku_sample[int(split_l[0])][int(split_l[1])]
            self.holder_label['text'] = "{} : pos {}|{}".format(val, int(split_l[0]) + 1, int(split_l[1]) + 1)
            if not self.holder: # IF YOU HAVEN'T SELECTED ANY BUTTON #
                self.holder.append(val)
                self.holder.append(int(split_l[0]))
                self.holder.append(int(split_l[1]))
                btn['bg'] = "#E4E4E4"
                btn['relief'] = "sunken"
                self.holder.append(btn)
            else: # IF YOU HAVE SELECTED A BUTTON #
                self.holder[3]['bg'] = "white"
                self.holder[3]['relief'] = "raised"
                self.holder.clear()
                self.holder.append(val)
                self.holder.append(int(split_l[0]))
                self.holder.append(int(split_l[1]))
                btn['bg'] = "#E4E4E4"
                btn['relief'] = "sunken"
                self.holder.append(btn)
        

    ### METHOD THAT CONTROLS THE BEHAVIOUR OF THE KEYPAD BUTTONS ###
    def onClickKeypadNums(self, text):
        if self.holder:
            self.holder[3]['text'] = int(text)
            self.holder[3]['bg'] = "#E4E4E4"
            self.holder[3]['relief'] = "raised"
            self.sudoku_sample[self.holder[1]][self.holder[2]] = int(text)
            self.holder.clear()
            self.holder_label['text'] = ""

    ### METHOD THAT CONTROLS THE BEHAVIOUR OF THE DELETE BUTTON FROM THE KEYPAD FRAME ###
    def onClickKeypadDelete(self, text):
        if self.holder:
            self.holder[3]['text'] = ""
            self.holder[3]['bg'] = "white"
            self.holder[3]['relief'] = "raised"
            self.sudoku_sample[self.holder[1]][self.holder[2]] = 0
            self.holder.clear()
            self.holder_label['text'] = ""

    ### METHOD THAT WILL CONTROL THE KEYBOARD INPUTS (WILL SOON BE UPDATED) ###
    def keyboardInput(self):
        args = event

    ### METHOD THAT TRIES TO SOLVE THE CURRENT GAME (IS ONLY WORKING FOR EASY AND MEDIUM DIFFICULTY GAMES, WILL SOON BE UPDATED) ###
    def solveGame(self):
        print("Try solve")

    ### METHOD THAT CHECKS THE CURRENT GAME STATE (CHECKS IF THE GAME IS CORRECTLY FILLED OR NOT) ###
        # if the game is solved correctly, the canvas is filled with the color 'blue'
        # if the game is solved incorrectly, the canvas is filled with the color 'red'
    def sudoku_checker(self, arr):
        # CHECK ROWS
        for row in range(0, 9):
            s_row = set(arr[row])
            if len(s_row) != 9: return False
            
            # CHECK COLUMN
            s_column = set()
            for column in range(0, 9):
                s_column.add(arr[column][row])
            if len(s_column) != 9: return False

        # CHECKS EACH INDIVIDUAL MATRIX
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                check_set = set()
                for s_row in range(0, 3):
                    for s_column in range(0, 3):
                        check_set.add(arr[row + s_row][column + s_column])
                if len(check_set) != 9: return False
        return True

    ### THE METHOD THAT ACTUALLY CHANGES THE CANVAS COLOR BASED ON THE 'sudoku_checker' OUTPUT ###
    def checkGame(self):
        if self.sudoku_checker(self.sudoku_sample):
            self.oval = self.c_canvas.create_oval(60,30,160,130, fill="blue")
            self.game_state = True
        else:
            self.oval = self.c_canvas.create_oval(60,30,160,130, fill="red")
            self.game_state = False

    ### METHOD THAT LOADS THE SUDOKU GAME INTO THE LIST WHICH HOLDS THE GAME ###
    def sudoku_loader(self, sudoku_strng):
        arr_ret = [[],[],[],[],[],[],[],[],[]]
        count = 0
        for row in range(0,9):
            for _ in range(0,9):
                arr_ret[row].append(sudoku_strng[count])
                count += 1

        return arr_ret

    ### METHOD THAT BRINGS BACK THE MAINFRAME AFTER IT WAS HIDDEN BY PRESSING THE 'GENERATE' BUTTON ###
    def bringBack(self):
        self.main_window.update()
        self.main_window.deiconify()

    ### THE WINDOW THAT POPS UP AFTER PRESSING THE 'GENERATE' BUTTON ###
    def popUp(self):
        if not self.game_state:
            win = tkinter.Toplevel()
            win.wm_title("window")
            self.main_window.withdraw()

            l = tkinter.Label(win, text="Are you sure you want to generate new game?")
            l.grid(row=0, column=0)

            yes = ttk.Button(win, text="Yes", command=lambda: [win.destroy(), self.bringBack(), self.generateSudoku(self.variable.get())])
            yes.grid(row=1, column=0, sticky="w")

            no = ttk.Button(win, text="No", command=lambda: [win.destroy(), self.bringBack()])
            no.grid(row=1, column=0, sticky="e")

    ### METHOD THAT IS FILLING THE BUTTONS ON THE WINDOW ###
    def generateSudoku(self, variable):
        db = sqlite3.connect("sudoku_db.sqlite")
        cursor = db.cursor().execute("SELECT * FROM s_{} ORDER BY RANDOM() LIMIT 1".format(variable))
        gen_sudoku = []
        for _, s_game in cursor:
            gen_sudoku = self.sudoku_loader(s_game)
        self.sudoku_sample = gen_sudoku
        
        self.pos_0_0['text'] = self.displayButton(self.sudoku_sample[0][0])
        self.pos_0_1['text'] = self.displayButton(gen_sudoku[0][1])
        self.pos_0_2['text'] = self.displayButton(gen_sudoku[0][2])
        self.pos_0_3['text'] = self.displayButton(gen_sudoku[0][3])
        self.pos_0_4['text'] = self.displayButton(gen_sudoku[0][4])
        self.pos_0_5['text'] = self.displayButton(gen_sudoku[0][5])
        self.pos_0_6['text'] = self.displayButton(gen_sudoku[0][6])
        self.pos_0_7['text'] = self.displayButton(gen_sudoku[0][7])
        self.pos_0_8['text'] = self.displayButton(gen_sudoku[0][8])

        self.pos_1_0['text'] = self.displayButton(gen_sudoku[1][0])
        self.pos_1_1['text'] = self.displayButton(gen_sudoku[1][1])
        self.pos_1_2['text'] = self.displayButton(gen_sudoku[1][2])
        self.pos_1_3['text'] = self.displayButton(gen_sudoku[1][3])
        self.pos_1_4['text'] = self.displayButton(gen_sudoku[1][4])
        self.pos_1_5['text'] = self.displayButton(gen_sudoku[1][5])
        self.pos_1_6['text'] = self.displayButton(gen_sudoku[1][6])
        self.pos_1_7['text'] = self.displayButton(gen_sudoku[1][7])
        self.pos_1_8['text'] = self.displayButton(gen_sudoku[1][8])

        self.pos_2_0['text'] = self.displayButton(gen_sudoku[2][0])
        self.pos_2_1['text'] = self.displayButton(gen_sudoku[2][1])
        self.pos_2_2['text'] = self.displayButton(gen_sudoku[2][2])
        self.pos_2_3['text'] = self.displayButton(gen_sudoku[2][3])
        self.pos_2_4['text'] = self.displayButton(gen_sudoku[2][4])
        self.pos_2_5['text'] = self.displayButton(gen_sudoku[2][5])
        self.pos_2_6['text'] = self.displayButton(gen_sudoku[2][6])
        self.pos_2_7['text'] = self.displayButton(gen_sudoku[2][7])
        self.pos_2_8['text'] = self.displayButton(gen_sudoku[2][8])

        self.pos_3_0['text'] = self.displayButton(gen_sudoku[3][0])
        self.pos_3_1['text'] = self.displayButton(gen_sudoku[3][1])
        self.pos_3_2['text'] = self.displayButton(gen_sudoku[3][2])
        self.pos_3_3['text'] = self.displayButton(gen_sudoku[3][3])
        self.pos_3_4['text'] = self.displayButton(gen_sudoku[3][4])
        self.pos_3_5['text'] = self.displayButton(gen_sudoku[3][5])
        self.pos_3_6['text'] = self.displayButton(gen_sudoku[3][6])
        self.pos_3_7['text'] = self.displayButton(gen_sudoku[3][7])
        self.pos_3_8['text'] = self.displayButton(gen_sudoku[3][8])

        self.pos_4_0['text'] = self.displayButton(gen_sudoku[4][0])
        self.pos_4_1['text'] = self.displayButton(gen_sudoku[4][1])
        self.pos_4_2['text'] = self.displayButton(gen_sudoku[4][2])
        self.pos_4_3['text'] = self.displayButton(gen_sudoku[4][3])
        self.pos_4_4['text'] = self.displayButton(gen_sudoku[4][4])
        self.pos_4_5['text'] = self.displayButton(gen_sudoku[4][5])
        self.pos_4_6['text'] = self.displayButton(gen_sudoku[4][6])
        self.pos_4_7['text'] = self.displayButton(gen_sudoku[4][7])
        self.pos_4_8['text'] = self.displayButton(gen_sudoku[4][8])

        self.pos_5_0['text'] = self.displayButton(gen_sudoku[5][0])
        self.pos_5_1['text'] = self.displayButton(gen_sudoku[5][1])
        self.pos_5_2['text'] = self.displayButton(gen_sudoku[5][2])
        self.pos_5_3['text'] = self.displayButton(gen_sudoku[5][3])
        self.pos_5_4['text'] = self.displayButton(gen_sudoku[5][4])
        self.pos_5_5['text'] = self.displayButton(gen_sudoku[5][5])
        self.pos_5_6['text'] = self.displayButton(gen_sudoku[5][6])
        self.pos_5_7['text'] = self.displayButton(gen_sudoku[5][7])
        self.pos_5_8['text'] = self.displayButton(gen_sudoku[5][8])

        self.pos_6_0['text'] = self.displayButton(gen_sudoku[6][0])
        self.pos_6_1['text'] = self.displayButton(gen_sudoku[6][1])
        self.pos_6_2['text'] = self.displayButton(gen_sudoku[6][2])
        self.pos_6_3['text'] = self.displayButton(gen_sudoku[6][3])
        self.pos_6_4['text'] = self.displayButton(gen_sudoku[6][4])
        self.pos_6_5['text'] = self.displayButton(gen_sudoku[6][5])
        self.pos_6_6['text'] = self.displayButton(gen_sudoku[6][6])
        self.pos_6_7['text'] = self.displayButton(gen_sudoku[6][7])
        self.pos_6_8['text'] = self.displayButton(gen_sudoku[6][8])

        self.pos_7_0['text'] = self.displayButton(gen_sudoku[7][0])
        self.pos_7_1['text'] = self.displayButton(gen_sudoku[7][1])
        self.pos_7_2['text'] = self.displayButton(gen_sudoku[7][2])
        self.pos_7_3['text'] = self.displayButton(gen_sudoku[7][3])
        self.pos_7_4['text'] = self.displayButton(gen_sudoku[7][4])
        self.pos_7_5['text'] = self.displayButton(gen_sudoku[7][5])
        self.pos_7_6['text'] = self.displayButton(gen_sudoku[7][6])
        self.pos_7_7['text'] = self.displayButton(gen_sudoku[7][7])
        self.pos_7_8['text'] = self.displayButton(gen_sudoku[7][8])

        self.pos_8_0['text'] = self.displayButton(gen_sudoku[8][0])
        self.pos_8_1['text'] = self.displayButton(gen_sudoku[8][1])
        self.pos_8_2['text'] = self.displayButton(gen_sudoku[8][2])
        self.pos_8_3['text'] = self.displayButton(gen_sudoku[8][3])
        self.pos_8_4['text'] = self.displayButton(gen_sudoku[8][4])
        self.pos_8_5['text'] = self.displayButton(gen_sudoku[8][5])
        self.pos_8_6['text'] = self.displayButton(gen_sudoku[8][6])
        self.pos_8_7['text'] = self.displayButton(gen_sudoku[8][7])
        self.pos_8_8['text'] = self.displayButton(gen_sudoku[8][8])
        
        cursor.close()
        db.close()

    ### METHOD THAT IS CONVERTING THE NUMBER 0 TO A BLANK SPACE ###
    def displayButton(self, num):
        if int(num) == 0:
            return ""
        else:
            return str(num)
        
        

if __name__ == "__main__":
    game = Sudoku()
