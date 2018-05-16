def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

print(anagram('Iceman1', 'Cinema12'))
print(anagram('Iceman12', 'Cinema12'))
input()
