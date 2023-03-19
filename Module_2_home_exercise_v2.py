import random
import string
from random import randint, choice
from string import ascii_lowercase
from collections import defaultdict

def merge(dicts):
    helper = defaultdict(lambda: [-1, -1, 0])  # key -> max, index_max, count

    for i, d in enumerate(dicts, 1):  # start indexing at 1
        for k, v in d.items():           
            helper[k][2] += 1  # always increase count          
            if v > helper[k][0]:             
                helper[k][:2] = [v, i]  # update max and index_max
 # build result from helper data structure
    result = {}
    for k, (max_, index, count) in helper.items():
        key = k if count == 1 else "{}_{}".format(k, index)
        result[key] = max_
    return result


#Generate list of dictionary of random characters and numbers as key value pairs 
rand_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))] 

result  = merge(rand_list) #Function call



print(rand_list)
print(result)
