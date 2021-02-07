import json

f = open("namecheap-tlds.txt")

tlds_info = []
tlds_list = []
tlds_price_dict = {}

for line in f:
    tlds_info.append(line.strip("\n"))

i = 0
for item in tlds_info:
    if i%2 == 0:
        tlds_list.append(item)
        next_item = item
    else: 
        if "\xe2\x82\xac" not in item and "?" not in item:
            raise ValueError("not a price:" + item)
        tlds_price_dict[next_item] = item
    i += 1

print(tlds_list)

print(tlds_price_dict)

f1 = open("tlds_list.txt", "w")

f1.write(json.dumps(tlds_list))
f1.close()

f2 = open("tlds_price_dict.txt", "w")
f2.write(json.dumps(tlds_price_dict))
f2.close()
