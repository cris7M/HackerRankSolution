import re

regex_St = r'hackerrank'
test_String = input()
# pattern = re.compile(regex_St)

print(len(re.findall(regex_St, test_String)))