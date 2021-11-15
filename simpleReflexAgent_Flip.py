import gym 
import random 
#Create our CartPole environment 
env = gym.make('CartPole-v0') 
env.reset() 

def RandomAgent(): 
    #each episode is a game that is run to its end 
    flipDirection=0
    for epoch in range (10): 
        #now we break up the frames 
        for t in range (500): 
            env.render() 

            #the next state, rewards, done flag, and info are all returned 
            next_state, reward, done, info = env.step(flipDirection) 
            print(t, next_state, reward, done, info, flipDirection) 
            randomAction=0
            if done: 
                env.reset() 
                break

            if flipDirection == 0:
                flipDirection = 1
            else:
                flipDirection = 0

RandomAgent()