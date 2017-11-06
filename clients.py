# -*- coding: UTF-8 -*-
__author__ = 'Chiachyi'
__time__ = '2017年11月6日 13:18:09'
__idea__ = ''
__future__ = '实现对话实时传输'

import websocket
import _thread
import time
def talkfo():
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:9001/")
    print("正在连接服务器....")
    print("目前只能讲英文....")
    ws_input = input("我想说：")
    ws.send(ws_input)
    print(ws_input,"已收到")
    #print("Receiving...")
    # result = ws.recv()
    # print("Received '%s'" % result)
    #ws.close()
    return

'''
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9001/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
'''


