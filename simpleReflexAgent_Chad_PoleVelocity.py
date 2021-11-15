import gym 
import random 
#Create our CartPole environment 
env = gym.make('CartPole-v0') 
env.reset() 

def RandomAgent(): 
    #each episode is a game that is run to its end 
    randomAction=1
    for epoch in range (10): 
        #now we break up the frames 
        for t in range (500): 
            env.render() 

            if randomAction ==1:
                action = env.action_space.sample() 
            else:
                if next_state[3]>0:
                    action=1
                else:
                    action=0

            #the next state, rewards, done flag, and info are all returned 
            next_state, reward, done, info = env.step(action) 
            print(t, next_state, reward, done, info, action) 
            randomAction=0
            if done: 
                env.reset() 
                break

RandomAgent()