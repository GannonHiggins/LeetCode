def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["apple", "app", "apricot"]))
print(longest_common_prefix(["apple", "banana", "cherry"]))
print(longest_common_prefix(["apple", "banana", "cherry"]))