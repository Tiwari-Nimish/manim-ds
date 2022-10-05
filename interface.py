from manim import *
from manim_ds import *

class Cli(Plays):
    def construct(self):
        print("----------------------")
        print("1. Stack ")
        print("2. Binary Search Tree")
        print("----------------------")
        choice = int(input("Enter : "))
        if choice == 1:
            self.stackOprs()
        if choice == 2:
            self.treeOprs()
    
    def stackOprs(self):
        print("----------------------")
        size = int(input("Enter the size of the stack: "))
        print("----------------------")
        stack = Stack(size = size)
        while True:
            print("----------------------")
            inp = int(input("Enter\n 0. to exit \n 1. Push \n 2. Pop \n Choice: " ))
            print("----------------------")
            if inp == 0:
                break
            if inp == 1:
                pushEle = input("Enter element to be pushed : ")
                inp = stack.checkOvf(inp)
                if inp == 0:
                    self.draws(stack)
                    break
                stack.addEle(pushEle)
                self.draws(stack)
            if inp == 2:
                inp = stack.checkUnf(inp)
                if inp == 0:
                    self.draws(stack)
                    break
                print("Element Poped ")
                stack.removeEle()
                self.draws(stack)
    
    def treeOprs(self):
        tree = []
        node = TNode()
        while True:
            print("-------------------")
            print("0. To Exit")
            print("1. Add Element")
            inp = int(input("Enter Choice : "))
            print("-------------------")
            if inp == 0:
                break
            if inp == 1:
                ele = input("Enter Element to be added : ")
                tree.append(ele)
                node.addEle(ele)
                self.draws(node)