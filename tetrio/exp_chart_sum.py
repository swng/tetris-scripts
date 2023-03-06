f = open("levels.txt", "r")
sum = 0
for i in range(5000):
    sum = sum + (int(f.readline().split()[2]))
print(sum)