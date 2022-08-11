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
list = [6,3,4,9,0,2,1,6,2,8,1,2,6,3,5,0,7,8,1]
print(list)
n = 4
linked = list_to_linked.linkedListMaker(list)
ans = removeNthFromEnd(linked, n)
while ans != None:
  print(ans.val, end=' ')
  ans = ans.next