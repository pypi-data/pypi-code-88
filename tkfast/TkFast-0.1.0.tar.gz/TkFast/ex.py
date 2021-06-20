from __init__ import *
def ex_1():
    ch = []
    questions = ["我们讨论并阅读了一部名著。","听了他一句话，改变了一生"
        ,"我可能是女生。","全国人民都万分悲痛。"]
    get_choose(ch,question="请选择没有语病一项。",label="选择",canclose=False,chooses=questions)
    if ch[0] == 3:
        show_alert("答对了！","Yes")
    else:
        show_alert("答错了！","No")
if __name__ == '__main__':
    ex_1()