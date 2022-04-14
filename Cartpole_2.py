import gym

env = gym.make('CartPole-v1')
env.reset()

for t in range(1000):
    env.render()

    #fallback conditions
    if (t == 0):
        action = env.action_space.sample() 
        next_state = (0,0,0,0)
    else:
        if(next_state[0] < 2.2):
            action = 1
        elif(next_state[0] > 2.2):
            action = 0
    
    if(next_state[2] < -0.1):
        action = 0
    elif(next_state[2] > 0.1):
        action = 1
    else:
        if(action == 0):
            action = 1
        elif(action == 1):
            action = 0
    
    next_state, reward, done, info = env.step(action)
    print(t, next_state, reward, done, info, action) 
    
    #terminate if we've exceeded bounds or cartpole has tipped beyond 15 degrees
    #if(done):
    #    break
    
env.close()