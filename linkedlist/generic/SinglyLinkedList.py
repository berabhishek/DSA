class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, arr):
        self.root = Node(arr[0])
        cursor = self.root
        for element in arr[1:]:
            cursor.next = Node(element)
            cursor = cursor.next
        
    def getRoot(self):
        return self.root

    #returns the length of the linkedlist
    def getLength(self) -> int:
        """Returns the length of the linkedlist"""
        length = 0
        cursor = self.root
        while cursor is not None:
            length += 1
            cursor = cursor.next
        return length
    
    def getMiddle(self) -> Node:
        """Get the middle node of the linkedlist."""
        fast = self.root
        slow = self.root
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def removeMiddle(self) -> Node:
        """Removes the middle node of the linkedlist"""
        pass

    def sortAscending(self):
        """Sorts the linked list into ascending order."""
        pass

    def sortDescending(self):
        """Sorts the linkedlist into descending order."""
        pass

    def searchElement(self):
        """Searches the element in the linkedlist."""
        pass

    def isSortedAscending(self) -> bool:
        """Checks if the linked list in ascending sorted order."""
        flag = True
        cursor = self.root
        while cursor.next is not None:
            if cursor.data > cursor.next.data: 
                return False
            cursor = cursor.next
        return flag

    def isSortedDescending(self) -> bool:
        """Checks if the linked list in descending sorted order."""
        flag = True
        cursor = self.root
        while cursor.next is not None:
            if cursor.data < cursor.next.data:
                return False
            cursor = cursor.next
        return flag

    def reverse(self):
        """Reverses a linked list."""
        first_pointer = None
        second_pointer = self.root
        third_pointer = second_pointer.next
        while third_pointer is not None:
            second_pointer.next = first_pointer
            first_pointer = second_pointer
            second_pointer = third_pointer
            third_pointer = third_pointer.next
        second_pointer.next = first_pointer
        self.root = second_pointer

    def removeElementFromIndex(self, index = 0):
        """Removes element from the linked list from the given index"""
        pass

    def insertElementAtIndex(self, element, index = 0):
        """Inserts element at the given index"""
        pass

    def insertIntoSorted(self, element):
        """Inserts into sorted linkedlist while maintaining the sort order, assumes the linkedlist is already sorted"""
        pass

    def removeFromSorted(self, element):
        """Removes an element from the sorted linkedlist"""
        pass

    def rotate(self, rotation):
        """Rotate a sorted linkedlist by given number."""
        pass

    def getRotation(self) -> int:
        """Finds the rotation of the sorted linkedlist."""
        pass

    def binarySearch(self, element) -> Node:
        """Binary search and return the node. Linked list can be ascending or descending sorted"""
        pass

    def toList(self) -> list:
        """Returs a python list of the linked list"""
        returnArr = []
        cursor = self.root
        while cursor is not None:
            returnArr.append(cursor.data)
            cursor = cursor.next
        return returnArr