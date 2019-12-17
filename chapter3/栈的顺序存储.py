# 栈的顺序存储
# 栈的初始化
class SequenceStack:
    def __init__(self):
        self.MaxStrackSize = 10    # 最大存储单元个数
        self.s = [None for x in range(0,self.MaxStrackSize)]
        self.top = -1

# 输出当前栈长度
    def GetStackLength(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            return self.top+1

# 判断栈是否为空
    def IsEmptyStack(self):
        if self.top == -1:
            itop = True
        else:
            itop = False

# 通过输入元素创建一个顺序栈
    def CreatStackByInput(self):
        data = input('请输入元素，以#结束输入:')
        while data!='#':
            self.PushStack(data)
            data = input('请继续输入元素，以#结束输入：')

# 入栈函数
    def PushStack(self,x):
        if self.top < self.MaxStrackSize-1:
            self.top = self.top+1
            self.s[self.top] = x
        else:
            print('栈满')
            return

# 出栈函数
    def PopStach(self):
        if self.IsEmptyStack():
            print('栈空')
            return
        else:
            itop = self.top
            self.top = self.top-1
            return self.s[itop]

# 遍历栈内元素
    def StcakTrave(self):
        if self.IsEmptyStack():
            print('栈空')
            return
        else:
            for i in range(0,self.top+1):
                print(self.s[i],end='')

# 编写测试函数
ss = SequenceStack()
ss.CreatStackByInput()
ss.StcakTrave()
ss.PopStach()
ss.StcakTrave()