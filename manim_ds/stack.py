""" Stack Implementation """
__all__ = [
    "Stack",
    "Plays", 
]

from manim import *
import numpy as np

class Stack(VGroup):
    def __init__(
        self,
        size: float = 0,
        scale: float = 0.5,
        index: float = 0,
        posU: float = 0,
        posD: float = 0,
        **kwargs,
    ) -> None:
        VGroup.__init__(self, **kwargs)
        self.size = size
        self.count = 0
        self.scale = scale
        self.index = size-1
        self.posU = posU
        self.posD = posD
        self.ele = []
        self.label = Text("TOP").scale(0.75)
        self.point = Arrow(start=LEFT , end=RIGHT)
        self.node = []
        for i in range(self.size):
            rect = Rectangle()
            rect.scale(self.scale)
            rect.next_to(rect,DOWN*i*4)
            self.node.append(rect)

        self.node[0].shift(DOWN)
        stack =  VGroup(*self.node)
        stack.move_to(ORIGIN)
        self.add(stack)

        #for mob in self:
        #    mob.set_z_index(1)

    def checkOvf(self, inp):
        if self.index < 0:
            self.overflow()
            return 0

    def checkUnf(self , inp):
        if self.index >= self.size-1:
            self.underflow()
            return 0

    def addEle(self ,val, **kwargs):
            lbl = Text(val).scale(0.75)
            lbl.move_to(self.node[self.index].get_center())
            self.ele.append(lbl)
            self.index -= 1
            self.count += 1
            self.add(*self.ele)
            self.top()
            self.add(self.label,self.point)
    
    def removeEle(self, **kwargs):
        self.remove(*[self.ele[self.count-1]])
        del self.ele[self.count-1]
        self.count -= 1
        self.index += 1
        self.top()

    def overflow(self):
        ofl = Text("OVERFLOW !").scale(0.75)
        ofl.set_color(RED)
        ofl.next_to(self.node[0],RIGHT)
        self.add(ofl)

    def underflow(self):
        ufl = Text("UNDERFLOW!").scale(0.75)
        ufl.set_color(BLUE)
        ufl.next_to(self.node[0],LEFT)
        self.add(ufl)        

    def top(self, **kwargs):
        if self.index >= self.size-1:
            self.point.move_to(self.node[self.index],LEFT)
        else:
            self.point.move_to(self.node[self.index+1],LEFT)
        self.point.shift(LEFT*2)
        always_redraw( lambda :
            self.label.next_to(self.point,UP).shift(LEFT*0.25 + DOWN * 0.25),
        )
    
class Plays(Scene):
    def draws(self ,mob, **kwargs):
        self.play(Transform(mob,mob))