from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pg

def possible(x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and i != y: 
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: 
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  
            if grid[Y][X] == n:
                return False    
    return True

def Print(matrix):
    for i in range(9):
        print(matrix[i])
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)

driver = webdriver.Firefox()
url = "https://four.websudoku.com/?level=4"
driver.get(url)
grid = []
row08 = ""

def calc(xin):
    row = ""
    for i in range(9):
        value = driver.find_element(By.ID, f"f{xin}").get_attribute("value")
        if value == "":
            row += "0"
        else:
            row += value
        xin = str(int(xin) + 10)
    return row

def insertList(inta):
    ints = []
    for i in inta:
        ints.append(int(i))
    grid.append(ints)



insertList(calc("00"))
insertList(calc("01"))
insertList(calc("02"))
insertList(calc("03"))
insertList(calc("04"))
insertList(calc("05"))
insertList(calc("06"))
insertList(calc("07"))
insertList(calc("08"))

print("AutoPlay in 5sec")
time.sleep(5)
solve()
pg.hotkey("Enter")
