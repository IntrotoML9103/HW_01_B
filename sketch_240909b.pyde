#Sneha Yalavarti, HW_01_B
#Original File: https://editor.p5js.org/thiagohersan/sketches/mJdFIgeNo

import random

class Agent: 
    def _init_ (self, width, height):
        self.x = random.random(17, width - 17)
        self.y = random.random(17, height - 17)
        self.vx = random.random(-2, 2)
        self.vy = random.random(-2, 2)
        self.radius = random.random(8, 16)
        self.diam = 2 * self.radius
    
    def update():
        self.updateByVelocity()
        self.bounceBoundary()
        
    def bounceBoundary():
        if (self.x + self.radius >= width or self.x - self.radius <= 0):
            self.vx *= -1
        if(self.y + self.radius >= height or self.y - self.radius <= 0):
            self.vy *= -1
            
    def updateByVelocity():
        self.x += self.vx;
        self.y += self.vy;
        
    def drawAgent():
        ellipse(self.x, self.y, self.diam)
    
    def draw(): 
        if (currentMode == POINT_MODE):
            stroke(0)
            self.drawPoint()
        elif (currentMode == OVERLAP_MODE):  
            stroke(0, 16)
            noFill()
            self.drawOverlap()    
        
    def drawPoint():
        point(tself.x, self.y)  
        
    def drawOverlap():
        for i in range(0,len(agents),1):
            otherAgent = agents[i]
            if (self != otherAgent): 
                tDist = dist(self.x, self.y, otherAgent.x, otherAgent.y)
                if (tDist < self.radius + otherAgent.radius):
                    cx = (self.x + otherAgent.x) / 2
                    cy = (self.y + otherAgent.y) / 2
                    ellipse(cx, cy, tDist)
                    
maxAgents = 32

agents = []

AGENT_MODE = 0
POINT_MODE = 1
OVERLAP_MODE = 2

currentMode = AGENT_MODE

def setup():
    size(800,600)
    
    for i in range(0,maxAgents,1): 
         agents.append(Agent(width,height))
         
def draw():
    for i in range(0,len(agents),1):
        agents[i].update()
    
    if(currentMode == AGENT_MODE): 
        background(220, 20, 120)
        
        noStroke();
        fill(255);
        for i in range(0,len(agents),1):
            agents[i].drawAgent()
    else:
        for i in range(0,len(agents),1):
            agents[i].draw()
            

def mouseClicked():
     currentMode = (currentMode + 1) % 3
     if (currentMode != AGENT_MODE):
          background(255)
        
        
        
    
