#!/usr/bin/env python
import sys
import os
import traceback
import subprocess
import threading
import time
import json
import asyncio
import websockets

try:
    from lang import *
except Exception as e:
    try:
        from .lang import *
    except Exception as ee:
        from docrun.lang import *
        pass
    pass

try:
    import psutil
except Exception as e:
    pass

import jupyter_client



server_address  = "127.0.0.1"
port_kernel     = 5595 

INFO            = {'quit':False}
GLOBALVAR       = {}
KERNELS         = {}
MANAGERS        = {}
THREADS         = {}

INFO['Kernels'] = jupyter_client.kernelspec.find_kernel_specs()

def close_jupyter_kernel(page_id,langs):
    print('try quit kernels for page ', page_id)
    INFO[page_id+"quit"] = True
    for lang in langs:
        if MANAGERS.get(page_id+lang):
            print("#############\nquit kernel ", page_id+lang, "\n#############")
            MANAGERS[page_id+lang].shutdown_kernel()
            GLOBALVAR[page_id+'status_'+lang] = 'idle'
            GLOBALVAR[page_id+'status_in_'+lang] = 'done'
            INFO[page_id+'kernel_status_'+lang] = lt("Stoped")
            pass
        pass
    pass

async def request_processing(websocket, path ):

    def msg_stdin(lang='python3', page_id='0'):
        async def task():
            print(page_id, "stdin thread started" )
            sys.stdout.flush()
            ready_count = 0
            while True:
                if INFO['quit']: 
                    print(page_id, "stdin loop quit for global quit")
                    return
                if INFO[page_id+"quit"]: 
                    print(page_id, "stdin loop quit for page quit")
                    return
                try:
                    time.sleep(0.005)
                    #time.sleep(1.001)
                    #print("stdin msg status: ",GLOBALVAR[page_id+'status_in_'+lang])
                    if not GLOBALVAR[page_id+'status_in_'+lang] in ['ready']:
                        ready_count = 0
                        time.sleep(0.05)
                        continue
                    ready_count += 1
                    if ready_count < 5: continue 
                    #print("waiting for stdin msg",GLOBALVAR[page_id+'status_in_'+lang])
                    sys.stdout.flush()
                    msg = KERNELS[page_id+lang].get_stdin_msg()
                    cont = msg['content']
                    cont['name'] = 'stdin'
                    #print( 'stdin message:', cont )

                    await GLOBALVAR[page_id+'websocket'].send(json.dumps(cont) )

                    # KERNELS[page_id+lang].input('999')
                    #print("request frontend to return an input")
                    sys.stdout.flush()
                    GLOBALVAR[page_id+'status_in_'+lang] = 'waiting'
                    pass
                except Exception as e:
                    print(page_id, "msg stdin loop break for ", e )
                    #traceback.print_exc()
                    #break
                    pass
                pass
            print(page_id, "stdin thread quit" )
            pass
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop( new_loop )
        loop = asyncio.get_event_loop()
        loop.run_until_complete( asyncio.gather( task() ) )
        loop.run_forever()
        pass

    def msg_control(lang='python3', page_id='0'):
        async def task():
            print(page_id, "control thread started")
            sys.stdout.flush()
            while True:
                if INFO['quit']: 
                    print(page_id, "control loop quit for global quit")
                    return
                if INFO[page_id+"quit"]: 
                    print(page_id, "control loop quit for page quit")
                    return
                try:
                    time.sleep(0.01)
                    msg = KERNELS[page_id+lang].get_control_msg()
                    cont = msg.get('content')
                    #print( 'control message:', cont )
                    await GLOBALVAR[page_id+'websocket'].send(json.dumps(cont) )

                    sys.stdout.flush()
                except Exception as e:
                    print(page_id, "msg control loop break for ", e)
                    #traceback.print_exc()
                    #break
                    pass
                pass
            print(page_id, "control thread quit")
            pass
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop( new_loop )
        loop = asyncio.get_event_loop()
        loop.run_until_complete( asyncio.gather( task() ) )
        loop.run_forever()
        pass

    def msg_shell(lang='python3', page_id='0'):
        async def task():
            print(page_id, "shell thread started")
            sys.stdout.flush()
            while True:
                if INFO['quit']: 
                    print(page_id, "shell loop quit for global quit")
                    return
                if INFO[page_id+"quit"]: 
                    print(page_id, "shell loop quit for page quit")
                    return
                try:
                    time.sleep(0.005)
                    if GLOBALVAR[page_id+'status_'+lang] in ['idle']:
                        #print("idle wait")
                        #sys.stdout.flush()
                        time.sleep(0.05)
                        continue
                    sys.stdout.flush()
                    msg = KERNELS[page_id+lang].get_shell_msg()
                    cont = msg.get('content')
                    #print( 'shell message:', cont )
                    # if cont.get('status') == 'ok':

                    time.sleep(0.5)
                    GLOBALVAR[page_id+'status_'+lang] = 'idle'
                    GLOBALVAR[page_id+'status_in_'+lang] = 'done'

                    #await GLOBALVAR['websocket'].send(json.dumps(cont) )

                    sys.stdout.flush()
                    pass

                except Exception as e:
                    print(page_id, "msg shell loop break for ", e)
                    #traceback.print_exc()
                    #break
                    pass
                pass
            print(page_id, "shell thread quit")
            pass
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop( new_loop )
        loop = asyncio.get_event_loop()
        loop.run_until_complete( asyncio.gather( task() ) )
        loop.run_forever()
        pass

    def msg_iopub(lang='python3', page_id='0'):
        async def task():
            print(page_id, "iopub thread started")
            sys.stdout.flush()
            while True:
                if INFO['quit']: 
                    print(page_id, "iopub loop quit for global quit")
                    return
                if INFO[page_id+"quit"]: 
                    print(page_id, "iopub loop quit for page quit")
                    return
                try:
                    time.sleep(0.005)
                    if GLOBALVAR[page_id+'status_'+lang] in ['idle']:
                        #print("idle wait")
                        sys.stdout.flush()
                        time.sleep(0.1)
                        #continue
                    if GLOBALVAR[page_id+'status_'+lang] == 'busy':
                        GLOBALVAR[page_id+'status_'+lang] = 'processing'


                    #print("waiting for iopub msg",GLOBALVAR[page_id+'status_'+lang])
                    sys.stdout.flush()
                    msg = KERNELS[page_id+lang].get_iopub_msg()
                    cont = msg.get('content')
                    #print( 'iopub message:', cont )
                    await GLOBALVAR[page_id+'websocket'].send(json.dumps(cont) )

                    sys.stdout.flush()
                    # GLOBALVAR[page_id+'status_'+lang] = ( cont.get('execution_state') or
                    #                        GLOBALVAR[page_id+'status_'+lang] )
                    # if GLOBALVAR[page_id+'status_'+lang] == 'idle': # set stdin to done
                    #     GLOBALVAR[page_id+'status_in_'+lang] = 'done'

                except Exception as e:
                    print(page_id, "msg iopub loop for error:", e)
                    #traceback.print_exc()
                    #break
                    pass

                pass
            print(page_id, "iopub thread quit")
            pass
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop( new_loop )
        loop = asyncio.get_event_loop()
        loop.run_until_complete( asyncio.gather( task() ) )
        loop.run_forever()
        pass

    def start_kernel(lang="python3", page_id='0'):
        print("try start kernel ",lang, ' for page ', page_id)
        sys.stdout.flush()
        MANAGERS[page_id+lang], KERNELS[page_id+lang] = jupyter_client.manager.start_new_kernel(
            kernel_name = lang
        )
        print(lang, " kernel started for page ",page_id)
        sys.stdout.flush()
        pass

    async def request():
        #print("\nsocket loop started")
        page_id = '0_'
        langs   = []
        while True:
            if INFO['quit']: return
            try:
                res = json.loads( await websocket.recv() )
                #print('get input request: ',res)
                mtype    = res.get('type','')
                lang     = res.get('language','')
                page_id  = res.get('page_id','0')+"_"

                if not lang in langs: langs.append( lang )

                GLOBALVAR[page_id+'websocket'] = websocket

                timer = INFO.get(page_id+"quit_timer",None)
                if timer:
                    print(page_id, " reconnecting, do not kill")
                    timer.cancel()
                    INFO[page_id+"quit_timer"] = None

                if mtype == "info_kernels":
                    #print("web request kernels")
                    for name in INFO['Kernels']:
                        INFO['Kernels'][name] = jupyter_client.kernelspec.get_kernel_spec(name).display_name
                        pass
                    await websocket.send('{"name":"kernels","kernels":'+json.dumps(INFO['Kernels'])+'}')
                    continue

                if not lang or not INFO['Kernels'].get(lang):
                    await websocket.send('{"name":"none_kernel","language":"'+lang+'"}')
                    await websocket.send('{"execution_state":"idle"}')
                    continue
                    pass

                if mtype == 'operate':
                    oper = res.get('operation')
                    if oper == "restart": # try  stop kernel
                        print("try to restart kernel for", lang)
                        MANAGERS[page_id+lang].restart_kernel()
                        continue
                    elif oper == "interrupt": # try  stop kernel
                        print("try to interrupt kernel for", lang)
                        MANAGERS[page_id+lang].interrupt_kernel()
                        continue
                    elif oper == "stop": # try  stop kernel
                        print("try to stop kernel for", lang)
                        MANAGERS[page_id+lang].shutdown_kernel()
                        INFO[page_id+'kernel_status_'+lang] = lt("Stoped")
                        continue
                    elif oper == "readmore": # try  stop kernel
                        #print("more should read from iopub", lang)
                        GLOBALVAR[page_id+'status_in_'+lang] = 'processing'
                        continue
                    print("unknown operation:",oper)
                    continue
                elif mtype == 'input': 
                    if not KERNELS[page_id+lang]:
                        #print("input request back, but no kernel exists, just abort")
                        continue
                    instr = res.get('input')
                    #print("send input str",instr, "as input. mark stdin ready")
                    KERNELS[page_id+lang].input(instr)
                    GLOBALVAR[page_id+'status_in_'+lang] = 'ready'
                    continue
                elif mtype == 'evaluate':
                    #print("normal input code")
                    instr = res.get('code')
                    if not MANAGERS.get(page_id+lang):
                        print( lt("Kernel {0} is not started. Try start...",page_id+lang) )
                        try:
                            start_kernel(lang, page_id)
                        except Exception as e:
                            errs = "start kernel failed for: {0}".format(e)
                            print(errs)
                            await websocket.send(
                                '{"name":"kernel-start-error","text":"'+errs+'"}')
                            traceback.print_exc()
                            continue
                            pass

                        GLOBALVAR[page_id+'status_'+lang] = 'idle'
                        GLOBALVAR[page_id+'status_in_'+lang] = 'done'
                        INFO[ page_id+"quit" ] = False

                        THREADS[page_id+lang] = {}
                        THREADS[page_id+lang]['iopub'] = threading.Thread(
                            target=msg_iopub, args=([lang,page_id]))
                        THREADS[page_id+lang]['iopub'].start()

                        THREADS[page_id+lang]['stdin']=threading.Thread(
                            target=msg_stdin, args=([lang,page_id]) )
                        THREADS[page_id+lang]['stdin'].start()

                        THREADS[page_id+lang]['shell']=threading.Thread(
                            target=msg_shell, args=([lang,page_id]) )
                        THREADS[page_id+lang]['shell'].start()


                        # THREADS[page_id+lang]['control']=threading.Thread(
                        #     target=msg_control, args=([lang,page_id]) )
                        # THREADS[page_id+lang]['control'].start()

                        time.sleep(0.001)
                        pass
                    while not KERNELS[page_id+lang]:
                        #print("wait for kernel to be ready")
                        time.sleep(0.05)
                        continue
                    if not MANAGERS[page_id+lang].is_alive():
                        print("kernel is not alive. Try restart")
                        MANAGERS[page_id+lang].restart_kernel()
                        pass
                    while not MANAGERS[page_id+lang].is_alive():
                        #print("wait for kernel to be alive")
                        time.sleep(0.05)
                        continue
                        pass
                    try:
                        #print("send input to kernel",KERNELS[page_id+lang] )
                        KERNELS[page_id+lang].execute( instr,
                                          silent=False,
                                          store_history=False,
                                          allow_stdin=True,
                        )
                        INFO[page_id+'kernel_status_'+lang] = lt("running")
                        GLOBALVAR[page_id+'status_'+lang]      = 'msgexec'
                        GLOBALVAR[page_id+'status_in_'+lang]   = 'ready'
                    except Exception as e:
                        print("kernel execution error:",e)
                        traceback.print_exc()
                        pass
                    pass
                else:
                    print('unknown request message:', res)
                    continue
                pass
            except Exception as e:
                print("request loop quit for ",e)
                #traceback.print_exc()
                print("will close kernels for ", page_id,' in 10s')
                INFO[page_id+'quit_timer'] = threading.Timer(10.0, close_jupyter_kernel,[page_id, langs])
                INFO[page_id+'quit_timer'].start()
                break
            pass
        pass



    request_task = asyncio.create_task( request() )
    await request_task

    pass

def run_server(): # in non-main thread
    #print("kernels : ", INFO['Kernels'])
    print("starting server for local kernel on port",port_kernel)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop( loop )
    loop = asyncio.get_event_loop()

    try:
        server = websockets.serve(request_processing, server_address, port_kernel)
        loop.run_until_complete( server )
        loop.run_forever()
    except Exception as e:
        print("quit with error:", e)
        pass
    #print("task assigned")
    pass

def stop_server(lang='python'):
    print("try stop server",)
    pass

#run_server()

def check_parent_pid():
    if not psutil: return
    while True:
        if not psutil.pid_exists( INFO['parent_pid'] ):
            print("no parent found. Quiting...")

            INFO['quit'] = True
            os._exit(1)
            pass
        time.sleep(0.05)
        pass

    pass
            

if __name__  == "__main__":
    #print('run server with argv:',sys.argv)
    try:
        INFO['parent_pid'] = int(sys.argv[-1])
        check = threading.Thread(target=check_parent_pid)
        check.start()
    except:
        INFO['parent_pid'] = -1
        print("not launched by parent process in manner")
        pass

    run_server()

