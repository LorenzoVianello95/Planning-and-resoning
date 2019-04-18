from maze_env import Maze

import matplotlib.pyplot as plt
import sys
from scipy.spatial import distance
import numpy as np
import time
import thread
import pygame
from pygame.locals import *
pygame.init()

def run_maze():
    step = 0
    nr=0
    rr = []  # reward per ogni singola esistenza
    rrr = []
    NUM_ITERATION=5000
    flag_aut_man= "m"
    for episode in range(NUM_ITERATION):
        observation = env.reset()
    
        number_of_iteration=100

        for _ in range(number_of_iteration):
        #while True:
            # fresh env
            env.render()
        
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            if (observation_[0]!=observation[0] or observation_[1]!=observation[1]):
                if (reward==10):
                    nr+=1

                RL.store_transition(observation, action, reward, observation_)

                if (step > 200) and (step % 5 == 0):
                    RL.learn()

                # swap observation
                observation = observation_

                # break while loop when end of this episode
                if done:
                    print(episode," ",reward)
                    rr.append(reward)
                    if len(rr)> NUM_ITERATION/100:
                        s=sum(rr)
                        m=float(s)/len(rr)
                        rrr.append(m)
                        rr=[]
                    break
                step +=1

    # end of game
    print('game over')
    plt.plot( rrr, 'r--')
    plt.show()
    print(nr)
    env.destroy()


if __name__ == "__main__":
    # maze game
    flag = input('Enter what u want(1 for first version, 2 for second): ')
    if flag==1:
        env = Maze()
        RL = DeepQNetwork(env.n_actions, env.n_features,
                          learning_rate=0.01,
                          reward_decay=0.9,
                          e_greedy=0.9,
                          replace_target_iter=200,
                          memory_size=10000,
                          # output_graph=True
                          )
        env.after(1000, run_maze)
        env.mainloop()
        #RL.plot_cost()
