#Sneha Yalavarti, HW_01_B
#Original File: https://editor.p5js.org/thiagohersan/sketches/mJdFIgeNo

class Agent: 
    def __init__ (self, width, height):
        self.x = random(17, width - 17)
        self.y = random(17, height - 17)
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
        self.radius = random(8, 16)
        self.diam = 2 * self.radius
    
    def update(self):
        self.updateByVelocity()
        self.bounceBoundary()
        
    def bounceBoundary(self):
        if (self.x + self.radius >= width or self.x - self.radius <= 0):
            self.vx *= -1
        if(self.y + self.radius >= height or self.y - self.radius <= 0):
            self.vy *= -1
            
    def updateByVelocity(self):
        self.x += self.vx;
        self.y += self.vy;
        
    def drawAgent(self):
        ellipse(self.x, self.y, self.diam, self.diam)
    
    def draw(self): 
        if (currentMode == POINT_MODE):
            stroke(0)
            self.drawPoint()
        elif (currentMode == OVERLAP_MODE):  
            stroke(0, 16)
            noFill()
            self.drawOverlap()    
        
    def drawPoint(self):
        point(self.x, self.y)  
        
    def drawOverlap(self):
        for i in range(0,len(agents),1):
            otherAgent = agents[i]
            if (self != otherAgent): 
                tDist = dist(self.x, self.y, otherAgent.x, otherAgent.y)
                if (tDist < self.radius + otherAgent.radius):
                    cx = (self.x + otherAgent.x) / 2
                    cy = (self.y + otherAgent.y) / 2
                    ellipse(cx, cy, tDist, tDist)
                    
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
        
        
        
    
