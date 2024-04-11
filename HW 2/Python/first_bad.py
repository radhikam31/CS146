def first_bad_version(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1

    return left

def is_bad_version(version):
    first_bad_version = 4  
    return version >= first_bad_version

if __name__ == "__main__":
    n = 5 
    print("First bad version:", first_bad_version(n))

# Output: First bad version: 4