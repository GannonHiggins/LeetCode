def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]



print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(12321))
print(isPalindrome(1234567890))
print(isPalindrome(1234567890))