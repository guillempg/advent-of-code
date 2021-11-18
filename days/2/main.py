def isValidPassword(character, atLeast, noMoreThan, password):
    #print("password:", password, "character:", character, "count:", password.count(character))
    if (password.count(character) < int(atLeast) or
            password.count(character) > int(noMoreThan)):
        return False
    else:
        return True

if __name__ == '__main__':
    with open('input') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    #print("values:", lines)
    ## Example '9-10 m: mmmmnxmmmwm'
    passwordToRule = {}
    invalid = 0
    print("There are ", len(lines), " passwords")
    for count, line in enumerate(lines):
        passwordToRule[count] = {}
        line.rstrip()
        line.lstrip()
        line = line.replace(':', '')
        #print("Line after remove colon:", line)
        fields = line.split(' ')
        times = fields[0].rstrip()
        minTimes = times.split("-")[0]
        maxTimes = times.split("-")[1]
        character = fields[1].replace(' ', '').rstrip()
        password = fields[2].replace(' ', '').rstrip()
        #print("MinTimes:", minTimes, "|MaxTimes:", maxTimes, "|Character:", character, "|Password:", password)

        if not isValidPassword(character, minTimes, maxTimes, password):
            print("charCount:", password.count(character), "line:", line)
            invalid = invalid+1
            print("Total valid passwords:", len(lines)-invalid)
