import random as rand
import mazes as m
import mazeFunctions as mf

number_of_mazes = 4
chosen_maze = rand.randrange(number_of_mazes)

maze_string = m.maze_char[chosen_maze]
matrix = m.maze_matrix[chosen_maze]

cur_x,cur_y = mf.getInicialState(chosen_maze)
mf.walk_into_path(matrix,maze_string,cur_x,cur_y)

