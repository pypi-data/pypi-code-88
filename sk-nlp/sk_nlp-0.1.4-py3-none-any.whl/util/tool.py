# -*- coding: utf-8 -*-
"""
数据结构相关的工具
并查集：求连通图，可用于关联同义词林
ac 自动机：多模式串匹配
有限状态机：多模式串匹配
"""

class UnionFindSet(object):
    """
    并查集

    """
    def __init__(self, nodes):
        """
        初始化并查集

        :param nodes: 传入的节点
        """
        # 记录每个节点的父节点
        self.fatherMap = {}
        # 各门派的人数
        self.setNumMap = {}
        # 初始化, 每个节点自成一派
        for node in nodes:
            self.fatherMap[node] = node
            self.setNumMap[node] = 1

    def findFather(self, node):
        """
        递归逻辑:返回当前节点的父节点; base case:当前节点的父节点是自己

        :param node: 节点
        :return: 父节点
        """
        father = self.fatherMap[node]
        if (node != father):
            father = self.findFather(father)
        # 超级优化: 路径压缩
        self.fatherMap[node] = father
        return father

    def isSameSet(self, a, b):
        """
        判断两个节点a和b是否属于同一门派

        :param a: 节点a
        :param b: 节点b
        :return: True/False
        """

        return self.findFather(a) == self.findFather(b)

    def union(self, a, b):
        """
        合并a所在的集合和b所在的集合

        :param a: 节点a
        :param b: 节点b
        :return: 无
        """
        if a is None or b is None:
            return
        # a的掌门
        aFather = self.findFather(a)
        # b的掌门
        bFather = self.findFather(b)

        if (aFather != bFather):
            # a所在门派的人数
            aNum = self.setNumMap[aFather]
            # b所在门派的人数
            bNum = self.setNumMap[bFather]
            # 人数少的门派加入人数多的门派
            if (aNum <= bNum):
                self.fatherMap[aFather] = bFather
                self.setNumMap[bFather] = aNum + bNum
                self.setNumMap.pop(aFather)
            else:
                self.fatherMap[bFather] = aFather
                self.setNumMap[aFather] = aNum + bNum
                self.setNumMap.pop(bFather)


class Node(object):
    """
    前缀树节点结构
    """

    def __init__(self):
        self.next = {}       #相当于指针，指向树节点的下一层节点
        self.fail = None     #失配指针，这个是AC自动机的关键
        self.isWord = False  #标记，用来判断是否是一个标签的结尾
        self.word = ""       #用来储存标签
        self.prefix_number = 0 #记录前缀
        self.word_number = 0

class Queue(object):
    """
    队列结构
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        判断队列是否为空

        :return: True/False
        """
        return self.items == []

    def enqueue(self, item):
        """
        进队列

        :param item: 队列元素
        :return:
        """

        self.items.insert(0, item)

    def dequeue(self):
        """
        元素出队列

        :return: 队列头元素
        """
        return self.items.pop()

    def get(self):
        """
        返回队列头元素

        :return: 队列头元素
        """
        return self.items[0]

    def size(self):
        """
        返回队列大小

        :return: 队列大小
        """
        return len(self.items)

class AC(object):
    """
    AC 自动机
    """

    def __init__(self):
        self.root = Node()  #定义根节点

    def add(self, word):
        """
        增加模式串

        :param word: 模式串
        :return: 无
        """

        temp_root = self.root
        for char in word:  # 遍历标签的每个字
            if char not in temp_root.next:  # 如果节点下没有这个字，就加入这个字的节点
                node1 = Node()
                node1.prefix_number += 1
                temp_root.next[char] = node1
            temp_root = temp_root.next[char]  # 沿着标签建立字典
        temp_root.isWord = True  # 标签结束，表示从根到这个节点是一个完整的标签
        temp_root.word = word  # 储存这个标签
        temp_root.word_number += 1
        temp_root.prefix_number += 1

    def dfs(self):
        """
        广度优先遍历

        :return: 广度优先遍历顺序得到的列表
        """
        temp_root = self.root
        queue = Queue()
        queue.enqueue(temp_root)
        char_list = []
        while not queue.is_empty():
            temp_root = queue.dequeue()
            for key in temp_root.next:
                char_list.append(key)
                temp = temp_root.next[key]
                queue.enqueue(temp)
        return char_list

    def make_fail(self):
        """
        创建fail指针

        :return: 无
        """
        temp_que = []
        temp_que.append(self.root)
        while len(temp_que) != 0:
            temp = temp_que.pop(0)
            p = None
            for key, value in temp.next.items():
                if temp == self.root:
                    temp.next[key].fail = self.root
                else:
                    p = temp.fail
                    while p is not None:
                        if key in p.next:
                            # temp.next[key].fail = p.fail
                            temp.next[key].fail = p.next[key]
                            break
                        p = p.fail
                    if p is None:
                        temp.next[key].fail = self.root
                temp_que.append(temp.next[key])

    def search(self, content):
        """
        多模式匹配查询

        :param content: 母串
        :return:

        Example
        -------
        >>> ac = AC()
        >>> ac.add('杰伦的七')
        >>> ac.add('周杰伦的')
        >>>ac.add('七里香')
        #看一下构建的前缀树，非必须
        >>> print(ac.dfs())
        ['杰', '周', '七', '伦', '杰', '里', '的', '伦', '香', '七', '的']
        # 构建fail指针
        >>> ac.make_fail()
        >>> result = ac.search('周杰伦的七里香七里香')
        >>> print(result)
        ['周杰伦的', '杰伦的七', '七里香', '七里香']
        """
        p = self.root
        result = []
        currentposition = 0
        flag = 0
        while currentposition < len(content):
            word = content[currentposition]
            while word not in p.next and p != self.root:
                p = p.fail
            if word in p.next:
                p = p.next[word]
            else:
                p = self.root
            if p.isWord:
                result.append(p.word)
            currentposition += 1
        return result

if __name__ == '__main__':
    """
    测试模块是否正常运行
    """
    ac = AC()
    #新增模式串
    ac.add('杰伦的七')
    ac.add('周杰伦的')
    ac.add('七里香')
    #看一下构建的前缀树，非必须
    print(ac.dfs())
    # 构建fail指针
    ac.make_fail()
    result = ac.search('周杰伦的七里香七里香')
    print(result)

