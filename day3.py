input = open("/home/fati/Desktop/input3").read()


from itertools import zip_longest

def bitPolarity(strings):
    polarity = []
    for string in strings:
        polarity = [
            s + (1 if x == '1' else -1)
            for s, x in zip_longest(polarity, string, fillvalue=0)
        ]
    return polarity

polarity = bitPolarity(input.splitlines())

gamma = sum([2**i for i, x in enumerate(reversed(polarity)) if x > 0])
epsilon = sum([2**i for i, x in enumerate(reversed(polarity)) if x < 0])
print(gamma * epsilon)



def getRating(condition, values):
    i = 0
    while True:
        v = condition(bitPolarity(values)[i])
        j = len(values) - 1
        for value in reversed(values):
            if value[i] != v: values.pop(j)
            if len(values) == 1: return int(values[0], 2)
            j -= 1
        i += 1

values = input.splitlines()
oxygen_gen_rating = getRating(lambda c: '1' if c >= 0 else '0', values.copy())
co2_scrubber_rating = getRating(lambda c: '0' if c >= 0 else '1', values.copy())

print(oxygen_gen_rating * co2_scrubber_rating)
