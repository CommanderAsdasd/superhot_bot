L1 = [1, 3, 5]
L2 = [1+1, 3, 5]
L3 = [1, 3+2, 5+6]
# for i,v in enumerate(L):          # (index,value)
for x,y,z in zip(L1,L2,L3):
    print(x,y,z)          # returns tuples
# for i in sorted(set(L)): print(i)     # sorted set from a list
# for x in reversed(L1):