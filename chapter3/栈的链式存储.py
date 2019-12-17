# # 栈的链式存储
# # 栈的初始化
# class LinkStack:
#     def __init__(self):
#         self.top = StackNode()
#
# # 初始化结点
# class StackNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
#
#
# # 判断链栈是否为空
#     def IsEmptyStack(self):
#         if self.top.next == None:
#             itop = True
#         else:
#             itop = False
#
# # 通过输入元素创建一个链栈
#     def CreatStackByInput(self):
#         data = input('请输入元素，以#结束输入:')
#         while data!='#':
#             self.PushStack(data)
#             data = input('请继续输入元素，以#结束输入：')
#
# # 入栈函数
#     def PushStack(self,da):
#         tStackNode = StackNode()
#         tStackNode.data = da
#         tStackNode.next = self.top.next
#         self.top.next = tStackNode
#         print("当前入栈的元素为：",da)
#
# # 出栈函数
#     def PopStach(self):
#         if self.IsEmptyStack() == True:
#             return
#         else:
#             tStackNode = self.top.next
#             self.top.next = tStackNode.next
#             return tStackNode.data
#
# # 遍历栈内元素
#     def StcakTrave(self):
#         if self.IsEmptyStack():
#             print('栈空')
#             return
#         else:
#             for i in range(0,self.top+1):
#                 print(self.s[i],end='')
#
# # 编写测试函数
# st = LinkStack()
# st.CreatStackByInput()
# st.StcakVisit()
# st.PopStach()
# st.StcakTrave()

class StackNode:
    def __init__(self):
        self.data = None
        self.next = None
class LinkStack:
    def __init__(self):
        self.top = StackNode()
    '''判断链栈是否为空'''
    def IsEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop
    '''进栈'''
    def PushStack(self,da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
        print("当前入栈的元素为：",da)
    '''出栈'''
    def PopStack(self):
        if self.IsEmptyStack() == True:
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data
    '''获取栈顶元素'''
    def GetTopStack(self):
        if self.IsEmptyStack() == True:
            print("栈为空")
        else:
            return self.top.next.data
    '''创建一个链栈'''
    def CreateStackByInput(self):
        data = input("请输入元素（确定按回车键，结束按“#”）：")
        while data != "#":
            self.PushStack(data)
            data = input("请输入元素（确定按回车键，结束按“#”）：")
    def StackVisit(self):
        element = input("请输入要寻找的元素：")
        i = 0
        tStackNode = self.top
        result = self.PopStack()
        while tStackNode.next!= None and element != result:
            tStackNode = tStackNode.next
            result = self.PopStack()
            i += 1
        if element == result:
            print("已找到，距栈顶",i,"个位置")
        else:
            print("链栈中无此元素")
Ls = LinkStack()
Ls.CreateStackByInput()
Ls.StackVisit()

