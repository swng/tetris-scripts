import json
from os import system

# Load JSON data from file
with open('data-5.json', encoding="utf-8") as f:
    data = json.load(f)

import itertools

# Generate all permutations of the letters "IOSZJLT"
permutations = itertools.permutations("IOSZJLT")

# Create an empty dictionary with permutations as keys and empty lists as values
permutations_dict = {"".join(p): [] for p in permutations}

tspins = ["tsm", "tss", "tsd", "tst"]
for setupindex, setup in enumerate(data):
    print(setupindex, setup["name"])
    if("Image" in setup and len(setup["Image"][0]) > 0):
        system(f"node glueFumens.js --fu {setup['Image'][0][0]} > gluedfumen.txt")
        glued = open("gluedfumen.txt").read()[:-1]
        print(glued)
        for tspin in tspins:
            if(tspin in setup["tag_primary"].lower()):
                system(f'java -jar sfinder.jar cover --tetfu {glued} -p "*p7" --mode {tspin} > coverdata.txt')
        else:
            system(f'java -jar sfinder.jar cover --tetfu {glued} -p "*p7" > coverdata.txt')
        queuescovered = []
        coverdata = [i.split(",") for i in open("output/cover.csv").read().splitlines()[1:]]
        for cover in coverdata:
            if(cover[1] == "O"):
                permutations_dict[cover[0]].append(setupindex)

with open('data-5-covered.json', 'w', encoding="utf-8") as f:
    json.dump(permutations_dict, f)
