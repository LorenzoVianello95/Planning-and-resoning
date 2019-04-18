import numpy as np
import matplotlib.pyplot as plt
from lrta import *

map= np.zeros((10,10))
#print(map)

forbidden_cels= [[0, 6], [1,6], [2,6], [3,6], [4,6], [5,6], [6,6], [6,4], [6,5]]

def create_env(map_env, forb_cells):
	for c in forb_cells:
		map_env[c[0], c[1]]= 10
	return map_env

map= create_env(map, forbidden_cels)


#plt.matshow(map)
#plt.show()

start_state=[0,0]
goal_state=[0,9]
map_heuristic= np.zeros((10,10))
map_distance_from_start= np.zeros((10,10))

def assign_provv_map(map_h, goal):
	for i in range(10):
		for j in range(10):
			map_h[i, j]= abs(i-goal[0])+ abs(j-goal[1])

	return map_h

map_heuristic= assign_provv_map(map_heuristic, goal_state)
map_distance_from_start= assign_provv_map(map_distance_from_start, start_state)
#print(map_distance_from_start)
#plt.matshow(map_heuristic)
#plt.show()

traj= lrta_search(map_heuristic,map_distance_from_start, start_state, goal_state, forbidden_cels)
#print(traj)



