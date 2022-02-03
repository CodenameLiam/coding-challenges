import string

def caesarCipher(s, k):

    alphabets = (string.ascii_lowercase, string.ascii_uppercase)

    def shift(alphabet):
        return alphabet[k:] + alphabet[:k]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)

    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return s.translate(table)


def caesarCipher2(s, k):
    k %= 26
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    key = dict(zip(lower, lower[k:] + lower[:k])) | dict(zip(upper, upper[k:] + upper[:k]))
    return s.translate(s.maketrans(key))

s = "There's-a-starman-waiting-in-the-sky"
k = 3

# print(caesarCipher2(s, k))


print("".join(reversed(s)))

