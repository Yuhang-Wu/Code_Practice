
def maxPalindrome(string):
    """ Find the max length of palindrome """

    # an empty string
    if (string == None) or (len(string) == 0) or (len(string) == 1):
        return len(string)

    newString = "#" + "#".join(list(string)) + "#"

    result = []
    for i in range(len(newString)):
        max_len = 0

        for j in range(1, len(newString) - i):
            if newString[i - j] == newString[i + j]:
                max_len += 1
        result.append(max_len)
    return max(result)
