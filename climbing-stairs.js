var climbStairs = function (n) {
    let countStairs = (stairsRemaining, stairsMap) => {
        // No valid results
        if (stairsRemaining < 0) {
            return 0;
        }

        // One valid result
        if (stairsRemaining === 0) {
            return 1;
        }

        // Number of valid results is stored in the map
        if (stairsMap[stairsRemaining]) {
            return stairsMap[stairsRemaining];
        }

        // Number of valid responses is the total number of valid responses for the ;eft and right hand sides of the tree for a given onde in the map
        stairsMap[stairsRemaining] =
            countStairs(stairsRemaining - 1, stairsMap) + countStairs(stairsRemaining - 2, stairsMap);

        // Return the valid result calculated from the map
        return stairsMap[stairsRemaining];
    };

    return countStairs(n, {});
};

console.log(climbStairs(9));
