board = [ "-","-","-",
          "-","-","-",
          "-","-","-"]
game_running = True
CurrentPlayer = "X"
Winner = None

def play_game():

  displayboard()

  while game_running:
    handle_turn(CurrentPlayer)
    GameOver()
    FlipPlayer()
  
 

def displayboard():
  print(board[0] + "|" + board[1] +"|" + board[2])
  print(board[3] + "|" + board[4] +"|" + board[5])
  print(board[6] + "|" + board[7] +"|" + board[8])


def CheckIfWin():
  global CurrentPlayer
  global Winner
  RowWinner = RowWin()
  ColumnWinner = ColumnWin()
  DiagonalWinner = DiagonalWin()
  if RowWinner or ColumnWinner or DiagonalWinner:
    Winner = CurrentPlayer
    return True
  return False

def CheckIfTie():
  global game_running
  global board
  x = 0
  while x < 9:
    if board[x] == "-":
      return False
    x = x + 1
  game_running = False
  return True

def RowWin():
  global game_running
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  if row1 or row2 or row3:
    game_running = False
    return True
    
def ColumnWin():
  global game_running
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"
  if column1 or column2 or column3:
    game_running = False
    return True

def DiagonalWin():
  global game_running
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
  if diagonal1 or diagonal2:
    game_running = False
    return True


def handle_turn(CurrentPlayer):
  YourTurn = True
  while YourTurn:
    position = int(input("Choose a position from 1-9: ")) - 1
    if board[position] is "-":
     board[position] = CurrentPlayer
     YourTurn = False
    else:
     print("Place Already Filled!")
  displayboard()



def GameOver():
  CheckIfWin()
  CheckIfTie()

def FlipPlayer():
  global CurrentPlayer
  if CurrentPlayer == "O":
    CurrentPlayer = "X"
  elif CurrentPlayer == "X":
    CurrentPlayer = "O"

tryagain = True
while tryagain:

  play_game()
  if Winner is None:
    print("Tie.")
  else:
    print(Winner + " won!")
  playagain = input("Do you want to try again? (Y/N) ")
  if playagain == "Y":
    tryagain = True
    board = [ "-","-","-",
          "-","-","-",
          "-","-","-"]
    game_running = True
    CurrentPlayer = "X"
    Winner = None
  else:
    tryagain = False
    break
