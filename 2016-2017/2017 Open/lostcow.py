x, y = map(int, input().split())

mov = 1
find = False
tot = 0
bes = x

if x<y:
    while find==False:
        bes = x
        bes += mov
        if bes>y:
            tot += abs(mov)-abs(bes-y)
            break
        tot += abs(mov*2)
        mov*=-2
    #print(bes,mov,tot)
if x>y: 
    while find==False:
        bes = x
        bes += mov
        if bes<y:
            tot += abs(mov)-abs(bes-y)
            break
        if bes==y:
            tot += abs(mov)
            break
        tot += abs(mov*2)
        mov*=-2
print(tot)
