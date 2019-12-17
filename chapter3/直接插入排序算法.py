# 算法8-1 初始化结点方法
#######################
class ListItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class SortSequenceList(object):
    def __init__(self):
        self.SeqList = []

    def CreateSequenceListByInput(self, nElement):
        self.SeqList.append(ListItem(int(0), 0))
        print("请输入数据：")
        for i in range(1, nElement + 1):
            a = input()
            self.SeqList.append(ListItem(int(a), i))

    def TraverseElementSet(self):
        for i in range(1, len(self.SeqList)):
            print(self.SeqList[i].key)

    #############################
    # 算法8-2 直接插入排序
    #############################
    def InsertSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(2, SeqListLen):
            self.SeqList[0].key = self.SeqList[i].key
            index = i
            while self.SeqList[index - 1].key > self.SeqList[0].key:
                self.SeqList[index].key = self.SeqList[index - 1].key
                index = index - 1
            self.SeqList[index].key = self.SeqList[0].key


if __name__ == '__main__':
    SL = SortSequenceList()
    SL.CreateSequenceListByInput(5)
    SL.InsertSort()
    print('插入排序算法结果为:')
    SL.TraverseElementSet()


# 定义插入排序函数
def insertion_sort(list):
    # 获取需要排序数据的个数
    N = len(list)
    # 插入排序的第一次插入从第二个数字开始选择，所以下标从1开始
    for i in range(1, N):
        # 从选择插入的数据，一次和它前一个比较，主要比前面的小就交换
        for j in range(i, 0, -1):
            # 判断大小
            if list[j] < list[j - 1]:
                # 交换
                temp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = temp


numlist = [19, 2, 13, 8, 34, 25, 7]
print("排序前：%s" % numlist)
insertion_sort(numlist)
print("排序后：%s" % numlist)