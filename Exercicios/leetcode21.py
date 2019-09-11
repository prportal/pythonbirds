# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
        pos = 0
        if len(l1) == 0:
            return(l2)
        if len(l2) == 0:
            return(l1)
        lresult = []
        print(l1, l2)
        while len(l1) > 0 and len(l2) > 0:
            if l1[0] == l2[0]:
                lresult.append(l1[0])
                lresult.append(l2[0])
                l1.pop(0)
                l2.pop(0)
            elif l1[0] > l2[0]:
                lresult.append(l2[0])
                l2.pop(0)
            else:
                lresult.append(l1[0])
                l1.pop(0)
##
        if len(l1) > 0:
            while len(l1) > 0:
                lresult.append(l1[0])
                l1.pop(0)
        else:
             while len(l2) > 0:
                lresult.append(l2[0])
                l2.pop(0)
        return(lresult)

##L1 = [1, 7]
##L2 = [1, 3, 4]
##L1 = [1, 3, 4, 6, 7]
##L2 = [1, 3, 4]
L1 = [1,2,4]
L2 = [1,3,4]

s = Solution()
print(s.mergeTwoLists(L1, L2))
