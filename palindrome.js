/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
	var reverse = x.toString().split("").reverse().join("");
	return reverse === x.toString() ? true : false;
};

var x = -12321;

console.log(isPalindrome(x));
