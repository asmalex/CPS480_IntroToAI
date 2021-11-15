import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(20):
    env.render()
    env.step(env.action_space.sample()) #end the study when the pole tips more than 15 degrees
env.close()