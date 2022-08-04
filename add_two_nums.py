from asyncio.windows_events import NULL
from typing import List


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def addTwoNumbers(l1, l2):
  num1 = 0
  num2 = 0
  while l1 != None and l2 != None:
    num1 += l1.val
    if (l1.next != None):
      num1 *= 10
    l1 = l1.next
    num2 += l2.val
    if (l2.next != None):
      num2 *= 10
    l2 = l2.next
  new_num = num1 + num2
  if new_num == 0:
    ans = ListNode()
  else:
    new_val = new_num % 10
    ans = ListNode()
    while new_num > 0:
      
      new_node = ListNode()