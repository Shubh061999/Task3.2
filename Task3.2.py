Input = [['car', 'face'], ['bikes', 'face'], ['bmw', 'allObj'], ['truck', 'logo'], ['van', 'action'],
         ['cycle', 'allOther']]

Output = {}

for item in Input:
    key = item[1]
    value = item[0]

    if key in Output:
        Output[key].append(value)
    else:
        Output[key] = [value]

print(Output)

