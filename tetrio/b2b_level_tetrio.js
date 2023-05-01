var assert = require('assert');

var tetrioatk = {
    garbage : {
        SINGLE: 0,
        DOUBLE: 1,
        TRIPLE: 2,
        QUAD: 4,
        TSPIN_MINI: 0,
        TSPIN: 0,
        TSPIN_MINI_SINGLE: 0,
        TSPIN_SINGLE: 2,
        TSPIN_MINI_DOUBLE: 1,
        TSPIN_DOUBLE: 4,
        TSPIN_TRIPLE: 6,
        TSPIN_QUAD: 10,
        BACKTOBACK_BONUS: 1,
        BACKTOBACK_BONUS_LOG: .8,
        COMBO_MINIFIER: 1,
        COMBO_MINIFIER_LOG: 1.25,
        COMBO_BONUS: .25,
        ALL_CLEAR: 10
    },
    b2b(btb){
        return tetrioatk.garbage["BACKTOBACK_BONUS"] * (Math.floor(1 + Math.log1p((btb) * tetrioatk.garbage["BACKTOBACK_BONUS_LOG"])) + (btb == 1 ? 0 : (1 + Math.log1p((btb) * tetrioatk.garbage["BACKTOBACK_BONUS_LOG"]) % 1) / 3))
    },
    calAtk(type,btb,cb){
        var atk = tetrioatk.garbage[type];
        if(btb > 0)  atk += tetrioatk.b2b(btb);
        atk *= 1 + tetrioatk.garbage["COMBO_BONUS"] * (cb);
        if(cb > 1) atk = Math.max(Math.log1p(tetrioatk.garbage["COMBO_MINIFIER"] * cb * tetrioatk.garbage["COMBO_MINIFIER_LOG"]), atk);
        return Math.floor(atk);
    }
}


function b2b_level_start(target_level) {
    assert(Number.isInteger(target_level));
    assert(target_level > 1);

    function binarySearch(max, min) {
        if (max == min || max == min+1) return max;

        let guess = Math.floor((max + min)/2);

        let b2b_level = tetrioatk.b2b(guess);

        if (b2b_level < target_level) min = guess;
        if (b2b_level > target_level) max = guess;

        return binarySearch(max, min);
    }

    let max = 1;
    while (tetrioatk.b2b(max) < target_level) max *= 2;

    let min = 1;

    return binarySearch(max, min);

    
}



for(let i = 2; i < 30; i++) {
    let res = b2b_level_start(i);
    console.log(`${i} at ${res}-chain`);
}