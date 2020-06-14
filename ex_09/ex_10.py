fname = input('enter file:')
if len(fname)<1 : fname = 'clown.txt'
hand = open(fname)


di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # print(w)
        if w in di:
            di[w] = di[w]+1
        else:
            di[w] = 1
            # print('**New**')
# print(di)


largest = -1
theword = None
for k,v in di.items():
    # print(k,v)
    if v> largest:
        largest =  v
        theword = k

# print(theword,largest)


x = sorted(di.items())
# print(x[:5])

tmp = list()
for k,v in di.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print('Flipped',tmp)
tmp = sorted(tmp, reverse=True)
# print('Sorted',tmp)

for v,k in tmp[:5] :
    print(k,v)
