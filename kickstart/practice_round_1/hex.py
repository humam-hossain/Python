# 7
# 1 # Case #1: Nobody wins
# . 
# 1 # Case #2: Blue wins
# B 
# 1 # Case #3: Red wins
# R 
# 2 # Case #4: Impossible
# BR
# BB
# 4 # Case #5: Blue wins
# BBBB
# BBB.
# RRR.
# RRRR
# 4 # Case #6: Impossible
# BBBB
# BBBB
# RRR.
# RRRR
# 6 # Case #7: Blue wins
# ......
# ..R...
# BBBBBB
# ..R.R.
# ..RR..
# ......

# Case #1: Nobody wins
# Case #2: Blue wins
# Case #3: Red wins
# Case #4: Impossible
# Case #5: Blue wins
# Case #6: Impossible
# Case #7: Blue wins

from termcolor import colored

def red(start, index, end, board_size):
  win = list()

  u_start = start

  # print(colored(start, "red"))
  for _ in range(board_size-2):
    temp = list()
    for e in u_start:
      i = e[0] + 1

      for k in range(-1,2):
        j = e[1] + k
        if [i,j] in index and [i,j] not in temp:
          temp.append([i,j])
    u_start = temp
    # print(colored(temp, "red"))
  # print(colored(f"start={start} index={index} end ={end} size={board_size}", "red"))

  for e in u_start:
    i = e[0] + 1

    for k in range(-1, 2):
      j = e[1] + k
      if [i,j] in end:
        win.append([i,j])
  print(colored(win, "red"))

  if len(win) > 1:
    return 2
  if len(win) == 0:
    return 0
  
  return 1

def blue(start, index, end, board_size):
  win = list()

  u_start = start

  print(colored(f"start={start} end={end}", "blue"))
  for _ in range(board_size-2):
    temp = list()
    for e in u_start:
      i = e[0] + 1

      for k in range(-1,2):
        j = e[1] + k
        if [i,j] in index and [i,j] not in temp:
          temp.append([i,j])
    u_start = temp
    print(colored(temp, "blue"))
  # print(colored(f"start={start} index={index} end ={end} size={board_size}", "blue"))

  for e in u_start:
    i = e[0] + 1

    for k in range(-1, 2):
      j = e[1] + k
      if [i,j] in end:
        win.append([i,j])
  # print(colored(win, "blue"))

  if len(win) > 1:
    return 2
  if len(win) == 0:
    return 0
  
  return 1

  
def game_status(board_size, board):
  red_play = 0
  red_start = list()
  red_index = list()
  red_end = list()
  red_check = True

  blue_play = 0
  blue_start = list()
  blue_index = list()
  blue_end = list()
  blue_check = True

  # print(colored(f"number_of_days = {board_size} vistors = {board}", "red"))

  if board_size == 1:
    if board[0][0] == "R":
      return "Red wins"
    elif board[0][0] == "B":
      return "Blue wins"
    else:
      return "Nobody wins" 

  for i in range(board_size):
    if "R" not in board[i]:
      red_check = False

    count = 0
    for j in range(board_size):
      if board[j][i] == "B":
        blue_play += 1
        count += 1

        if i != 0 and i != board_size-1:
          blue_index.append([j,i])
        if i == board_size-1:
          blue_end.append([j,i])
        if i == 0:
          blue_start.append([j,i])
        
      elif board[j][i] == "R":
        red_play += 1
        if j != 0 and j != board_size-1:
          red_index.append([j,i])
        if j == board_size-1:
          red_end.append([j,i])
        if j == 0:
          red_start.append([j,i])
        
    if count == 0:
      blue_check = False

  # print(colored(f"red_check={red_check}, red_start={red_start}, red_index={red_index}, red_end={red_end}, red={red_start+red_index+red_end}", "red"))
  # print(colored(f"blue_check={blue_check}, blue_start={blue_start}, blue_index={blue_index}, blue_end={blue_end}", "blue"))

  # "Impossible", "Blue wins", "Red wins", or "Nobody wins"

  l_diff = blue_play-red_play
  l_diff = l_diff if l_diff>0 else 0-l_diff

  if l_diff>1:
    return "Impossible"

  if red_check:
    red_result = red(red_start, red_index, red_end, board_size)
    print(colored(red_result, "red"))
  
  if blue_check:
    blue_result = blue(blue_start, blue_index, blue_end, board_size)
    print(colored(blue_result, "blue"))

  return "Nobody wins"

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    board_size = int(input())
    board = []
    for _ in range(board_size):
      board.append(list(input().strip()))

    ans = game_status(board_size, board)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
