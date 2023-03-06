from itertools import permutations

all_bags = list(permutations(['L', 'J', 'S', 'Z', 'I', 'O', 'T']))

# print(len(all_bags))


'''
25% L before S, T before Z, have to hold T
	12.5% Z before L, able to use hold on L
	12.5% L before Z
		6.25% S before T, can hold L
		6.25% T before S, forced to place L on left and create hanging S
'''

labels = [
    "L before S, T before Z, Z before L",
    "L before S, T before Z, L before Z",
    "L before S, T before Z, L before Z, S before T",
    "L before S, T before Z, L before Z, T before S"
]
counts = [0,0,0,0]


for perm in all_bags:
    if perm.index('L') < perm.index('S') and perm.index('T') < perm.index('Z') and perm.index('Z') < perm.index('L'):
        counts[0] = counts[0] + 1
    if perm.index('L') < perm.index('S') and perm.index('T') < perm.index('Z') and perm.index('L') < perm.index('Z'):
        counts[1] = counts[1] + 1
    if perm.index('L') < perm.index('S') and perm.index('T') < perm.index('Z') and perm.index('L') < perm.index('Z') and perm.index('S') < perm.index('T'):
        counts[2] = counts[2] + 1
    if perm.index('L') < perm.index('S') and perm.index('T') < perm.index('Z') and perm.index('L') < perm.index('Z') and perm.index('T') < perm.index('S'):
        counts[3] = counts[3] + 1

for i in range(4):
    print(labels[i], counts[i]/5040)