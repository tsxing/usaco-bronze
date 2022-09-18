import sys
sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")

class Rect:
  def __init__(self):
    self.x1,self.y1,self.x2,self.y2 = map(int, input().split())
  def area(self):
    return (self.x2-self.x1)*(self.y2-self.y1)

def intersect(a,b):
  overlapX = max(0, min(a.x2, b.x2) - max(a.x1, b.x1))
  overlapY = max(0, min(a.y2, b.y2) - max(a.y1, b.y1))
  return overlapX*overlapY
  
rects = []
for _ in range(3):
  rects.append(Rect())

print(rects[0].area()+rects[1].area()-intersect(rects[0],rects[2])-intersect(rects[1],rects[2]))

