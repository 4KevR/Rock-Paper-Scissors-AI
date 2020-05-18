from random import choice
from time import sleep

from . import analyse

# 0 rock, 1 paper, 2 scissors

class ComputerPlayer:
    def __init__(self):
        self.points = 0
    
    def random(self):
        return choice(["r","p","s"])
    
    def point(self):
        self.points += 1
    
    
class HandPlayer:    
    def __init__(self):
        self.points = 0
        #self.camera = PiCamera()
        # self.camera.vflip = True
        # self.camera.hflip = True

    def recognize(self):
        #analysing
        analysis = analyse.classify("media/img.jpg")

        label = analysis["class_name"]
        confidence = analysis["confidence"]
        
        print ("I think this is: '%s' with %d%% confidence" % (label, confidence))
        
        return {"label":label[0],"confidence":confidence}
    
    def __consoleInput(self):
        inp = input("Gebe ein (r, p, s): ")
        if inp in ["r","p","s"]:
            return inp
        else:
            return self.__consoleInput()
        
    def point(self):
        self.points += 1