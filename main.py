import random
import os
from colorama import Fore
import time
TTT_board = ["_","_","_","_","_","_","_","_","_"]

def clear_screen(): #works on Windows, Mac, and Linux
  os.system('cls' if os.name == 'nt' else 'clear')

___ = """
        |         |
        |         | 
        |         |
        |         |
"""
__o = """
        |         |  ----- 
        |         | |     |
        |         | |     |
        |         |  ----- 
"""
__x = """
        |         |  \  /  
        |         |   \\    
        |         |   /\\   
        |         |  /  \\  
"""
_o_ = """
        |  -----  |
        | |     | |
        | |     | |
        |  -----  |
"""
_oo = """
        |  -----  |  -----
        | |     | | |     |
        | |     | | |     |
        |  -----  |  -----
"""
_ox = """
        |  -----  |  \  /  
        | |     | |   \\    
        | |     | |   /\\   
        |  -----  |  /  \\  
"""
_x_ = """
        |   \  /  |
        |    \\    |
        |    /\\   |
        |   /  \\  |
"""
_xo = """
        |   \  /  |  -----  
        |    \\    | |     | 
        |    /\\   | |     | 
        |   /  \\  |  -----  
"""
_xx = """
        |   \  /  |  \  /  
        |    \\    |   \\    
        |    /\\   |   /\\   
        |   /  \\  |  /  \\  
"""
o__ = """
 -----  |         |
|     | |         |
|     | |         |
 -----  |         |
"""
o_o = """
 -----  |         |  -----  
|     | |         | |     | 
|     | |         | |     | 
 -----  |         |  -----  
"""
o_x = """
 -----  |         |  \  /
|     | |         |   \\   
|     | |         |   /\\   
 -----  |         |  /  \\  
"""
oo_ = """
 -----  |  -----  |
|     | | |     | |
|     | | |     | |
 -----  |  -----  |
"""
ooo = """
 -----  |  -----  |  -----
|     | | |     | | |     |
|     | | |     | | |     |
 -----  |  -----  |  -----
"""
oox = """
 -----  |  -----  |  \  /  
|     | | |     | |   \\    
|     | | |     | |   /\\   
 -----  |  -----  |  /  \\  
"""
ox_ = """
 -----  |   \  /  |
|     | |    \\    | 
|     | |    /\\   |
 -----  |   /  \\  |
"""
oxo = """
 -----  |   \  /  |  -----  
|     | |    \\    | |     | 
|     | |    /\\   | |     |   
 -----  |   /  \\  |  -----   
"""
oxx ="""
 -----  |   \  /  |  \  /   
|     | |    \\    |   \\     
|     | |    /\\   |   /\\    
 -----  |   /  \\  |  /  \\   
"""
x__ = """
  \  /  |         | 
   \\    |         | 
   /\\   |         | 
  /  \\  |         | 
"""
x_o = """
  \  /  |         |  -----  
   \\    |         | |     | 
   /\\   |         | |     | 
  /  \\  |         |  -----  
"""
x_x = """
  \  /  |         |  \  /
   \\    |         |   \\
   /\\   |         |   /\\
  /  \\  |         |  /  \\
"""
xo_ = """
  \  /  |  -----  | 
   \\    | |     | | 
   /\\   | |     | | 
  /  \\  |  -----  |
"""
xoo = """
  \  /  |  -----  |  -----  
   \\    | |     | | |     | 
   /\\   | |     | | |     |  
  /  \\  |  -----  |  -----  
"""
xox = """
  \  /  |  -----  |  \  /
   \\    | |     | |   \\
   /\\   | |     | |   /\\
  /  \\  |  -----  |  /  \\
"""
xx_ = """
  \  /  |   \  /  |
   \\    |    \\    | 
   /\\   |    /\\   | 
  /  \\  |   /  \\  |  
"""
xxo = """
  \  /  |   \  /  |  -----  
   \\    |    \\    | |     | 
   /\\   |    /\\   | |     | 
  /  \\  |   /  \\  |  -----  
"""
xxx = """
  \  /  |   \  /  |  \  /
   \\    |    \\    |   \\
   /\\   |    /\\   |   /\\
  /  \\  |   /  \\  |  /  \\
"""
horiz = "----------------------------"

def board_refresh():
  clear_screen()
  row1 = TTT_board[0] + TTT_board[1] + TTT_board[2]
  row2 = TTT_board[3] + TTT_board[4] + TTT_board[5]
  row3 = TTT_board[6] + TTT_board[7] + TTT_board[8]
  print(eval(row1) + horiz + eval(row2) + horiz + eval(row3))
def player_move():
  board_refresh()
  print("Enter the corresponding index of the desired square.")
  print("Enter HELP to view the indexes of the squares.")
  choice = input("")
  if choice.lower() == "help":
    clear_screen()
    print("""
  /|    |  /  \   |  /  \\
   |    |     /   |  ___/
   |    |    /    |     \\
   |    |  /___   |  ___/ 
----------------------------
 |   |  |  ----   | /  \\
 |___|  | |____   | |___
     |  |      |  | |   \\
     |  |  ____|  | \\___/
----------------------------
  ----  | /    \\  | /   \\
     /  | \\____/  | \\___|  
    /   | /    \\  |     |
   /    | \\____/  |     |  
    """)
    print("press <ENTER> to exit.")
    input("")
    player_move()
  elif choice == "1" or choice == "2" or choice == "3" \
  or choice == "4" or choice == "5" or choice == "6" \
  or choice == "7" or choice == "8" or choice == "9":
    if TTT_board[int(choice)-1] == "_":
      TTT_board[int(choice)-1] = "x"
      win_check(opponent_move)
    else:
      print("You cannot move here.")
      time.sleep(.75)
      player_move()
  else:
    print("<ERROR>")
    time.sleep(1)
    player_move()
def opponent_move():
  clear_screen()
  board_refresh()
  time.sleep(1)
  opponent_move = False
  while opponent_move == False:
    num = random.randint(0,8)
    if TTT_board[num] == "_":
      TTT_board[num] = "o"
      opponent_move = True
      win_check(player_move)
def restart_game():
  print("Do you want to play again?")
  print("y/n")
  again = input("")
  if again == "n":
    exit()
  else:
    global TTT_board
    TTT_board = ["_","_","_","_","_","_","_","_","_"]
    board_refresh()
    player_move()
def win_check(next_move):
  if TTT_board[0] == "x" and TTT_board[1] == "x" and TTT_board[2] == "x" or \
  TTT_board[3] == "x" and TTT_board[4] == "x" and TTT_board[5] == "x" or \
  TTT_board[0] == "x" and TTT_board[4] == "x" and TTT_board[8] == "x" or \
  TTT_board[2] == "x" and TTT_board[5] == "x" and TTT_board[8] == "x" or \
  TTT_board[1] == "x" and TTT_board[4] == "x" and TTT_board[7] == "x" or \
  TTT_board[0] == "x" and TTT_board[3] == "x" and TTT_board[6] == "x" or \
  TTT_board[6] == "x" and TTT_board[7] == "x" and TTT_board[8] == "x" or \
  TTT_board[2] == "x" and TTT_board[4] == "x" and TTT_board[6] == "x":
    clear_screen()
    board_refresh()
    print("You Win!")
    restart_game()
  elif TTT_board[0] == "o" and TTT_board[1] == "o" and TTT_board[2] == "o" or \
  TTT_board[3] == "o" and TTT_board[4] == "o" and TTT_board[5] == "o" or \
  TTT_board[0] == "o" and TTT_board[4] == "o" and TTT_board[8] == "o" or \
  TTT_board[2] == "o" and TTT_board[5] == "o" and TTT_board[8] == "o" or \
  TTT_board[1] == "o" and TTT_board[4] == "o" and TTT_board[7] == "o" or \
  TTT_board[0] == "o" and TTT_board[3] == "o" and TTT_board[6] == "o" or \
  TTT_board[6] == "o" and TTT_board[7] == "o" and TTT_board[8] == "o" or \
  TTT_board[2] == "o" and TTT_board[4] == "o" and TTT_board[6] == "o":
    clear_screen()
    board_refresh()
    print("You lose.")
    restart_game()
  elif "_" not in TTT_board:
    clear_screen()
    board_refresh()
    print("It's a tie!")
    restart_game()
  next_move()  
player_move()
