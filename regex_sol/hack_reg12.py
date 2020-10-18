import re

'''
Excluding specific character
'''

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.,]$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())