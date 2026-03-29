class Tree:
   #Constructor
   def __init__(self, initval = None):
      self.value = initval
      if self.value:
         self.left = Tree()
         self.right = Tree()
      else:
         self.left = None
         self.right = None
      return
   ##only empty nodr has value none
   def isempty(self):
      return(self.vale == None)
   #leaf nodes have both children empty
   def isleaf(self):
              return(self.value != None and self.left.isempty() and self.right.isempty())
   #inorder transversal
   def inorder(self):
       if self.empty():
           return([])
       else:
           return(self.left.inorder()+[self.value.inorder()])
   #display tree as a string
   def __str__(self):
   return(str(self.inorder()))
   
   #check if value v occurs in tree
   def find (self, v):
      if self.isempty():
         return(False)
      if self.value == v:
         return(True)
      if v < self.value:
         return(self.left.find(v))
      if v > self.value:
         return(self.right.find(v))
   def minval(self):
      if self.left.isempty():
         return(self.value)
      else:
         return(self.;eft.minval())
   def maxval(self):
      if self.right.isempty():
         return(self.value)
      else:
         return(self.right.maxval())
   def insert (self, v):
      if self.isempty():
         self.value = v
         self.left = Tree()
         self.right = Tree()
      if self.value == v:
         return
      if v < self.value:
         self.left.insert(v)
         return
      if v > self.value:
         self.right.insert(v)
         return
   def delete (self,v):
      if self.isempty():
         return
      if v < self.value:
         self.left.delete(v)
         return
      if v > self.value:
         self.right.delete(v)
         return
      if v == self.value:
         if self.isleaf():
            self.makeempty()
         elif self.left.isempty():
            self.copyright()
         elif self.right.isempty():
         self.copyleft()
         else: 
            self.value = self.left.maxval()
            self.left.delete(self.left.maxval()) 
         return  
   #convert leaf node to empty node
   def makeempty(self):
      self.value = None
      self.left = None
      self.right = None
      return
   #promote left child
   def copyleft(self):
      self.value = self.left.value
      self.left = self.left.left
      self.right = self.left.right
      return
   #promote right child
   def copyright(self):
      self.value = self.right.value
      self.left = self.right.left
      self.right = self.right.right
      return
   def leftrotate(self):
      v = self.value
      vr = self.right.value
      tl = self.left
      trl = self.right.left
      trr =self.right.right

      newleft = Tree(v)
      newleft.left = tl
      newleft.right = trl

      self.value = vr
      self.right = trr 
      self.left = newleft
      return

   def rightrotate(self):
      v = self.value
      vl = self.left.value
      tll = self.left.left
      tlr = self.left.right
      tr = self.right

      newright = Tree(v)
      newright.left = tlr
      newright.right = tr

      self.value = vl
      self.right = tll 
      self.right = newright
      return

   def insert(self, v):
      if self.isempty():
         self.value = v
         self.left = Tree()
         self.right = Tree()
      if self.value == v:
         return
      if v < self.value:
         self.left.insert(v)
         self.left.rebalance()
         return 
      if v > self.value:
         self.right.insert(v)
         self.right.rebalance()
         return

      if v < self.value:
         self.left.insert(v)
         self.left.rebalance()
         self.height = 1 + max(self.left.height, self.right.height)
         return
      if v > self.value:
         self.right.insert(v)
         self.right.rebalance()
         self.height = 1 + max(elf.left.height, self.right.height)
         return   
   
   def delete (self,v):
      if self.isempty():
         return
      if v < self.value:
         self.left.delete(v)
         self.right.rebalance()
         return
      if v > self.value:
         self.right.delete(v)
         self.right.rebalance()
         return
      if v == self.value:
         if self.isleaf():
            self.makeempty()
         elif self.left.isempty():
            self.copyright()
         elif self.right.isempty():
         self.copyleft()
         else: 
            self.value = self.left.maxval()
            self.left.delete(self.left.maxval()) 
         return
   def height(self):
      if self.isempty():
         return(0)
      else:
         return(1+ max(self.left.height(), self.right.height()))