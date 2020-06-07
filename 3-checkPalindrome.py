def checkPalindrome(inputString):
    t = inputString[::-1]
    if t == inputString:
        return True
    else:
        return False