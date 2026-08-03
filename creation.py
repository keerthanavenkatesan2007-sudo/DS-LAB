  class node:
  def__init_(self,data):
       self.data=data self.next=none
class linkedlist:
  def__init_(self):
       self.head=none
  def push(self,new_data):
      new_node=node(new_data)
      new_node.next=self.head
      self.head=new_node
 def insertafter(self,prev_node,new_data):
   if prev_node is none:
     print("the given previous node must inlinkedlist.")
     return
     new_node=node(new_data)
     new_node.next=prev_node.next
     prev_node.next=new_node
def append(self,new_data):
  new_node=node(new_data)
  if self.head is none:
    self.head=new_node
    return
    last=self.head
    while(last.next):
      last=last.next
      last.text=new_node
def printlist(self):
  temp=self.head
  while(temp):
    print(temp.data)
    temp=temp.next
if__name_=='_main__':
      llist=linkedlist()
      llist.append(6)
      llist.push(7);
      llist.push(1);
      llist.append(4)
      llist.insertafter(llist.head.next,8)
print('created linked list is:')
      llist.printlist() 
