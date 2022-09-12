import sys
sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")

bill1x1,bill1y1,bill1x2,bill1y2 = map(int, input().split())
bill2x1,bill2y1,bill2x2,bill2y2 = map(int, input().split())
tx1,ty1,tx2,ty2 = map(int, input().split())


def area(recx1,recy1,recx2,recy2):
  return (recx2-recx1)*(recy2-recy1)

def intersect(recX1,recY1,recX2,recY2, rec2X1,rec2Y1,rec2X2,rec2Y2): #intersecting area of 2 recs
  height = min(recY2,rec2Y2)-max(recY1,rec2Y1)
  length = min(recX2,rec2X2)-max(recX1,rec2X1)
  if min(height,length)>0:
    return height*length
  else:
    return 0

#one rec and truck intersects. find rec area - intersection. do that for our 2 recs/billboards, then add the 2 visible parts.

a1 = area(bill1x1,bill1y1,bill1x2,bill1y2)
a2 = area(bill2x1,bill2y1,bill2x2,bill2y2)

i1 = intersect(bill1x1,bill1y1,bill1x2,bill1y2,tx1,ty1,tx2,ty2)
i2 = intersect(bill2x1,bill2y1,bill2x2,bill2y2,tx1,ty1,tx2,ty2)
  
visible1 = a1-i1
visible2 = a2-i2

print(visible1+visible2)

