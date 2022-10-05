""" BST Implementation """
__all__ = [
    "TNode",
    "Plays", 
]

from manim import *
from .treeMaker import *
import numpy as np

class TNode(VGroup):
    def __init__(
    self,
    **kwargs):
        VGroup.__init__(self,**kwargs)
        self.tree = []
        self.nds = []
        self.lines = []
        self.topCount = []
        self.nodeGrp = VGroup()

    def addLines(self,indexOut,indexIn):
        self.lines.append(Line(self.nds[indexOut].get_bottom(),self.nds[indexIn].get_top()))
        self.topCount[indexIn] = 1
    
    def showNodes(self,data,lvl,posL,posR,rT):
        self.nds = []
        lbls = []
        self.lines = []
        self.topCount = [0]*len(data)
        nGrp = VGroup()
        
        for i in range(len(data)):
            lbls.append(Tex(data[i]))
            self.nds.append(Circle().scale(0.4))
            self.nds[i].shift(UP+DOWN*lvl[i])
            self.nds[i].shift(LEFT*posL[i]+RIGHT*posR[i])
            lbls[i].move_to(self.nds[i].get_center())


        for i in range(len(data)):
            for nindex in range(len(data)):
                iDistR = posR[i]-posL[i]
                nDistR = posR[nindex]-posL[nindex]
                if lvl[i]+1 == lvl[nindex] and rT[nindex] == data[i]:
                    if self.topCount[nindex] == 1:
                        continue
                    
                    if i == 0:
                        self.addLines(i, nindex)
                    
                    if iDistR>0 and nDistR>0:
                        self.addLines(i, nindex)
                    
                    if -iDistR>0 and -nDistR>0:
                        self.addLines(i, nindex)
                                        
        
        self.nodeGrp.remove(*[mobs for mobs in self.nodeGrp])
        self.nodeGrp.add(*self.nds,*lbls,*self.lines)
        self.nodeGrp.move_to(ORIGIN).shift(UP)
        self.nodeGrp.scale(0.75)
        self.add(self.nodeGrp)


    def addEle(self,ele):
        tmaker = BST()
        self.tree.append(int(ele))
        for ele in self.tree:
            tmaker.makeNode(ele)
        tdata,tlvl,tposL,tposR,rT = tmaker.preorder(tmaker.root)
        self.showNodes(tdata,tlvl,tposL,tposR,rT)
    
class Plays(Scene):
    def draws(self ,mob, **kwargs):
        self.play(Transform(mob,mob))
