import random
import string
from random import randint, choice
from string import ascii_lowercase
from collections import defaultdict

def merge(dicts):
    helper = defaultdict(lambda: [-1, -1, 0])  # key -> max, index_max, count
    #print(helper)
    for i, d in enumerate(dicts, 1):  # start indexing at 1
        for k, v in d.items():
            #print('inital helper', helper)
            helper[k][2] += 1  # always increase count
            #print('after increment helper' , helper)
            if v > helper[k][0]:
                #print('thedfgthekrtbttj' , v ,helper[k][0])
                helper[k][:2] = [v, i]  # update max and index_max
            #print('inner' , helper)
    #print('outer' , helper)
    
    # build result from helper data structure
    #print(helper)
    result = {}
    for k, (max_, index, count) in helper.items():
        key = k if count == 1 else "{}_{}".format(k, index)
        result[key] = max_
    return result


#rand_list = [{random.choice(string.ascii_lowercase): randint(0, 100) for i in range(5)} for j in range(randint(2,8))]

rand_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]

result  = merge(rand_list)



print(rand_list)
print(result)