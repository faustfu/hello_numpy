import gym
import numpy as np
import matplotlib.pyplot as plt

def do_episode(w, env): # 給定特定權重，計算行動步數
    done = False
    observation = env.reset()
    num_steps = 0

    while not done and num_steps <= max_number_of_steps:
        action = take_action(observation, w)
        observation, _, done, _ = env.step(action)
        num_steps += 1

    step_val = -1 if num_steps >= max_number_of_steps else num_steps - max_number_of_steps
    return step_val, num_steps

def take_action(X, w): # 依據狀態分數決定行動
    action = 1 if calculate(X, w) > 0.0 else 0
    return action

def calculate(X, w): # 計算特定權重下的狀態分數
    result = np.dot(X, w)
    return result

env = gym.make('CartPole-v0')

#env.render()

eta = 0.2
sigma = 0.05

max_episodes = 5000
max_number_of_steps = 200
n_states = 4
num_batch = 10
num_consecutive_iterations = 100

w = np.random.randn(n_states) # 4個狀態的權重
reward_list = np.zeros(num_batch)
reward_h = []
last_time_steps = np.zeros(num_consecutive_iterations)
mean_list = []

for episode in range(max_episodes//num_batch):
    N = np.random.normal(scale=sigma,size=(num_batch, w.shape[0]))
    for i in range(num_batch):
        w_try = w + N[i]
        reward, steps = do_episode(w_try, env)
        if i == num_batch-1:
            print('%d Episode finished after %d steps / mean %f' %(episode*num_batch, steps, last_time_steps.mean()))
        last_time_steps = np.hstack((last_time_steps[1:], [steps]))
        reward_list[i] = reward
        mean_list.append(last_time_steps.mean())

    if last_time_steps.mean() >= 195: break 

    std = np.std(reward_list)
    if std == 0: std = 1
    A = (reward_list - np.mean(reward_list))/std
    w_delta = eta /(num_batch*sigma) * np.dot(N.T, A)
    w += w_delta


env.close()

plt.plot(mean_list)
plt.xlabel("episode")
plt.ylabel("mean_step")
plt.show()