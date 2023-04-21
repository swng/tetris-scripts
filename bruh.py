import json
from os import system

# Load JSON data from file
with open('data-3.json', encoding="utf-8") as f:
    data = json.load(f)[:3]

import itertools

# Generate all permutations of the letters "IOSZJLT"
permutations = itertools.permutations("IOSZJLT")

# Create an empty dictionary with permutations as keys and empty lists as values
permutations_dict = {"".join(p): [] for p in permutations}

tspins = ["tsm", "tss", "tsd", "tst"]

datalength = len(data)
for setupindex, setup in enumerate(data):
    print(f"setup number {setupindex} out of {datalength}")
    if("Image" in setup and len(setup["Image"][0]) > 0):
        system(f"node converttoblue.js {setup['Image'][0][0]} > bluedfumen.txt")
        blued = open("bluedfumen.txt").read().replace("\n", "")
        system(f"node encode.js {blued} > bluedfumen.txt")
        blued = open("bluedfumen.txt").read().replace("\n", "")
        system(f"java -jar sfinder.jar setup --tetfu {blued} --patterns *p7 --fill I -d 180 -K kicks/tetrio180.properties -fo csv > setupoutput.txt")
        allfumens = [i.split(",")[0] for i in open("output/setup.csv").read().splitlines()[1:]]
        queuesalreadycovered = []
        for fumen in allfumens:
            system(f"node glueFumens.js --fu {fumen} > gluedfumen.txt")
            glued = open("gluedfumen.txt").read().splitlines()
            for tspin in tspins:
                if(tspin in setup["tag_primary"].lower()):
                    system(f"java -jar sfinder.jar cover --tetfu {glued} -p *p7 --mode {tspin} > coverdata.txt")
            else:
                system(f"java -jar sfinder.jar cover --tetfu {glued} -p *p7 > coverdata.txt")
            queuescovered = []
            coverdata = [i.split(",") for i in open("output/cover.csv").read().splitlines()[1:]]
            for cover in coverdata:
                if(cover[1] == "O" and not cover[0] in queuesalreadycovered):
                    permutations_dict[cover[0]].append(setupindex)
                    queuesalreadycovered.append(cover[0])

with open('data-3-covered.json', 'w', encoding="utf-8") as f:
    json.dump(permutations_dict, f)
