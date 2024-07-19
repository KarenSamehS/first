class Node:
 def __init__(self,data):
  self.data=data
  self.right=None
  self.left=None
 
def invert(root):
 if root is None:
  return
 invert(root.left)
 invert(root.right)
 temp=root.left
 root.left=root.right
 root.right=temp

def inOrder(root):
 if root is None :
  return 
 inOrder(root.left)
 print(root.data , end = " ")
 inOrder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
inOrder(root)
print("\n")
invert(root)
inOrder(root)

