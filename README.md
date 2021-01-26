# my_sudoku

Simply run the 'sudoku_class.py' on an IDE and the game will pop-up.

The game's feel should be easy to grasp without much explanation, each button is named in such a way that you will understand how everything works.

There is a feature which doesn't fully work in the game, which is the sudoku_solver that is run through the "SOLVE" button.
The method is deleted from the sudoku_class.py file and uploaded in a seperate .py file under the name of 'sudoku_solver.py'.
You can examin the file to understand how it works, but currently is only able to solve easy/medium games. There are some more game logic which
  needs to be implemented into the algorithm, which will soon be available.
  
The 'sudoku_db.splite' is a SQLite file which holds the sudoku games in the next format (1:PRIMARY KEY _ID, 2:TEXT NOT NULL SUDOKU_STRING).
  There are 4 tables under the name of 's_easy', 's_medium', 's_hard' and 's_expert'. The total number of sudoku games are 12 at the moment.
