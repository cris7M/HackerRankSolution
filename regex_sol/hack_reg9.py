'''
Forward Reference
'''

import re


Regex_Pattern = r'^(\2tic|(tac))+$'	


print(str(bool(re.search(Regex_Pattern, input()))).lower())