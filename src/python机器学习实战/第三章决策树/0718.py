# AUTHOR lijixin


# list01=[('a',1),('a',2),('b',1),('b',2)]
#
# [('a'),[1,2],('b'),[1,2])]

# list01=[('a',1),('a',2),('b',1),('b',2)]
# list =zip(*list01)
# print(list)
# # print(list[0][0])


from collections import defaultdict

def merge_final_values(values):
    mergeddict = defaultdict(list)
    print(type(mergeddict))
    for group in values:
        # print(group[:-1])
        # print(type(group[:-1]))
        mergeddict[group[:-1]].append(group[-1])
    return [(k + (list(v),) if len(v) > 1 else k+(list(v),))
            for k, v in mergeddict.items()]
list01=[('a',1),('a',2),('b',1),('b',2),('c',2)]
# test = [(1, 2, 'R'), (1, 3, 'S'), (1, 2, 'S'), (2, 3, 'S')]

print(merge_final_values(list01))