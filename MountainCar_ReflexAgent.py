import gym 
import random 

#Create our MountainCar Environment
env = gym.make('MountainCar-v0') 
env.reset() 

def RandomAgent(): 
    #each episode is a game that is run to its end 
    
    for epoch in range (10): 
        #now we break up the frames 
        for t in range (500): 
            env.render() 
            
            if(next_state[1] < 0)
                action = 0
            elif
                action = 2

            #the next state, rewards, done flag, and info are all returned 
            next_state, reward, done, info = env.step(action) 
            print(t, next_state, reward, done, info, action) 
            
            if done: 
                env.reset() 
                break

RandomAgent()