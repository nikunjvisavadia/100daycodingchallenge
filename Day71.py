t = int(input())
lc = []
for mml in range(0,t):
    l = int(input())
    jk = str(input())
    tp = []
    for kkc in jk.split(" "):
        tp.append(int(kkc))
    lc.append(tp)
for bb in lc:
    ofr=0
    for iir in range(0,len(bb)):
        l = 0
        m = 0
        for kke in range(0,len(bb)):
            if bb[kke] <= bb[iir]:
                l+=1
            else:
                m+=1
        if l>m:
            ofr+=1
    print(ofr)