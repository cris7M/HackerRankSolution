import re

'''
Matching specific Charecter
'''
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())