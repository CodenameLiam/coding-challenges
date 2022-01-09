
const pigLatin = (input) =>  input.substring(1, input.length) +  input[0] + (/^[aeiou]$/i.test(input[0]) ? "way" : "ay");




console.time();
pigLatin("Zach");
console.timeEnd();

console.log(pigLatin("hello"));

function toPigLatin(str) {
    // person -> //ersonpay
    return ['a','e','i','o','u'].find(e => e === str[0]) === undefined ? str.substring(1,str.length) + str[0] + 'ay' : str + 'way';
}

console.time();
toPigLatin('Zach');
console.timeEnd();