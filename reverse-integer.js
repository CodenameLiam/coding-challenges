/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
	const result = parseFloat(Math.abs(x).toString().split("").reverse().join(""));
	return result <= 2147483647 ? result * Math.sign(x) : 0;
};

var x = -2147483412;
var answer = reverse(x);

console.log(answer);
