import json
from pprint import pprint

#get tlds
f = open("namecheap-tlds.txt")

tlds_info = []
tlds_stripped_list = []
tlds_price_map = {}

for line in f:
    tlds_info.append(line.strip("\n"))

i = 0
for item in tlds_info:
    if i%2 == 0:
        stripped_tld = ''.join(e for e in item if e.isalnum()).lower()
        tlds_stripped_list.append(stripped_tld)
        next_item = stripped_tld 
    else: 
        if "€" not in item and "?" not in item:
            raise ValueError("not a price or question mark: " + item)
        tlds_price_map[next_item] = float(item.strip("€").replace(",","").replace("?","0"))
    i += 1


#get palindromes
palindromes_file = open("palindromes.txt")
palindromes_raw_list = palindromes_file.readlines()

palindromes_stripped = []
stripped_pal_map = {}

for p in palindromes_raw_list:
    stripped_pal = ''.join(e for e in p if e.isalnum()).lower()
    if stripped_pal not in palindromes_stripped:
        stripped_pal_map[stripped_pal] = p
        palindromes_stripped.append(stripped_pal)

#compare stripped palindromes and tlds
tld_pal_dict = {}
for tld in tlds_stripped_list:
    for pal in palindromes_stripped:
        if tld in pal:
            if not tld in tld_pal_dict:
                tld_pal_dict[tld] = []
                tld_pal_dict[tld].append(tlds_price_map[tld])
            tld_pal_dict[tld].append(stripped_pal_map[pal])


tld_sorted = sorted(tld_pal_dict, key=lambda a: tld_pal_dict[a][0])
tld_pal_dict_sorted = {}

for tld in tld_sorted:
    tld_pal_dict_sorted[tld] = tld_pal_dict[tld]
    print(tld)
    for x in tld_pal_dict[tld]:
        print(x)
    print("")
    y = input()


#print(tld_sorted)
#pprint(tld_pal_dict_sorted, sort_dicts=False)

