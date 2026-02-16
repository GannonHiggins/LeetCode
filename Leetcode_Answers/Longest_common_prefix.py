'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


SOLVED
runtime 3ms
memory 12.9 MB
'''

def longest_common_prefix(strs):
    min_length = float('inf')

    for s in strs:
        if len(s) < min_length:
            min_length = len(s)
    
    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return strs[0][:i]
        i += 1
    return strs[0][:i]

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["apple", "app", "apricot"]))
print(longest_common_prefix(["apple", "banana", "cherry"]))
print(longest_common_prefix(["apple", "banana", "cherry"]))