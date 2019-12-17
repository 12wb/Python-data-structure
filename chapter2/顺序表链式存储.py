class Node(object):  # 定义一个超类
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):  # 创建单链表类
    def __init__(self):
        self.head = Node(None)

    def CreateSingleLinked(self):
        Cnode = self.head
        Element = input("请输入数据")
        while Element != "#":
            nNode = Node(int(Element))
            Cnode.next = nNode  # 头结点的下一个节点指向头结点
            Cnode = Cnode.next  # 头结点指向下一个节点
            #Cnode.next = nNode         # 循环单链表
            #nNode.next = self.head.next
            #Cnode = Cnode.next

            Element =input("请继续输入")

    def TraverseElement(self):
        Cnode = self.head
        if Cnode.next == None:
            print("当前链表为空!")
            return
        print("当前链表为:")
        while Cnode != None:
            Cnode = Cnode.next
            self.visitElement(Cnode)

    def visitElement(self,tNode):
        if tNode != None:
            print(tNode.data,"-<",end="")
        else:
            print("none")

    def InsertElementHead(self):
        Element = input("请输入新插入首端元素")
        while Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def InsertElementTail(self):
        Element = input("请输入新插入尾端元素")
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode

    def DeleteElement(self):
        Element = input("请输入删除的节点")
        pNode = self.head
        cNode = self.head
        if self.isEmpty(cNode):
            print("当前链表为空")
            return
        while cNode.next != None and cNode.data != Element:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == Element:
            pNode.next = cNode.next
            del cNode
            print("删除成功")
        else:
            print("删除失败")
    def isEmpty(self,t):
        if t.next==None:
            return True


LinkList = SingleLinkedList()
LinkList.CreateSingleLinked()
LinkList.TraverseElement()
LinkList.InsertElementHead()
LinkList.TraverseElement()
LinkList.InsertElementTail()
LinkList.TraverseElement()
LinkList.DeleteElement()
LinkList.TraverseElement()
LinkList.isEmpty()
