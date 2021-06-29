import screenagent
import configparser
import time

agent = screenagent.ScreenAgent("localhost", 12345)
last_time = 0
config = configparser.ConfigParser()
config.read('config.ini')

while True:
    current_time = time.time()
    if current_time - last_time > int(config['frame']['frequency']):
        agent.send_screenshot("test.bmp")
        last_time = time.time()
