def pig_latin(string):
    for i in string:
        if i[0] in 'aeiou':
            return string + 'ay'
        return string[1:]+string[0] + 'ay'
p=pig_latin('apple')
print(p)
