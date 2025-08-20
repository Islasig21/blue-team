'''import re
re.findall()
re.compile
re.split
re.sub
re.search
'''

import re
string = "Hello my number is 123456789 and my friend's number is 987654321"

regex = (r'\d+')
match = re.findall(pattern=regex, string=string)

print(match)
p = re.compile(r'\d)')
p_more = re.compile(r'\d+)')
p_word = re.compile(r'\w\)')
p_word_plus = re.compile(r'\W+')
p_word_big = re.compile(r'\W')
p_start = re.compile(r'\we*')
find = p_start.findall("ababbaabbb")
print(find)