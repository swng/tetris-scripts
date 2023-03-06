f = open('in.txt', 'r')
lines = f.readlines()
lines.sort()

for line in lines:
    print(line)

# with open('out.txt', 'w') as g:
#     for line in lines:
#         g.write(line)