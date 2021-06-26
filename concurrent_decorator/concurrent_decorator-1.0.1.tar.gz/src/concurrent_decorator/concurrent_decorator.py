from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
def mul_threadpool(max_workers = 2,args_list=None):
    def showtime(func):
        executor = ThreadPoolExecutor(max_workers=max_workers)
        def wrapper(*args):
            start_time = time.time()
            # 如果有参数就开启多线程
            if args_list:
                res=[data for data in executor.map(func, args_list)]
            else:
                func(*args)
            end_time = time.time()
            print('work in {} threads, spend time is {}s'.format(max_workers,end_time - start_time))
            return res
        return wrapper
    return showtime

def mul_processpool(max_workers = 2,args_list=None):
    #暂不可用
    def showtime(func):
        executor = ProcessPoolExecutor(max_workers=max_workers)
        def wrapper(*args):
            start_time = time.time()
            # 如果有参数就开启多进程
            if args_list:
                res=[data for data in executor.map(func, args_list)]
            else:
                func(*args)
            end_time = time.time()
            print('work in {} process, spend time is {}s'.format(max_workers,end_time - start_time))
            return res
        return wrapper
    return showtime

if __name__=='__main__':
    # 单参数函数可以直接调用
    @mul_threadpool(max_workers=2,args_list=[1,2,1])  
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times

    print(get_html())

    # 多参数函数丢进字典后使用
    a=[1,1,1]
    b=[0.5,0,1]
    data=[]
    for i in range(len(a)):
        data.append({'a':a[i],'b':b[i]})
    @mul_threadpool(max_workers=2,args_list=data)
    def add(data=None):
        a=data['a']
        b=data['b']
        # print(a,b)
        time.sleep(a+b)
        return a+b
    print(add())


    
