def sol():
    print('5次失敗就會退出遊戲')
    fail_count=0
    string=''
    while string=='':
        string=input(f'請輸入一個字串:\n')
    while fail_count<5:
        print(f'上一個字串是{string}')
        new_string=input(f'請輸入-{string[-1]}-開頭的字串(失敗次數{fail_count}次):\n')
        if new_string=='':
            continue
        elif new_string[0]!=string[-1]:
            fail_count+=1
            continue
        string=string+'-'+new_string
    print('遊戲結束')