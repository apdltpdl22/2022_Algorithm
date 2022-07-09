# 회전하는 큐 (단일 연결 리스트 활용)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Left(self, arr):
        count = 0
        find_arr = arr
        HeadVal = self.head

        if (HeadVal is not None) :
            while(HeadVal == self.tail) :
                if (HeadVal.data in find_arr):
                    find_arr.remove(HeadVal.data)

                if (len(find_arr) == 0):
                    return count

                self.tail.next = HeadVal
                HeadVal = HeadVal.next
                count += 1

        return

    def Right(self, arr):
        count = 0
        find_arr = arr
        TailVal = self.tail

        if (TailVal is not None):
            while (TailVal.data == self.head.data):
                if (TailVal.data in find_arr):
                    find_arr.remove(TailVal.data)

                if (len(find_arr) == 0):
                    return count

                TailVal.next = self.head


        return


