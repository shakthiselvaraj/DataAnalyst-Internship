# Regular Expression (RegEX)

import re

pattern = '^a...s$'
string = 'aedfs'
ans = re.match(pattern, string)

if ans:
    print('Pattern Correct!')

else:
    print('Pattern Incorrect!')


string1 = 'hey10 hi 23hello'
pattern1 = '\d+'
ans1 = re.split(pattern1, string1)
print(ans1)

