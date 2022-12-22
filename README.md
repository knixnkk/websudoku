# Sudoku Solver
This script uses the Selenium and PyAutoGUI libraries to solve a Sudoku puzzle on the website https://four.websudoku.com/

# Requirements
  Python 3
  Selenium
  PyAutoGUI
  
# To install the required libraries, run the following command:
- pip install selenium pyautogui

# Usage
- 1. Open the file in a text editor and set the path to your Firefox driver executable in the following line:
-         `driver = webdriver.Firefox(executable_path="path/to/geckodriver")`
- 2. Run the script:
-         `python sudoku_solver.py`

The script will open the website in a Firefox browser and solve the Sudoku puzzle. The solution will then be entered in the input fields on the website and the form will be submitted.

# Code Explanation

The `possible()` function checks if a given number `n` can be placed at the given coordinates `x`, `y` in the Sudoku grid.

The `Print()` function converts the solution matrix into a flat list of strings and uses PyAutoGUI to enter the values in the input fields on the website.

The `solve()` function uses a recursive approach to solve the Sudoku puzzle. It tries all possible numbers for each empty cell and backtracks when a contradiction is found. When the puzzle is solved, the solution is printed and the form is submitted.

The `calc()` function uses Selenium to extract the values from the input fields on the website and stores them in a string.

The `insertList()` function converts the string of values into a list of integers and appends it to the `grid` list.

Finally, `the solve()` function is called to solve the puzzle and the solution is entered on the website.
