import linked_list

def swapNodes(self, head: linked_list.ListNode, k: int) -> linked_list.ListNode:
  tracker = []
  curr = head
  while curr != None:
    tracker.append(curr.val)
    curr = curr.next
  curr = head
  # First & last node case
  if k == 1:
    while curr.next != None:
      curr = curr.next
    curr.next = head
    
    