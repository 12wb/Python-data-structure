#########################
#  初始化顺序表函数
#########################
class SeqList:  # 定义顺序表类

    def __init__(self):   # 构造函数，初始化对象
       self.SeqList = []   # 创建空间

     # 创建顺序表函数

    def CreateSequenceList(self):
        print("**********")
        print('*请输入数据后回车确认，若想结束请输入#。*')
        print('**********')
        Element = input('请输入元素:')
        while Element != '#':
          self.SeqList.append(int(Element))
          Element = input('请输入元素:')

# 查找
    def FindElement(self):
        key = int(input('请输入想要查找的值:'))
        if key in self.SeqList:
            ipos = self.SeqList.index(key)
            print("查找成功！值为:", self.SeqList[ipos], "的元素，位于当前顺序表的第", ipos + 1, "个位置。")
        else:
            print('查找失败！当前顺序表中不存在值为"key"的元素')

# 插入
    def InsertElement(self):
        ipos = int(input("请输入待插入元素的位置："))
        Element = int(input("请输入待插入的值："))
        self.SeqList.insert(ipos,Element)
        print("插入元素后， 当前顺序表为：\n",self.SeqList)

# 删除
    def DeleteElement(self):
        dpos = int(input("请输入待删除的元素："))
        print("正在删除元素",self.SeqList[dpos])
        self.SeqList.remove(self.SeqList[dpos])
        print("删除后顺序表为:\n",self.SeqList)
# 遍历
    def TraverseElement(self):
        SeqListLen = len(self.SeqList)
        print("******遍历顺序表中元素******")
        for i in range(0,SeqListLen):
            print("第",i+1,"个元素的值为",self.SeqList[i])


# 求顺序表的最值函数
    def GetExtremm(self):
        while True:
            print("***************************************")
            print("*1:查询最大值")
            print("*2:查询最小值")
            print("*3:查询最大值和最小值")
            print("*0:退出程序")
            print("***************************************")
            i = int(input("请输入:"))
            if i == 1:
                print("顺序表最大值为：",max(self.SeqList))
            elif i == 2:
                print("顺序表最小值为：",min(self.SeqList))
            elif i == 3:
                print("顺序表最大值为：", max(self.SeqList))
                print("顺序表最小值为：", min(self.SeqList))
            elif i == 0:
                break
    def SetSequenceList(self):
        print("删除重复元素", list(set(self.SeqList)))

    def x(self):
        print("转置", self.SeqList[::-1])


if __name__ == '__main__':
   seqlist = SeqList ()
   seqlist.CreateSequenceList()  # 创建顺序表
   seqlist.FindElement()
   seqlist.InsertElement()
   seqlist.DeleteElement()
   seqlist.TraverseElement()
   seqlist.GetExtremm()
   seqlist.SetSequenceList()
   seqlist.x()
