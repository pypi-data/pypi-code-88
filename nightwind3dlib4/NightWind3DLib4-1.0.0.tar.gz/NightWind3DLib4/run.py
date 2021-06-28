from direct.directbase.DirectStart import base
from direct.showbase.ShowBaseGlobal import globalClock
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import *
from NightWind3DLib4.Actor import Character
import random


class Window:
    def __init__(self):
        # 窗体初始化
        self.base = base
        self.window = WindowProperties()
        self.window.setTitle("Run")
        self.window.setSize(600, 800)
        self.base.win.requestProperties(self.window)
        self.base.disableMouse()
        self.base.setBackgroundColor(0 / 255, 128 / 255, 255 / 255)

        # 设置玩家
        self.player = Character(ModelName="actor",
                                AnimsName={"jump": "actor_jump",
                                           "down": "actor_down"},
                                pos=(0, -9960, 5),
                                ColliderName="player")

        # 设置地面
        self.floor = loader.loadModel("ground")
        self.floor.reparentTo(render)

        # 记录时间
        self.total_time = 0
        self.last_spawn_time = 0
        self.last_speedup_time = 0
        self.spawn_time = 0.8
        self.least_spawn_time = 0.5

        # 调整速度
        self.speed = 1
        self.max_speed = 3

        # 调整角度
        self.base.cam.setPos(0, -10015, 45)
        self.base.cam.setHpr(0, -30, -2)

        self.spawned = []

        # 设置键盘状态
        self.KeyStates = {"right": False, "left": False, "middle": True,
                          "changing_right": False, "changing_left": False,
                          "jump": False, "roll": False}

        # 键盘事件
        self.KeyEvent()

        # 将任务添加到任务管理器中
        taskMgr.add(self.update)

    def KeyEvent(self):
        # 捆绑和捕捉键盘事件
        self.base.accept("w", self.ChangeKeyState, ["jump", True])
        self.base.accept("w-up", self.ChangeKeyState, ["jump", False])
        self.base.accept("s", self.ChangeKeyState, ["roll", True])
        self.base.accept("s-up", self.ChangeKeyState, ["roll", False])
        self.base.accept("a", self.ChangeKeyState, ["changing_left", True])
        self.base.accept("d", self.ChangeKeyState, ["changing_right", True])

    def ChangeKeyState(self, action, state):
        self.KeyStates[action] = state
        taskMgr.add(self.ChangeRoad)

    def ChangeRoad(self, task):
        if self.KeyStates["changing_left"]:
            # 玩家试图向左切换跑道
            self.KeyStates["changing_left"] = False

            if self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于左边的跑道
                pass

            elif not self.KeyStates["left"] and \
                    self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于中间的跑道
                self.KeyStates["left"] = True
                self.KeyStates["middle"] = False

            elif not self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    self.KeyStates["right"]:

                # 玩家位于右边的跑道
                self.KeyStates["middle"] = True
                self.KeyStates["right"] = False

        if self.KeyStates["changing_right"]:
            # 玩家试图向右切换跑道
            self.KeyStates["changing_right"] = False

            if self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于左边的跑道
                self.KeyStates["middle"] = True
                self.KeyStates["left"] = False

            elif not self.KeyStates["left"] and \
                    self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于中间的跑道
                self.KeyStates["right"] = True
                self.KeyStates["middle"] = False

            elif not self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    self.KeyStates["right"]:

                # 玩家位于右边的跑道
                pass

        if self.KeyStates["left"]:
            self.player.actor.setX(-9)
        elif self.KeyStates["middle"]:
            self.player.actor.setX(0)
        elif self.KeyStates["right"]:
            self.player.actor.setX(9)

        return task.done

    def SpawnBlocks(self):
        board = loader.loadModel("roadblock121_forbidden")
        jump1 = loader.loadModel("roadblock111_up")
        jump2 = loader.loadModel("roadblock211_up")
        jumpOrDown = loader.loadModel("roadblock111_updown")
        Blocks = [board, jump1, jump2, jumpOrDown]

        block = random.choice(Blocks)
        if block is jump2:
            x = random.choice([-9, 0])
        else:
            x = random.choice([-9, 0, 9])

        pos = (x, -9820, 5)
        block.reparentTo(render)
        block.setPos(pos)
        return block

    def update(self, task):
        dt = globalClock.getDt()
        self.total_time += dt

        if int(self.total_time) - int(self.last_speedup_time) == 10:
            self.speed += 0.1
            self.last_speedup_time = self.total_time

        if self.speed >= self.max_speed:
            self.speed = self.max_speed

        if self.total_time - self.last_spawn_time >= self.spawn_time:
            block = self.SpawnBlocks()
            self.spawned.append(block)
            self.last_spawn_time = self.total_time

        if int(self.total_time) % 100 == 0 and int(self.total_time) != 0:
            self.spawn_time -= 0.05

        if self.spawn_time <= self.least_spawn_time:
            self.spawn_time = self.least_spawn_time

        for block in self.spawned:
            block.setY(block, -self.speed)
            if block.getY() < -10000:
                self.spawned.remove(block)

        return task.cont


if __name__ == "__main__":
    window = Window()
    window.base.run()
