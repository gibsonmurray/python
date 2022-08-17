import linked_list

def swapNodes(head: linked_list.ListNode, k: int) -> linked_list.ListNode:
  # tracker = []
  # curr = head
  # while curr != None:
  #   tracker.append(curr.val)
  #   curr = curr.next
  curr = head
  # First & last node case
  if k == 1:
    while curr.next != None:
      curr = curr.next
    curr.next = head
    curr = head
    while curr.next.next != head:
      curr = curr.next
    temp = curr.next
    curr.next = head
    temp.next = head.next
    head.next = temp
    head.next = None
    head = temp
  return head
    
    
#Tests
list = linked_list.linkedListMaker([1, 2, 3, 4, 5])
list = swapNodes(list, 1)
while list != None:
  print(list.val, end=' ')
  list = list.next