def isPowerOfThree(n):
    while (n != 1):
        if (n % 3 != 0):
            return False
        n = n // 3
    else:
        return True


print(isPowerOfThree(27))
print(isPowerOfThree(21))
