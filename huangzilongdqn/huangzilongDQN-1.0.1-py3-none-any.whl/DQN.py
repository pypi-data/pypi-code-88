import tensorflow as tf

from tensorflow.keras import layers, optimizers, datasets, Sequential
import numpy as np
from collections import \
    deque  # deque 是一个双端队列, 如果要经常从两端append 的数据, 选择这个数据结构就比较好了, 如果要实现随机访问,不建议用这个,请用列表.deque 优势就是可以从两边append ,appendleft 数据. 这一点list 是没有的.
import random

import matplotlib.pyplot as plt
import pandas as pd

r = np.array([[-10, -10, -10, -10, -1, -10],
              [-10, -10, -10, -1, -10, 10],
              [-10, -10, -10, -1, -10, -10],
              [-10, -1, -1, -10, -1, -10],
              [-1, -10, -10, -1, -10, 10],
              [-10, -1, -10, -10, -1, 10]])

# r = np.array([[-1, -1, -1, -1, 0, -1],
#               [-1, -1, -1, 0, -1, 100],
#               [-1, -1, -1, 0, -1, -1],
#               [-1, 0, 0, -1, 0, -1],
#               [0, -1, -1, 0, -1, 100],
#               [-1, 0, -1, -1, 0, 100],
#               ])

# 执行步数。
step_index = 0

# 状态数。
state_num = 6

# 动作数。
action_num = 6

# 训练之前观察多少步。
OBSERVE = 11.

# 选取的小批量训练样本数。
BATCH = 40  # 一般是较大会有比较好的效果，一是更快收敛，二是可以躲过一些局部最优点。但是也不是一味地增加batch size就好，太大的batch size 容易陷入sharp minima，泛化性不好。较小的batch size可能会使得网络有明显的震荡。

# epsilon 的最小值，当 epsilon 小于该值时，将不在随机选择行为。
FINAL_EPSILON = 0.0001

# epsilon 的初始值，epsilon 逐渐减小。
INITIAL_EPSILON = 0.1

# epsilon 衰减的总步数。
EXPLORE = 3000000.

# 探索模式计数。
epsilon = INITIAL_EPSILON

# 训练步数统计。
learn_step_counter = 0

# 学习率。
learning_rate = 0.001

# γ经验折损率。
gamma = 0.9

# 记忆上限。
memory_size = 5000

# 当前记忆数。
memory_counter = 0

# 保存观察到的执行过的行动的存储器，即：曾经经历过的记忆。
replay_memory_store = deque()

# 生成一个状态矩阵（6 X 6），每一行代表一个状态。
state_list = np.identity(state_num)

# 生成一个动作矩阵。
action_list = np.identity(action_num)

acclist = []
lostlist = []

# 学习率
a = 0.5


class DeepQNetwork:

    def __init__(self):
        # 创建神经网络。
        self.model = self.create_model()
        self.target_model = self.create_model()

    def create_model(self):
        self.model = Sequential(
            [
                layers.Reshape((3, 2)),
                layers.Conv1D(filters=16, kernel_size=1, strides=1, padding='same', activation='selu'),
                layers.Conv1D(filters=16, kernel_size=1, strides=1, padding='same', activation='selu'),
                layers.MaxPool1D(pool_size=1, strides=1, padding='same'),
                layers.Conv1D(filters=32, kernel_size=1, strides=1, padding='same', activation='selu'),
                layers.Conv1D(filters=32, kernel_size=1, strides=1, padding='same', activation='selu'),
                layers.MaxPool1D(pool_size=1, strides=1, padding='same'),
                layers.Flatten(),
                layers.Dense(units=6)
            ]
        )

        #     # layers.Dense(units=128, activation='selu',kernel_regularizer=tf.keras.regularizers.l2(0.05)),
        #     # layers.Dense(units=64, activation='selu',kernel_regularizer=tf.keras.regularizers.l2(0.05)),
        #     # layers.Dense(units=32, activation='selu',kernel_regularizer=tf.keras.regularizers.l2(0.05)),
        #     # layers.Dense(units=16, activation='selu',kernel_regularizer=tf.keras.regularizers.l2(0.05)),
        #     # layers.BatchNormalization(),
        #     # layers.Dense(units=6)])

        self.model.build(input_shape=(None, 6))
        self.model.compile(optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['accuracy'],
                           loss=tf.keras.losses.mse)
        self.model.summary()
        return self.model

    def select_action(self, state_index):
        """
        根据策略选择动作。
        :param state_index: 当前状态。
        :return:
        """
        global epsilon
        current_state = state_list[state_index:state_index + 1]

        if step_index <= OBSERVE:
            if step_index < 6:
                current_action_index = step_index
            else:
                current_action_index = step_index - 6

        if step_index > OBSERVE:
            if np.random.uniform() < epsilon:
                current_action_index = np.random.randint(0, action_num)
            else:
                actions_value = self.model.predict(current_state)
                action = np.argmax(actions_value)
                current_action_index = action
            # 开始训练后，在 epsilon 小于一定的值之前，将逐步减小 epsilon。
            if step_index > OBSERVE and epsilon > FINAL_EPSILON:
                epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE
        return current_action_index

    def step(self, state, action):
        """
        执行动作。
        :param state: 当前状态。
        :param action: 执行的动作。
        :return:
        """
        reward = r[state][action]

        next_state = action

        done = False

        if action == 5:
            done = True

        return next_state, reward, done

    def save_store(self, current_state_index, current_action_index, current_reward, next_state_index, done):
        """
        保存记忆。
        :param current_state_index: 当前状态 index。
        :param current_action_index: 动作 index。
        :param current_reward: 奖励。
        :param next_state_index: 下一个状态 index。
        :param done: 是否结束。
        :return:
        """
        current_state = state_list[current_state_index:current_state_index + 1]
        current_action = action_list[current_action_index:current_action_index + 1]
        next_state = state_list[next_state_index:next_state_index + 1]
        # 记忆动作(当前状态， 当前执行的动作， 当前动作的得分，下一个状态)。
        replay_memory_store.append((
            current_state,
            current_action,
            current_reward,
            next_state,
            done))

        # 如果超过记忆的容量，则将最久远的记忆移除。
        if len(replay_memory_store) > memory_size:
            replay_memory_store.popleft()
        global memory_counter
        memory_counter += 1

    def experience_replay(self):
        """
        记忆回放。
        :return:
        """
        global learn_step_counter
        global a
        # 随机选择一小批记忆样本。
        batch = BATCH if memory_counter > BATCH else memory_counter  # 相当于三目运算符效果，三目运算符：对于条件表达式  b ? x : y ，先计算条件b，然后进行判断。如果b的值为true，计算x的值，运算结果为x的值；否则，计算y的值，运算结果为y的值。一个条件表达式绝不会既计算x，又计算y。条件运算符是右结合的，也就是说，从右向左分组计算。
        # 如果a > b的结果为真，h = "变量1", 如果为假，h = "变量2"
        # h = "变量1" if a>b else "变量2"

        minibatch = random.sample(replay_memory_store, batch)  # 用于截取列表的指定长度的随机数，但是不会改变列表本身的排序

        batch_state = None
        batch_action = None
        batch_reward = None
        batch_next_state = None
        batch_done = None
        # 把minibatch中的值取出来
        for index in range(len(minibatch)):

            if batch_state is None:
                batch_state = minibatch[index][0]
            elif batch_state is not None:
                batch_state = np.vstack((batch_state, minibatch[index][0]))  # np.vstack:按垂直方向（行顺序）堆叠数组构成一个新的数组

            if batch_action is None:
                batch_action = minibatch[index][1]
            elif batch_action is not None:
                batch_action = np.vstack((batch_action, minibatch[index][1]))

            if batch_reward is None:
                batch_reward = minibatch[index][2]
            elif batch_reward is not None:
                batch_reward = np.vstack((batch_reward, minibatch[index][2]))

            if batch_next_state is None:
                batch_next_state = minibatch[index][3]
            elif batch_next_state is not None:
                batch_next_state = np.vstack((batch_next_state, minibatch[index][3]))

            if batch_done is None:
                batch_done = minibatch[index][4]
            elif batch_done is not None:
                batch_done = np.vstack((batch_done, minibatch[index][4]))

        # q_predict_next：下一个状态的 Q 值。
        q_predict_next = self.target_model.predict(batch_next_state)

        # 当前state的对应q值表
        q_current_value = self.model.predict(batch_state)

        # 目标 Q 值
        q_target = []

        # 这里可以参考第一部分中所描述的计算方法
        # 循环计算目标Q值
        for i in range(len(minibatch)):

            # 当前即时得分。
            current_reward = batch_reward[i][0]

            # 更新 Q 值。
            new_q_value = current_reward + gamma * np.max(q_predict_next[i])

            # 获取自身Q值的预测
            cur_q_value = q_current_value[i]

            new_q_value = (1 - a) * cur_q_value[batch_next_state[i].argmax()] + a * new_q_value

            # 当得分小于 -1 时，表示走了不可走的位置。
            if current_reward == -10:
                cur_q_value[batch_next_state[
                    i].argmax()] = current_reward
                q_target.append(cur_q_value)

            else:
                cur_q_value[batch_next_state[i].argmax()] = new_q_value
                q_target.append(cur_q_value)

        q_target = np.asarray(
            q_target)  # np.array与np.asarray功能是一样的，都是将输入转为矩阵格式,np.array与np.asarray的区别，其在于输入为数组时，np.array是将输入copy过去而np.asarray是将输入cut过去，所以随着输入的改变np.array的输出不变，而np.asarray的输出在变化

        # 更新网络

        history = self.model.fit(batch_state, q_target, epochs=1, batch_size=len(minibatch))
        learn_step_counter += 1
        if learn_step_counter % 50 == 0:
            # 每 50 步，将 model 的权重赋值给 target_model
            self.target_model.set_weights(self.model.get_weights())
        return history.history

    def train(self):
        """
        训练。
        :return:
        """

        # 初始化当前状态。
        current_state = np.random.randint(0, action_num - 1)  ###随机初始状态
        # epsilon = INITIAL_EPSILON

        global step_index

        while True:

            # 选择动作。

            action = self.select_action(current_state)  ###由初始状态current_state根据策略选择action

            # 执行动作，得到：下一个状态，执行动作的得分，是否结束。
            next_state, reward, done = self.step(current_state, action)

            # 保存记忆。
            self.save_store(current_state, action, reward, next_state, done)

            # 先观察一段时间累积足够的记忆再进行训练。
            if step_index > OBSERVE:
                history = self.experience_replay()
                acclist.append(history['accuracy'])
                lostlist.append(history['loss'])

            # 训练次数
            if step_index > 500:
                break

            # 如果状态为游戏结束，那么就随机生成一个状态
            if done:
                current_state = np.random.randint(0, action_num - 1)
            else:
                current_state = next_state

            step_index += 1
            if step_index % 100 == 0:
                print("current step:{}".format(step_index))
                print(self.model.predict(action_list))

    def test(self):
        """
        运行并测试。
        :return:
        """
        # 首先进行训练
        self.train()
        plt.plot(acclist, color='green')
        plt.plot(lostlist, color='red')
        plt.show()

        # 每个房间都走一遍，尝试走到5号房间
        for index in range(5):

            start_room = index

            print("#############################", "Agent 在", start_room, "开始行动", "#############################")

            current_state = start_room

            step = 0

            target_state = 5

            while current_state != target_state:
                out_result = self.model.predict(state_list[current_state:current_state + 1])
                # print(out_result)

                next_state = np.argmax(out_result[0])
                # print(next_state)

                print("Agent 由", current_state, "号房间移动到了", next_state, "号房间")

                current_state = next_state

                step += 1

            print("Agent 在", start_room, "号房间开始移动,移动了", step, "步到达了目标房间 5")

            print("#############################", "Agent 在", 5, "结束行动", "#############################")
            return 1


# if __name__ == "__main__":
#     DQN = DeepQNetwork()
#     DQN.test()


DQN = DeepQNetwork()
DQN.test()