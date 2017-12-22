
f = open('statearray.txt', 'w')
for line in f:
    line[0] = '('
    line.replace(" ", "")
