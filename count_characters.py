from collections import defaultdict
from collections import Counter

def count_characters2(string2):
    count_dict2 = defaultdict(int)
    for c in string2:
        count_dict2[c] += 1
    print(count_dict2)

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters('Dynasty')
count_characters('12345anagram')
count_characters2('Dynasty')
count_characters2('12345anagram')
print(Counter('Dynasty'))
input()
