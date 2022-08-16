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

# indexed starting at 1
def insert(head: ListNode, node: ListNode, n: int) -> ListNode:
  curr = head
  for i in range(n - 2):
    curr = curr.next
  node.next = curr.next
  curr.next = node
  return head

#Tests
head = linkedListMaker([1, 2, 3, 4, 5, 6])
new_node = ListNode(8)
insert(head, new_node, 7)
curr = head
while curr != None:
  print(curr.val, end=' ')
  curr = curr.next
  