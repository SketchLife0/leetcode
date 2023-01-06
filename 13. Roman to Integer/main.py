def romanToInt(s: str) -> int:
    elems = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
    result = 0
    skip = -1
    for i in range(len(s)):
        if i == skip:
            continue
        if i+1 < len(s) and elems[s[i]] < elems[s[i+1]]:
            result += elems[s[i+1]] - elems[s[i]]
            skip = i+1
        else:
            result += elems[s[i]]
    return result


# def romanToInt(s: str) -> int:
#     dic = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }
#     total = 0
#     prev = 0
#     for i in range(len(s)):
#         curr = dic[s[i]]
#         if curr > prev:
#             total += curr - 2 * prev
#         else:
#             total += curr
#         prev = curr
#     return total


print(romanToInt("MCMXCIV"))
