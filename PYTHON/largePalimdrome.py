# CRAZY
"""
Dada una cadena, encuentra la subcadena palindrómica más larga.

Input: "babad"
Output: "bab" o "aba"
"""
def isPalindrome(txt):
    return txt == txt[::-1]


def allSubStrings(txt):
    substrings = []

    for i in range(len(txt)):
        for j in range(i + 1, len(txt) + 1):
            substrings.append(txt[i:j])

    substrings.sort(key=len, reverse=True)
    return substrings


def searchLargestPalindrome(txt):
    _subStr = allSubStrings(txt)

    for i in _subStr:
        if isPalindrome(i):
            print("Palindromo más largo: ", i)
            break

_word = "babad"
searchLargestPalindrome(_word)
