# tetrio related scripts

Lots of random stuff. A lot is kinda useless.

Not going to describe them all.

# download_tetrio_game.py
requires your account token in a .env file (not uploading mine here), and the replay ID given as an argument in cmd. Lol. Um, reccommend you use szy's [inoe API](https://inoue.szy.lol/api/) instead (github repo for inoe [here](https://github.com/szymonszl/inoue)).

# emotes.js
exerpt from tetrio source containing the data related to tetrio emotes. This is a really really old capture, it is probably outdated, I don't intend to regularly update this. Zudo maintains https://emotes.kagar.in/ and if that goes down [here's a backup](https://github.com/swng/TETR.IO-emote-list).

# find_badges.py
Was an attempt to look for secret badges by parsing through every accessible player using the exp leaderboard. No particularly novel secret badges were discovered. Be warned, this script uses an incredible number of API requests. Not viable. If you do want to run it, adjust `after` value accordingly.

# find_top_b2b_blitzer.py
Sorts blitz leaderboard by b2b chain. Obviously, blitz leaderboard only includes score PBs and doesn't include runs that aren't score PBs that may have higher b2b chains. Currently I'm #1 😎 - because most people PC loop and currently my competition broke b2b in their PBs.

# guess_blitz_method.py
an attempt to guess at the blitz method used based on line clears done in the run. Ratio cutoffs were arbitrarily set. With how much theory has progressed, the ratio cutoffs are likely inaccurate at this point. May rehaul this script in the future but at this point 99% of people are doing some form of optimized 8L - DPC loop /shrug

# thing.py
A lot of these are pretty dumb trivia stuff

# disputed_blitzers.py
Some scores are marked as disputed on the leaderboard. Who and why? Is the common denominator just tetrio+ or whatever? Curious.

# b2b_level_tetrio.js
At what b2b chain do certain "levels" start in tetrio attack table? Figure it out with binary search using tetrio damcalc function.