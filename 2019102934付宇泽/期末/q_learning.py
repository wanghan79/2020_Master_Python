import numpy as np
import time
from env import Env

EPSILON = 0.1  # 贪婪程度
ALPHA = 0.1  # 学习率
GAMMA = 0.9  # 衰减因子
MAX_STEP = 30  # 最大步数

np.random.seed(0)


def epsilon_greedy(Q, state):
    if (np.random.uniform() > 1 - EPSILON) or ((Q[state, :] == 0).all()):
        action = np.random.randint(0, 4)  # 探索环境
    else:
        action = Q[state, :].argmax()  # 贪婪,选取最大未来奖励
    return action


e = Env()
Q = np.zeros((e.state_num, 4))  # 初始化Q_table,45*4

for i in range(50):
    e = Env()
    while (e.is_end is False) and (e.step < MAX_STEP):
        action = epsilon_greedy(Q, e.present_state)  # 选取策略
        state = e.present_state
        # print(action, state)
        reward = e.interact(action)  # 执行动作并获得奖励
        new_state = e.present_state
        Q[state, action] = (1 - ALPHA) * Q[state, action] + \
                           ALPHA * (reward + GAMMA * Q[new_state, :].max())  # 更新Q_table
        e.print_map()
        time.sleep(0.1)
    print('Episode:', i, 'Total Step:', e.step, 'Total Reward:', e.total_reward)
    time.sleep(2)
print(Q)