** 
姓名：刘铎 amos.Liu  
班级：软件工程班 
学号：2019102962  
time: 2020/6/19 
**

###
一、工程概述：
代码包含了强化学习几种算法的具体实现。
主要研究方向：ReinforcementLearning & recommendation system

ps：最近在做关于求职推荐路径推荐用到了包括generator,decorator等课上着重讲的方法，因为代码还不成熟，暂时不放上来了
###

###
二、主要工作（包含算法）：
DQN及其变种: doubleDQN,duelingDQN,DDQN;
AC及其变种：A2C，A3C，DDPO 后面几种方法还没有没有具体实现，只看了理论设计
###

###
三、环境相关说明：

在OpenAI的gym环境下，进行模型训练。 ps：使用前需要 pip install gym
运行的环境有：'Pendulum-v0'，'CartPole-v0'

```
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action

```

每个文件夹为一个算法的实现，通过gym或者自建的环境进行实践
具体运行环境在每个文件的title里注明
eg:
```
"""
Double DQN & Natural DQN comparison,
The Pendulum example.
Using:
Tensorflow: 1.0
gym: 0.8.0
"""
```

for DQN,double&dueling
这是两个实验为基础的代码，比较了不同算法的性能区别
通过 import matplotlib.pyplot as plt 直观显示算法速度和稳定性的差异

###

###
四、具体代码实现简述（以QLearning为例）：

主要目的： 训练一个智能体走迷宫的游戏

**maze_env.py**
环境搭建，通过 import TKinter 构建一个 4*4 maze
```
import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk 
```

**RL_brain.py**
智能体构建，主要运用Q-learning来进行一个智能体决策过程。
```
    def choose_action(self, observation):
        # action selection
        if:
            # choose best action
        else:
            # choose random action
        return action

    def learn(self, s, a, r, s_):
        if:
            # next state is not terminal
        else:
            # next state is terminal
     # update
```

**run_this.py**
启动，把探索次数设置为100次
```
if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
```
###

###
五、感悟及感谢：
    之前对python有一点基础，熟悉Django和Flask的一些项目。本对课程并没有特别高的期待，但却被王老师的热情所感动，所感染。虽然总是对python的发展有很多质疑，想转向go的开发。但是还是在王老师的耐心讲解中获取了力量，深感自己需要更多夯实基础脚踏实地的学习。祝老师未来一切顺利，期待以后与您的更多交流。