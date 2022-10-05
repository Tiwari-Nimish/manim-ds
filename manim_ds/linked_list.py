"""Linked List Implimentation"""

__all__ = [
    "Node",
    "Plays",
]

from manim import *
import numpy as np

class NodeLst(VGroup):
    def __init__(
        self,
        size: float = 0,
        index: float = 0,
        scale: float = 0.5,
        **kwargs,
    ) -> None:
        VGroup.__init__(self, **kwargs)
        self.size = size
        self.index = index
        self.scale = scale
        self.valNode = []
        self.addNode = []
        # valN = Rectangle()
        # addN = Rectangle()
        # pointNxt = Arrow(start=LEFT,end=RIGHT)
        # self.valNode.append(valN)
        # self.addNode.append(addN)
        # self.listG = VGroup(*self.valNode,*self.addNode)
        # always_redraw(lambda: self.listG.scale(self.scale))
        self.listG = VGroup()
        self.add(self.listG)
    
    
    def addEle(self , val, **kwargs):
        if len(self.valNode) <= 0:
            print("Hello")
        else:
            for mob in self.listG:
                mob.shift(LEFT*2)
            #self.listG.move_to(pointNxt.tip.tip_point())
        valN = Rectangle().scale(self.scale)
        addN = Rectangle().scale(self.scale)
        addN.next_to(valN)
        pointNxt = Arrow(start=LEFT,end=RIGHT)
        ele = Tex(val)
        self.valNode.append(valN)
        self.addNode.append(addN)
        self.index += 1
        self.listG.add(*self.valNode,*self.addNode,ele)
        self.add(*self.valNode,*self.addNode,ele)


        


class Plays(Scene):
    def draws(self ,mob, **kwargs):
        self.play(Transform(mob,mob))