# 定义一个结点
class QueueNode:
    def __init__(self):
        self.data = None
        self.next = None

# 定义一个链式队列
class LinkQueue:
    # 初始化
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode

    # 判断队列是否为空
    def IsEmptyQueue(self):
        if self.front ==self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    # 入队的函数
    def EnQueue(self,data):
        # 创建新结点
        tQueueNode = QueueNode()
        tQueueNode.data = data
        # 链接到队尾
        self.rear.next = tQueueNode
        # 修改rear
        self.rear = tQueueNode
        print("当前进队的元素为：",data)


    """
    队：
    1、队列里有没有数据 front==rear
    没有数据（空）
    队列为空，无法出队
    2、队列里有1个数据
    if self.front.next.next = None:
            self.front.next = None
            self.reat = self.front
    3、队列里有2个或以上数据
            tNode = self.front.next
            self.front == tNode.next
            return tNode.data
    """

    # 出队的函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        elif self.front.next.next == None:
            self.front.next = None
            self.rear = self.front
        else:
            tQueueNode = self.front.next
            self.front.next = tQueueNode.next
            return tQueueNode.data



