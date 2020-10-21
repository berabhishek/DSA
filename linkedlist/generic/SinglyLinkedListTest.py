import unittest
from SinglyLinkedList import SinglyLinkedList
import random

class SinglyLinkedListTestCase(unittest.TestCase):

    def setUp(self):
        """"""
        self.oddUnsortedList = [5,2,3,1,4]
        self.evenUnsortedList = [6,3,4,1,2,5]
        # self.linkedList = SinglyLinkedList()

    def testLinkedListLength(self):
        arr = self.evenUnsortedList
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.getLength() == len(arr))
    
    def testLinkedListOddMiddle(self):
        arr = self.oddUnsortedList
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.getMiddle().data == arr[len(arr)//2])
    
    def testLinkedListEvenMiddle(self):
        arr = self.evenUnsortedList
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.getMiddle().data == arr[len(arr)//2-1] or linkedList.getMiddle().data == arr[len(arr)//2])

    #testing sorting 
    def testIsAscendingSortedPartiallyEndingUnsorted(self):
        arr = [1,2,3,4,5,6,8,7]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.isSortedAscending() == False)
    
    def testIsDescendingSortedPatiallyEndingUnsorted(self):
        arr = [10,9,8,7,6,5,4,11]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.isSortedDescending() == False)
    
    def testIsAscendingSortedFullySorted(self):
        arr = [i for i in range(100)]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.isSortedAscending() == True)

    def testIsDescendingSortedFullySorted(self):
        arr = [i for i in range(100, 0, -1)]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.isSortedDescending() == True)
    
    def testSortedHalfUnsorted(self):
        arr = [i for i in range(100)]
        arr += [i for i in range(100, 0, -1)]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.isSortedAscending() == False and linkedList.isSortedDescending() == False)
    
    #test the tolist
    def testToList(self):
        arr = [random.random() for i in range(100)]
        linkedList = SinglyLinkedList(arr)
        assert(linkedList.toList() == arr)

    #test the reverse
    def testReverseLinkedList(self):
        arr = [5,4,2,1,3,4]
        linkedList = SinglyLinkedList(arr)
        linkedList.reverse()
        assert(linkedList.toList() == arr[::-1])

    def testReverseOneElement(self):
        arr = [5]
        linkedList = SinglyLinkedList(arr)
        linkedList.reverse()
        assert(linkedList.toList() == arr[::-1])

    def testReverseTwoElements(self):
        arr = [5,4]
        linkedList = SinglyLinkedList(arr)
        linkedList.reverse()
        assert(linkedList.toList() == arr[::-1])
    
if __name__ == "__main__":
    unittest.main()