import list_to_linked

def removeNthFromEnd(head: list_to_linked.ListNode, n : int):
  tracker = []
  curr = head
  while curr != None:
    tracker.append(curr.val)
    curr = curr.next
  curr = head
  # First node case
  if n == len(tracker):
    head = head.next
  # Middle or last node case
  elif (len(tracker) > 1):
    for i in range(len(tracker) - n):
      curr = curr.next
    curr.next = curr.next.next
  # Empty list case
  else:
    head = None
  return head

#Tests 
node2 = ListNode(2)
node1 = ListNode(1, node2)
print(removeNthFromEnd(node1, 2).val)