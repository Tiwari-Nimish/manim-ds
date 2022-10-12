class Node():

      def __init__(self,data,lvl,posL,posR,rTo):
          self.data = data 
          self.left = None 
          self.right = None 
          self.level = lvl
          self.leftTvl = posL
          self.rightTvl = posR
          self.relTo = rTo
class BST():

      def __init__(self): 
          self.root = None
          self.treedata = []
          self.treelvl = []
          self.treeposL = []
          self.treeposR = []
          self.rT = []

      def makeNode(self,val): 
          updater = 3
          if self.root == None:
             self.root = Node(val,0,0,0,0)

          else:
             current = self.root
             lvl = 0
             posL = 0
             posR = 0
             rT = 0
             while True:
                if val < current.data :
                   if current.left:
                      current = current.left
                      lvl += 1
                      updater -= 0.6
                      rT = current.data

                   else:
                      lvl += 1
                      posR = current.rightTvl
                      posL = current.leftTvl
                      rT = current.data
                      if lvl == 1:
                        posR = 0
                        posL = 3.75
                      else:
                        posR += 0
                        posL += updater
                      current.left = Node(val,lvl,posL,posR,rT)
                      updater -= 0.6

                      break    
                elif val > current.data:
                    if current.right:
                       current = current.right
                       lvl += 1
                       updater -= 0.6
                       rT = current.data

                    else:
                       lvl += 1
                       posR = current.rightTvl
                       posL = current.leftTvl
                       rT = current.data
                       if lvl == 1:
                        posR = 3.75
                        posL = 0
                       else:
                        posR += updater
                        posL += 0
                       current.right = Node(val,lvl,posL,posR,rT)
                       updater -= 0.6

                       break     
                else:
                    break 

      def preorder(self,node):
         if node is not None: 
            self.treedata.append(node.data)
            self.treelvl.append(node.level)
            self.treeposL.append(node.leftTvl)
            self.treeposR.append(node.rightTvl)
            self.rT.append(node.relTo)
            self.preorder(node.left)
            self.preorder(node.right)
         return self.treedata,self.treelvl,self.treeposL,self.treeposR,self.rT
