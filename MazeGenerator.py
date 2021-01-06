from __future__ import print_function

import random
import sys


openScale = 7 # 1-9; 1 ~ MAXIMUM #WALLS || 9 ~ MINIMUM #WALLS
SIZE = 4
EMPTY = ' 0 , '
WALL = '-1 , '
AGENT = ' 0 , '
GOAL = ' 0 , '
# SIZE = 4
# EMPTY = ' '
# WALL = '#'
# AGENT = 'S'
# GOAL = 'E'

def adjacent(cell):
  i,j = cell
  for (y,x) in ((1,0), (0,1), (-1, 0), (0,-1)):
    yield (i+y, j+x), (i+2*y, j+2*x)

def generate(width, height, verbose=True):
  '''Generates a maze as a list of strings.
     :param width: the width of the maze, not including border walls.
     :param heihgt: height of the maze, not including border walls.
  '''
  # add 2 for border walls.
  global openScale
  global SIZE
  global EMPTY
  global WALL
  global AGENT
  global GOAL

  width += 0
  height += 0
  rows, cols = height, width

  maze = {}

  spaceCells = set()
  connected = set()
  walls = set()

  # Initialize with grid.
  for i in range(rows):
    for j in range(cols):
      if (i%2 == 1) and (j%2 == 1):
        maze[(i,j)] = EMPTY
      else:
        maze[(i,j)] = WALL

  # Fill in border.
  for i in range(rows):
    maze[(i,0)] = WALL
    maze[(i,cols-1)] = WALL
  for j in range(cols):
    maze[(0,j)] = WALL
    maze[(rows-1,j)] = WALL

  for i in range(rows):
    for j in range(cols):
      if maze[(i,j)] == EMPTY:
        spaceCells.add((i,j))
      if maze[(i,j)] == WALL:
        walls.add((i,j))

  # Prim's algorithm to knock down walls.
  originalSize = len(spaceCells)
  connected.add((1,1))
  while len(connected) < len(spaceCells):
    doA, doB = None, None
    cns = list(connected)
    random.shuffle(cns)
    for (i,j) in cns:
      if doA is not None: break
      for A, B in adjacent((i,j)):
        if A not in walls:
          continue
        if (B not in spaceCells) or (B in connected):
          continue
        doA, doB = A, B
        break
    A, B = doA, doB
    maze[A] = EMPTY
    walls.remove(A)
    spaceCells.add(A)
    connected.add(A)
    connected.add(B)
    if verbose:
      cs, ss = len(connected), len(spaceCells)
      cs += (originalSize - ss)
      ss += (originalSize - ss)
      if cs % 10 == 1:
        print('%s/%s cells connected ...' % (cs, ss), file=sys.stderr)



  # Insert character and goals.
  TL = (agent_X,agent_Y)
  BR = (goal_X, goal_Y)
  # if rows % 2 == 0:
  #   BR = (BR[0]-1, BR[1])
  # if cols % 2 == 0:
  #   BR = (BR[0], BR[1]-1)

  maze[TL] = AGENT
  maze[BR] = GOAL

  lines = []
  for i in range(rows):
    line = ''.join(maze[(i,j)] for j in range(cols))
    line = line[:-3]
    lines.append(line)

  return lines

# ================ MAIN ================
if __name__ == '__main__':


  print("Enter maze size")
  SIZE = int(input())
  print("Enter walls ratio: 1-{} (1 - minimum number of walls, {} maximum number of walls)".format(SIZE**2,SIZE**2))
  openScale = int(input())
  print("Enter starting point, x coordinate (1+)")
  agent_X = int(input())
  print("Enter starting point, y coordinate (1+)")
  agent_Y = int(input())
  print("Enter goal point, x coordinate (2 - {})".format(SIZE - 2))
  goal_X = int(input())
  print("Enter goal point, y coordinate (2 - {})".format(SIZE - 2))
  goal_Y = int(input())


  width = SIZE
  height = SIZE

  args = sys.argv[1:]
  if len(args) >= 1:
    width = int(args[0])
  if len(args) >= 2:
    height = int(args[1])

  if len(args) < 2:
    print('Use command-line args to specify width and height.', file=sys.stderr)
    print('  Odd numbers are suggested because of the walls.', file=sys.stderr)
  print('Non-maze text is printed to stderr, so you \n  can use > to pipe just the maze to a file.\n', file=sys.stderr)

  print('Generating %sx%s maze (not including border)...\n' % (width, height), file=sys.stderr)

  maze = generate(width, height)

  print('Done.\n', file=sys.stderr)

  #print('\n'.join(maze))

  # add numbers
  mazeSize = width
  lines = []
  newMaze = [[0 for x in range(int(mazeSize))] for y in range(int(mazeSize))]
  for i in range(0,int(mazeSize)):
    lines.append(maze[i])

  for i in range(0, int(mazeSize)):

    line = lines[i]
    splitted = line.split(',')
    for j in range(0, int(mazeSize)):
      if '0' in splitted[j]:
        newMaze[j][i] = random.randint(5,9)
      elif '-1' in splitted[j]:
        # decreasing num of walls

        if random.randint(1,openScale) == 1 or (j == agent_X and i == agent_Y) or (j == goal_X and i == goal_Y):
          newMaze[j][i] = random.randint(5, 9)
        else:
          newMaze[j][i] = -1




  print("UCS")
  print(SIZE)
  print(''+str(agent_X)+','+str(agent_Y))
  print(''+str(goal_X)+','+str(goal_Y))
  # print it
  for i in range(0, int(mazeSize)):
    for j in range(0, int(mazeSize)):
      if j == int(mazeSize) - 1:
        if j==0:
          print(str(newMaze[j][i]), end="", flush=True)
        else:
          print(' ' + str(newMaze[j][i]), end="", flush=True)
      else:
        if j==0:
          print(str(newMaze[j][i]) + ',', end="", flush=True)
        else:
          print(' ' + str(newMaze[j][i]) + ',', end="", flush=True)

    print('')

  print('')
  print('')
  print("PRESS ENTER TO EXIT")
  input()
input()
#import random

# script to generate mazes

# size = 450
# decreaseVal = 0
# for i in range(0,size):
#     for j in range(0,size):
#         randomNumber = random.randint(1,12)
#         while randomNumber == decreaseVal:
#             randomNumber = random.randint(1,size-2)
#         if j%4 == 0:
#             randomNumber = 2
#         if j%7 == 0:
#             randomNumber = 2
#         if i < j+2 and i> j-2:
#             if i%3 == 0:
#                 randomNumber = 1
#         print(randomNumber-decreaseVal,end="",flush=True)
#         if j is not size-1:
#             print(',', end="", flush=True)
#     print("")
