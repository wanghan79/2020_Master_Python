import copy

"""MAP = \
    '''
.........
.       .
.     o .
.       .
.........
'''"""

MAP = \
    '''
.........
.  x    .
.   x o .
.       .
.........
'''
# MAP处理遍历
MAP = MAP.strip().split('\n')
MAP = [[c for c in line] for line in MAP]

# 动作集
DX = [-1, 1, 0, 0]  # 行位移
DY = [0, 0, -1, 1]  # 列位移


class Env(object):
    def __init__(self):
        self.map = copy.deepcopy(MAP)  # 深复制MAP
        self.x = 1  # 行位置
        self.y = 1  # 列位置
        self.step = 0
        self.total_reward = 0
        self.is_end = False

    def interact(self, action):
        assert self.is_end is False
        new_x = self.x + DX[action]
        new_y = self.y + DY[action]
        new_pos_char = self.map[new_x][new_y]
        self.step += 1
        if new_pos_char == '.':  # 新位置在无效位置不移动
            reward = 0
        elif new_pos_char == ' ':
            self.x = new_x
            self.y = new_y  # 更新位置
            reward = 0
        elif new_pos_char == 'o':  # 新位置在目的地
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '  # 更新位置
            self.is_end = True  # end
            reward = 100
        elif new_pos_char == 'x':  # 新位置在陷阱
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '  # 更新位置
            reward = -5
        self.total_reward += reward
        return reward

    @property
    def state_num(self):
        rows = len(self.map)
        cols = len(self.map[0])
        return rows * cols

    @property
    def present_state(self):
        cols = len(self.map[0])
        return self.x * cols + self.y

    def print_map(self):
        printed_map = copy.deepcopy(self.map)
        printed_map[self.x][self.y] = 'A'
        print('\n'.join([''.join([c for c in line]) for line in printed_map]))
