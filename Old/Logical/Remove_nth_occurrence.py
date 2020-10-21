l = ['india','usa','india','uk','india']


pos1 = 0
pos2 = 2

c = len(l)

for i in range(0,c):
    if (l[i] == 'india'):
        del l[i]
