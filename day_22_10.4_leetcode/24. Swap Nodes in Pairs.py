'''

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res

        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了åå
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next