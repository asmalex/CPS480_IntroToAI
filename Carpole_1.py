import gym

env = gym.make('CartPole-v1')
env.reset()

for t in range(1000):
    env.render()
    action = env.action_space.sample() 
    
    next_state, reward, done, info = env.step(action)
    print(t, next_state, reward, done, info, action) 
    
env.close()