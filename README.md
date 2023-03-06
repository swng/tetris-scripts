# Random assortment of short scripts involved in tetris research, largely dealing with sfinder output

# copy.bat
copies the cover.csv from the sfinder directory into the current directory. Adjust coverPath to your own sfinder directory. It's a batch file, so it's to be run on Windows.

# covered_path.py
reads a cover.csv file, and prints out the paths that are covered by a particular queue. Adjust the queue string on L14 to the queue you're looking into... Python.

# uncovered_queues.py
reads a cover.csv file, and prints out queues for which no solutions are covered. Python.

# forced_solution.py
reads a cover.csv file, and prints out the queues for which a particular solution is "forced" - that particular solution is the only solution covered by that queue. Adjust the index of the solution you're interested in. Used to get a sense of what sort of queue patterns to look for a particular (fallback) solution. Python.

# minimals.py
reads a cover.csv file and heuristically tries to generate a "minimal" subset of solutions that maintains full coverage. Heuristic methods are not guaranteed to find the absolute smallest possible sized qualifying subset, but they generaly get close (often n+1 or n+2) and are significantly faster than brute force.  
Used to attempt to generate semi-manually curated "minimal" sets. Adjust the input paths in the cover.csv, the logic in the heuristics used, whatever, to try to coax it into including sols you like, whatever.  
After parsing the data, it determines sols that definitely must be in the minimal set, and sols that definitely don't need to be in the minimal set. Then it runs through the heuristic alg of generating the "minimal" set. One bruteforce alg and two heuristic methods are provided. Keep 2/3 of these commented out.  
Sorted decreasing method attempts greedily removing sols (in order of coverage) until no sols can be removed while maintaining full coverage.  
Sorted increasing method attempts greedily adding sols (in order of added coverage) until coverage stops increasing.  
Again, results are not guaranteed to be absolutely minimal.  
Python

# path_to_cover.js
Converts path.csv to cover.csv. The path.csv is assumed to be generated with sfinder arguments arguments `-f csv -k pattern`  
Node.js

# 1kf.js
For full transparency and for preservation sake, uploading my personal copy of 1kf jstris userscript here into this repo. Original script by Justin1L8. This is the deepdrop version - this means that it will look for the lowest possible row to drop the piece.  
Usage:  
Install this userscript with a userscript manager extension such as Tampermonkey/Greasemonkey/Violentmonkey.  
Set certain variables to configure a few things:  
username string (my 1kf account is "1kfst")  
columnar alignment - I found "inward" to be the most intuitive.  
row-to-rotation mapping - I found default reasonable.  
require2taps - useful when learning the keys for certain placements. Effectively 2kf when you have this on.  
.  
I haven't made any real changes to this script. Just uploading for preservation's sake along with transparency to anyone interested in looking into how I play 1kf.

Putting tetrio related scripts in tetrio folder. Mainly stuff that involves interacting with tetrio API.