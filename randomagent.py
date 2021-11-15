import gym
import random

#Create our CartPole environment
env = gym.make('CartPole-v0')
env.reset()

def RandomAgent():
    randomAction = 1


    #each episode is a game that is run to its end
    for epoch in range (10):
        #now we break up the frames
        for t in range (500):
            env.render()

            action = env.action_space.sample()

            #the next state, rewards, done flag, and info are all returned
            next_state, reward, done, info = env.step(action)

            action = env.action_space.sample()

            #the next state, rewards, done flag, and info are all returned
            next_state, reward, done, info = env.step(action)

            print(t, next_state, reward, done, info, action)
            if done:
                env.reset()
                break

RandomAgent()