import time
import mazes as m

StepCost = 1

def print_spacer():
    print(m.spacer)

def getInicialState(index): # onde está o início?
    y_pos = 0
    for y in m.maze_matrix[index]:
        x_pos = 0
        for x in y:
            if x == 2: return x_pos,y_pos
            x_pos = x_pos + 1
        y_pos = y_pos + 1

def sucessor(matrix,x,y): # onde posso ir?
    possibilities = []
    if matrix[y][x-1] == 1 or matrix[y][x-1] == 3:
        possibilities.append([x-1,y])
    if matrix[y-1][x] == 1 or matrix[y-1][x] == 3:
        possibilities.append([x,y-1])
    if matrix[y+1][x] == 1 or matrix[y+1][x] == 3:
        possibilities.append([x,y+1])
    if matrix[y][x+1] == 1 or matrix[y][x+1] == 3:
        possibilities.append([x+1,y])
    return possibilities

def result():
    print("")

def objetivo(matrix,x,y): # chegou ao objetivo?
    if matrix[y][x] == 3:
        print("Objetivo atingido!")
        return True
    return False

def PathCost():
    print("")

def print_matrix(m):
    for line in m:
        print(line)

def replace_char(string,matrix,x,y,char):
    # marcando como visitano na matriz
    matrix[y][x] = 4
    # ilustrando na string
    char_pos = 2*x + 42*y # retificação da posição na matriz para o labirinto em texto
    string = string[:char_pos] + char + string[char_pos+1:]
    return string, matrix

def mark_visited(string,matrix,x,y):
    return replace_char(string,matrix,x,y,'▣')

def walk_into_path(matrix,string,x,y):
    possibilities = sucessor(matrix,x,y)
    if len(possibilities) < 1: return
    for path in possibilities:
        x = path[0]
        y = path[1]
        if objetivo(matrix,x,y): exit(1)
        string,matrix = mark_visited(string,matrix,x,y)
        time.sleep(0.2)
        print_spacer()
        print(string)
        walk_into_path(matrix,string,x,y)

