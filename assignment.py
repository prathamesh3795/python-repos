class node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node


    #Traverse and print the value

    def traverse(self):
        if not self.head:
            print("Empty List")
            return
        cur=self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next

        print("None")


    # Insert by specific position    

    def insert(self,pos,new):
        print("Insert Data:",new,"At Position : ",pos)
        new_node=node(new)
        if pos==1:
           new_node.next=self.head
           self.head=new_node
           return
        curr=self.head
        for _ in range(pos -2):
            if curr is None:
                print("Out of bond")
                return
            curr=curr.next

        if curr is None:
            print("Out of bound")
            return
        new_node.next=curr.next
        curr.next=new_node

      
    # Delete Negative Node

    def delete(self):
        cur=self.head
        temp=self.head
        while self.head and self.head.data <0:
            self.head=self.head.next
        while cur and cur.next:
       
            if cur.next.data<0:
                temp=cur.next
                cur.next=cur.next.next
                temp.data=None
                temp.next=None
                temp=None
            else:
                cur=cur.next    

l1=linkedList()
l1.append(-10)
l1.append(11)
l1.append(-20)
l1.append(-10)

l1.traverse()

l1.insert(3,50)
print("Before Insert New Node")
l1.traverse()

l1.delete()
print("Before Delete Negative Node")
l1.traverse()