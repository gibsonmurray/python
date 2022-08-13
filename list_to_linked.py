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