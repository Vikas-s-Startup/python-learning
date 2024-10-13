# s1 = aaabbacbccddefgg
# s2 = abbabaaccdcdeeff
#
# list
# the
# characters
# which
# has
# same
# frequency


s1 = 'aaabbacbccddefgg'
s2 = "abbabaaccdcdeeff"

char_count_map_s1 = {}
char_count_map_s2 = {}


for char in s1:
    if char in char_count_map_s1.keys():
        char_count_map_s1[char] +=1
    else:
        char_count_map_s1[char] = 1

for char in s2:
    if char in char_count_map_s2.keys():
        char_count_map_s2[char] +=1
    else:
        char_count_map_s2[char] = 1

print("String1 Values")
for key, value in char_count_map_s1.items():
    print(key, value)

print("===================================")

print("String2 Values")
for key, value in char_count_map_s2.items():
    print(key, value)


# calculate frequence

for s1_key, s1_value in char_count_map_s1.items():
        if s1_key in char_count_map_s2.keys():
            if s1_value == char_count_map_s2[s1_key]:
                print(f"{s1_key} found and values match and the value is {char_count_map_s1[s1_key]}")

# i94, DL, SSN #, Passport. H1 last extension copy.