let longestCommonPrefix = function (strs) {
    let longest = "";

    if (strs.length === 0) {
        return longest;
    }

    let comparisonWord = strs[0];

    for (const [comparisonIndex, comparisonLetter] of [...comparisonWord].entries()) {
        for (const currentWord of strs.slice(1)) {
            if (comparisonLetter !== currentWord[comparisonIndex] || comparisonIndex > currentWord.length) {
                return longest;
            }
        }

        longest += comparisonLetter;
    }

    return longest;
};

let test1 = ["flower", "flowington", "floght", "flit", "floweron"];

let test2 = ["dog", "racecar", "car"];

console.time("longestCommonPrefix");
console.log(longestCommonPrefix(test1));
console.timeEnd("longestCommonPrefix");

var longestCommonPrefix2 = function (strs) {
    "use strict";
    if (strs === undefined || strs.length === 0) {
        return "";
    }

    return strs.reduce((prev, next) => {
        let i = 0;
        while (prev[i] && next[i] && prev[i] === next[i]) i++;
        return prev.slice(0, i);
    });
};

console.time("longestCommonPrefix");
console.log(longestCommonPrefix2(test1));
console.timeEnd("longestCommonPrefix");
