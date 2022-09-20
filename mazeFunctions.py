import mazes as m

StepCost = 1

def getInicialState(index): # onde está o início?
    y_pos = 0
    for y in m.maze_matrix[index]:
        x_pos = 0
        for x in y:
            if x == 2: return x_pos,y_pos
            x_pos = x_pos + 1
        y_pos = y_pos + 1

def sucessor(index,x,y): # onde posso ir?
    possibilities = []
    if m.maze_matrix[index][y-1][x-1] == 1:
        possibilities.append([x-1,y-1])
    if m.maze_matrix[index][y][x-1] == 1:
        possibilities.append([x-1,y])
    if m.maze_matrix[index][y+1][x-1] == 1:
        possibilities.append([x-1,y+1])
    if m.maze_matrix[index][y-1][x] == 1:
        possibilities.append([x,y-1])
    if m.maze_matrix[index][y+1][x] == 1:
        possibilities.append([x,y+1])
    if m.maze_matrix[index][y-1][x+1] == 1:
        possibilities.append([x+1,y-1])
    if m.maze_matrix[index][y][x+1] == 1:
        possibilities.append([x+1,y])
    if m.maze_matrix[index][y+1][x+1] == 1:
        possibilities.append([x+1,y+1])
    return possibilities

def result():
    print("")

def objetivo(index,x,y): # chegou ao objetivo?
    if m.maze_matrix[index][y][x] == 3:
        print("Objetivo atingido!")
        return True
    return False

def PathCost():
    print("")

def replace_char(string,matrix,x,y):
    # marcando como visitano na matriz
    print(x,y)
    matrix[y][x] = 4
    print(matrix)
    # ilustrando na string
    char_pos = 2*x + 42*y # retificação da posição na matriz para o labirinto em texto
    string = string[:char_pos] + '▣' + string[char_pos+1:]
    print(string)
    return string, matrix
