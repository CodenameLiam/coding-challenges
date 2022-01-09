# Given a roman numeral, convert it to an integer.



class Solution:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    romanBefore = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        num = 0
        index = 0
        
        # ------------------------------ Skip iterations ----------------------------- #
        # while index < len(s) - 1:
        #     two = s[index] + s[index + 1] 
        #     if two in self.romanBefore:
        #         num += self.romanBefore[two]
        #         index += 2
        #     else:
        #         num += self.roman[s[index]]
        #         index += 1
        
        # return num + self.romanCovertDict[s[index]]


        # ------------------ Better solution just taking away value ------------------ #
        # for i in range(0, len(s) - 1):
        #     if self.roman[s[i]] < self.roman[s[i+1]]:
        #         num -= self.roman[s[i]]
        #     else:
        #         num += self.roman[s[i]]

        # return num + self.roman[s[-1]]


        # ------------------------------ Cooked solution ----------------------------- #
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        return sum(map(self.roman.get, s))




print(Solution().romanToInt('MCMXCIV'))