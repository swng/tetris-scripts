import csv
import itertools
import copy

csv_file = open('cover.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

solutions = [[]]

queues = [[]]

queues_minimal_set = [[]]

ids = []

line = 0
for row in csv_reader:
    line += 1
    if line == 1:
        for i in range(1, len(row)): # 0th entry is fumen of solution
            solutions.append([row[i]])
            ids.append(i)
    else:
        queues.append([row[0]])
        queues_minimal_set.append([row[0]])
        for i in range(1, len(row)):
            if row[i] == "O":
                solutions[i].append(True)
                queues[line-1].append(i)
            else:
                solutions[i].append(False)

csv_file.close()

# print(solutions[1][0:20]) # sanity check, printing the beginning of the first line

# ids = []
# print(ids)
print(len(ids))

def forced_minimal(id):
    for i in range(1, len(solutions[id])):
        if solutions[id][i]:
            if len(queues[i]) == 2:
                return True

    return False

def check_subset_removal(id):
    removal_candidate = solutions[id]
    for i in range(1, len(solutions)):
        if i != id:
            solution = solutions[i]
            is_subset = True
            for j in range(1, len(removal_candidate)):
                if removal_candidate[j] and not solution[j]: # removal candidate covers a queue not supported by this solution
                    is_subset = False
                    break
            if is_subset:
                # print(solutions[id][0] + " is a subset of " + solutions[i][0])
                return True
    is_subset = True
    for j in range(1, len(removal_candidate)):
        if removal_candidate[j] and not forced_minimals_coverage[j]:
            is_subset = False
            break
    if is_subset:
        return True

    return False

def proper_set(queues, ids):
    safe = True
    for queue in queues:
        queue_safe = False
        if len(queue) <= 1:  # length 1 means no solutions worked in the first place
            queue_safe = True
        if len(queue) > 1:
            for id in queue:
                if id in ids: # a solution in our set worked for this queue!
                    queue_safe = True
        if not queue_safe:
            safe = False
    return safe

def check_removal(queues, id):
    for queue in queues:
        if id in queue:
            if len(queue) == 2:
                return False
    return True

def check_addition(id):
    added_coverage = False
    for i in range(len(queues)):
        if len(queues_minimal_set[i]) == 1: # if there's currently no solutions for this queue in the current mininimal set
            if id in queues[i]: # if this solution CAN apply to this queue
                queues_minimal_set[i].append(id) # so this function has a side effect
                #if not added_coverage:
                #    print(f"Adding {id}. It adds queue {queues_minimal_set[i][0]}")
                added_coverage = True
    return added_coverage

def sort_against(queues, existing_ids, potential_ids):
    uncovered_queues = [] # ids of queues not covered by existing solutions
    for i in range(1, len(queues)):
        queue = queues[i]
        if len(set(queue) & set(existing_ids)) == 0:
            uncovered_queues.append(i)

    added_coverage = [[x, 0] for x in potential_ids] # number of queues these new solutions add to existing set
    for potential in added_coverage: 
        for uncovered_queue in uncovered_queues:
            if solutions[potential[0]][uncovered_queue]:
                potential[1] += 1
    
    
    added_coverage.sort(key=lambda x: x[1], reverse = True)
    #return ([x[0] for x in added_coverage])
    return added_coverage

# example element of queues
# ['TILJSZO', 1, 5, 6, 14, 15, 16, 17, 18]

# generate sample minimal sets of size n, check if they are proper

forced_minimals = set()

forced_minimals_coverage = [False for i in range(len(queues))]

# find solutions that are guaranteed in and guaranteed out of the minimal set

for id in ids:
    if forced_minimal(id):
        forced_minimals.add(id)

keep_going = True
removed_ids = []

while keep_going:
    keep_going = False
    for id in ids:
        if check_subset_removal(id):
            ids.remove(id)
            removed_ids.append(id)
            for i in range(1, len(solutions[id])):
                if solutions[id][i]:
                    queues[i].remove(id)
                    if len(queues[i]) == 2:
                        forced_minimals.add(queues[i][1])
                        keep_going = True
                        added_minimal_coverage = solutions[id]
                        for j in range(len(added_minimal_coverage)):
                            if added_minimal_coverage[j]:
                                forced_minimals_coverage[j] = True


print("removed minimals:", len(removed_ids))

print("forced minimals:", len(forced_minimals), forced_minimals)

for id in forced_minimals:
    ids.remove(id)

print(len(ids))

# intense method - this is NOT going to be remotely viable for large sets

# min_size = 36 # this is size of the minimal set being generated

# input(f"now iterating over ({len(ids)} choose {min_size - len(forced_minimals)}) combinations")

# candidates = list(itertools.combinations(ids, min_size - len(forced_minimals)))

# input("oh my god it's done generating")

# for candidate in candidates:
#     full_candidate = list(candidate) + forced_minimals
    
#     if proper_set(queues, full_candidate):
#         full_candidate.sort()
#         print(full_candidate)
#         # print(list(candidate))
#         any_good = True




# sorted decreasing method

potential_ids = copy.copy(ids)
minimal_set = list(forced_minimals)

candidates =  [[x, 5040] for x in minimal_set] + sort_against(queues, minimal_set, potential_ids)

if True:
    for candidate in reversed(candidates): # solutions should be in reversed coverage order. all tspin solutions come first
            id = candidate[0]
            if candidate[1] == 0 or check_removal(queues, id):
                
                for queue in queues:
                    if id in queue:
                        queue.remove(id)
                if id in ids:
                    ids.remove(id)
                    removed_ids.append(id)

removed_ids.sort()

ids = list(forced_minimals) + ids
ids.sort()
print(ids)
print(len(ids))

print("Disclaimer, this is a greedy approach. There may be a smaller minimal set than this, or better minimal sets.")

for id in ids:
   print(solutions[id][0])





# sorted increasing method

# potential_ids = copy.copy(ids)
# minimal_set = list(forced_minimals)

# added = True

# while added:
#     candidates = sort_against(queues, minimal_set, potential_ids)
#     #print(candidates)
#     added = False
#     for candidate in candidates:
#         id = candidate[0]
#         if candidate[1] != 0 and check_addition(id):
#             minimal_set.append(id)
#             potential_ids.remove(id)
#             added = True
#             break

# minimal_set.sort()

# print(minimal_set)
# print(len(minimal_set))
# print("Disclaimer, this is a greedy approach. There may be a smaller minimal set than this, or better minimal sets.")

# for id in minimal_set:
#    print(solutions[id][0])