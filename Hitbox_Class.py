import math

class Hitbox:

    def __init__(self, activex, activey, actwidth, actheight, passivex, passivey, paswidth, pasheight,
                 parent):
        self.activex = activex
        self.activey = activey
        self.actrightx = activex + actwidth
        self.actrighty = activey
        self.actdownx = activex
        self.actdowny = activey + actheight
        self.actfarx = activex + actwidth
        self.actfary = activey + actheight
        self.passivex = passivex
        self.passivey = passivey
        self.pasfarx = passivex + paswidth
        self.pasfary = passivey + pasheight
        self.parent = parent

    def hit(self):
        if (((self.activex > self.passivex and self.activex < self.pasfarx and
             self.activey > self.passivey and self.activey < self.pasfary)
            or (self.actrightx > self.passivex and self.actrightx < self.pasfarx and
                self.actrighty > self.passivey and self.actrighty < self.pasfary)
            or (self.actdownx > self.passivex and self.actdownx < self.pasfarx and
                self.actdowny > self.passivey and self.actdowny < self.pasfary)
            or (self.actfarx > self.passivex and self.actfarx < self.pasfarx and
                self.actfary > self.passivey and self.actfary < self.pasfary))) and self.parent.blit:
            return True
        else:
            return False

    def inside(self):
        if ((self.activex > self.passivex and self.activex < self.pasfarx and
             self.activey > self.passivey and self.activey < self.pasfary)
            and (self.actrightx > self.passivex and self.actrightx < self.pasfarx and
                self.actrighty > self.passivey and self.actrighty < self.pasfary)
            and (self.actdownx > self.passivex and self.actdownx < self.pasfarx and
                self.actdowny > self.passivey and self.actdowny < self.pasfary)
            and (self.actfarx > self.passivex and self.actfarx < self.pasfarx and
                self.actfary > self.passivey and self.actfary < self.pasfary)):
            return True
        else:
            return False

    def slope(self, y2, y1, x2, x1):
        return ((y2-y1)/(x2-x1))

    def linefunctionx(self, slope, x, y, pointx, pointy):
        slope = slope()
        return (slope * (x - pointx)) + pointy

    def linefunctiony(self, slope, y, pointx, pointy):
        return ((y - pointy) / slope) + pointx

    def laser(self, direction):
        y1 = self.linefunctionx(math.atan(direction), self.passivex, self.activex, self.activey)
        y2 = self.linefunctionx(math.atan(direction), self.pasfarx, self.activex, self.activey)
        x1 = self.linefunctiony(math.atan(direction), self.passivey, self.activex, self.activey)
        x2 = self.linefunctiony(math.atan(direction), self.pasfary, self.activex, self.activey)
        if ((y1 > self.passivey and y1 < self.pasfary) or (y2 > self.passivey and y2 < self.pasfary) or
            (x1 > self.passivex and x1 < self.pasfarx) or (x2 > self.passivex and x2 < self.pasfarx)):
            return True
        else:
            return False


    def getParent(self):
        return self.parent

    def changeActive(self, activex, activey):
        self.activex = activex
        self.activey = activey

    def changePassive(self, passivex, passivey):
        self.passivex = passivex
        self.passivey = passivey