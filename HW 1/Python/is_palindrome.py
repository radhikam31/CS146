def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())  
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    string = "A man, a plan, a canal, Panama!"
    print(f"Is \"{string}\" a palindrome? {is_palindrome(string)}")
#Output: Is "A man, a plan, a canal, Panama!" a palindrome? True