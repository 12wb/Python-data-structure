class SeqList:  # 定义顺序表类

    def __init__(self):   # 构造函数，初始化对象
       self.SeqList = []   # 创建空间

     # 创建顺序表函数

    def CreateSequenceList(self):
        print("**********")
        print('*请输入数据后回车确认，若想结束请输入#。*')
        print('**********')
        Element = input('请输入:')
        while Element != '#':
          self.SeqList.append(int(Element))
          Element = input('请输入元素:')

    def delete(self):
        print()
