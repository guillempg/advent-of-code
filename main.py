def pairs_with_summed_value(values, summed):
    output = []
    for v1 in values:
        for v2 in values:
            added = int(v1) + int(v2)
            print("added:", added)
            if (int(v1) != int(v2) and
                    added == summed):
                output.append(v1)
                output.append(v2)
    return output

def trios_with_summed_value(values, summed):
    output = []
    for v1 in values:
        for v2 in values:
            for v3 in values:
                added = int(v1) + int(v2) + int(v3)
                print("added:", added)
                if (int(v1) != int(v2) and
                    int(v2) != int(v3) and
                    int(v1) != int(v3) and
                    added == summed):
                    output.append(v1)
                    output.append(v2)
                    output.append(v3)
    return output

if __name__ == '__main__':
    with open('input') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    print("values:", lines)
    pairs = pairs_with_summed_value(lines, 2020)
    print("pairs:", pairs)
    for previous, current in zip(pairs, pairs[1:]):
        multiplied = int(previous)*int(current)
        print("Multiplying: ", previous, " with ", current, " gives:", multiplied)
    trios = trios_with_summed_value(lines, 2020)
    print("trios:", trios)
    for previous2, previous, current in zip(trios, trios[1:],trios[2:]):
        multipliedTrio = int(previous2) * int(previous) * int(current)
        print("Multiplying: ", previous2, " with ", previous, " with ", current, " gives:", multipliedTrio)

