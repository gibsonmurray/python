class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def linkedListMaker(list: list) -> ListNode:
  ans = None
  new = None
  curr = None
  if (len(list) > 0):
    new = ListNode(list[0])
    ans = new
    for i in range(1, len(list)):
      curr = new
      new = ListNode(list[i])
      curr.next = new
  return ans

#Tests
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# head = linkedListMaker(list)
# for i in range(len(list)):
#   print(head.val, end=' ')
#   head = head.next