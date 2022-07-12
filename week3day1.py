import re

with open('files/regex_test.txt') as file: 
    data = file.readlines()
print(data)

pattern = re.compile('(\w*)\s(\w*\s)?(\w{5,10})$')

print('\n\nExpected Output:')
for line in data:
    match = pattern.match(line)
    if match:
        if match.group(2):
            print(f'{match.group(1)} {match.group(2)} {match.group(3)}')
        else:
            print(f'{match.group(1)}  {match.group(3)}')
    else:
        print(None) 