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
    for i in range(len(tracker) - n - 1):
      curr = curr.next
    curr.next = curr.next.next
  # Empty list case
  else:
    head = None
  return head

#Tests 
list = [1, 2, 3, 4]
print(list)
n = 1
linked = list_to_linked.linkedListMaker(list)
ans = removeNthFromEnd(linked, n)
while ans != None:
  print(ans.val, end=' ')
  ans = ans.next