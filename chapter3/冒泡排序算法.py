###################################
# 冒泡排序:原理就是重复的进行 两两 元素之间的比较
# （冒泡的意思就是左右之间的比较元素）
class ListItem(object):
    def __init__(self ,key,value):
        self.key = key
        self.value = value
class SortSequenceList(object):
    def __init__(self):
        self.SeqList=[]
    def  CreateSequenceListByInput(self,nElement):
        self.SeqList.append(ListItem(int(0), 0))
        print("请输入数据：")
        for i in range(1,nElement+1):
            a = input()
            self.SeqList.append(ListItem(int(a), i))
    def TraverseElementSet(self):
        for i in range(1,len(self.SeqList)):
            print(self.SeqList[i].key)

    ########################
    #算法8-7 冒泡排序算法
    ########################
    def BubbleSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(1,SeqListLen-1):
            for j in range(1,SeqListLen-i):
                print("j=",j)
                if self.SeqList[j+1].key < self.SeqList[j].key:
                    self.SeqList[0].key = self.SeqList[j].key
                    self.SeqList[j].key = self.SeqList[j+1].key
                    self.SeqList[j+1].key = self.SeqList[0].key
            self.TraverseElementSet()

if __name__ =='__main__':
    SL=SortSequenceList()
    SL.CreateSequenceListByInput(7)
    SL.BubbleSort()
    print('排序算法结果为:')
    SL.TraverseElementSet()
