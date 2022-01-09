/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
	let int = 0;

	for (let i = 0; i < s.length; i++) {
		let val1 = value(s[i]);

		if (i + 1 < s.length) {
			let val2 = value(s[i + 1]);

			if (val1 >= val2) {
				int += val1;
			} else {
				int += val2 - val1;
				i++;
			}
		} else {
			int += val1;
			i++;
		}
	}
	return int;
};

var value = function (s) {
	switch (s) {
		case "I":
			return 1;
		case "V":
			return 5;
		case "X":
			return 10;
		case "L":
			return 50;
		case "C":
			return 100;
		case "D":
			return 500;
		case "M":
			return 1000;
		default:
			return -1;
	}
};

var s = "MMMCMDVI";

console.log(romanToInt(s));
