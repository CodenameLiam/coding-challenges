// Brute force
// var twoSum = function (nums, target) {
// 	for (var i = 0; i < nums.length; i++) {
// 		for (var j = 1; j < nums.length; j++) {
// 			if (i !== j && nums[i] + nums[j] == target) {
// 				return [i, j];
// 			}
// 		}
// 	}
// };

// Hashmap
const twoSum = (nums, target) => {
	const map = new Map(nums.slice().map((val, idx) => [val, idx]));

	for (let i = 0; i < nums.length; i++) {
		const index = map.get(target - nums[i]);

		if (index && index !== i) {
			return [i, index];
		}
	}
	return [];
};

const nums = [2, 5, 5, 11];
const target = 10;
const answer = twoSum(nums, target);

console.log(answer);
