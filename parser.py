from collections import defaultdict
dict1 = defaultdict(int)
def parser(fname):
    dict1 = defaultdict(int)
    with open(fname) as f:
        for line in f:
            for char in line:
                dict1[char] += 1
    return sorted(dict1.items(), key=lambda d: d[1])[:8]

#
# with open("symbols.txt") as f:
#     for line in f:
#         for char in line:
#             dict1[char] += 1
#
# print(sorted(dict1.items(), key=lambda d:d[1])[:8])



print(parser('symbols.txt'))


