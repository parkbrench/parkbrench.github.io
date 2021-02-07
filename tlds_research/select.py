import json


with open('sorted.json', 'r') as fin:
    data = json.load(fin)


shorts = {}

for domain in data:
    shorts[domain] = dict()
    for i, d in enumerate(data[domain]):
        # breakpoint()
        if i == 0:
            shorts[domain]['price'] = d
            shorts[domain]['domains'] = list()
            # breakpoint()
            continue
        if len(d) < 20:
            shorts[domain]['domains'].append(d)
    if len(shorts[domain]['domains']) == 0:
        del shorts[domain]


with open('shorts.json', 'w') as fout:
    json.dump(shorts, fout, indent=4)