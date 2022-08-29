import linked_list

def swapNodes(head: linked_list.ListNode, k: int) -> linked_list.ListNode:
  n = 0
  curr = head
  while curr != None:
    n = n + 1
  curr = head # resets curr to head
  # Case 1: odd number of nodes, swaps middle node : nothing changes
  if n % 2 == 1:
    # Do nothing
    return head
  # Case 2: if k = 1 or n
  elif k == 1 or k == n:
    while curr.next != None:
      curr = curr.next
    temp = curr #copies last node
    curr = head 
    temp.next = head.next
    curr.next = None
    head = temp
  # Case 3: if k <= n/2
  elif k <= n/2:
    for i in range(1, k):
      curr = curr.next
    temp1 = curr
    for i in range(1, n - (2 * k)):
      curr = curr.next
    temp2 = curr
    # continue to swap
  # Case 4: k >= n/2

    
    
#Tests
list = linked_list.linkedListMaker([1, 2, 3, 4, 5])
list = swapNodes(list, 1)
while list != None:
  print(list.val, end=' ')
  list = list.next