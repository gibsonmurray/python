class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def addTwoNumbers(l1, l2):
  num1 = 0
  num2 = 0
  ans = None
  count1 = 0
  count2 = 0
  while l1 != None and l2 != None:
    num1 += l1.val * (10**count1)
    num2 += l2.val * (10**count2)
    if (l1 != None):
      l1 = l1.next
    if (l2 != None):
      l2 = l2.next
    count1 = count1 + 1
    count2 = count2 + 1
  new_num = num1 + num2
  if new_num == 0:
    ans = ListNode()
  else:
    if ans == None:
      ans = ListNode(new_num % 10)
      new_num = new_num / 10
    curr = ans
    while new_num > 1:
      while curr != None:
        if curr.next == None:
          new_node = ListNode(new_num % 10)
          curr.next = new_node
          curr = None
        if curr != None:
          curr = curr.next
      new_num = int(new_num / 10)
    return ans

#Tests
three_a = ListNode(3)
two_a = ListNode(4, three_a)
one_a = ListNode(2, two_a)
three_b = ListNode(4)
two_b = ListNode(6, three_b)
one_b = ListNode(5, two_b)
curr = addTwoNumbers(one_a, one_b)
while curr != None:
  print(curr.val)
  curr = curr.next