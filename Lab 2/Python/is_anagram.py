def is_anagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(f"Is \"{t}\" an anagram of \"{s}\"? {is_anagram(s, t)}")

# Output: Is "nagaram" an anagram of "anagram"? True