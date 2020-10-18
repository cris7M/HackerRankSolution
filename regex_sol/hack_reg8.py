'''
Branch Reset Group
'''

import re
# '''
# Backreferences To Failed Groups

# '''


Regex_Pattern = r'^\d{2}((\.)|(:)|(-)|(---))\d{2}\1\d{2}\1\d{2}$'	


print(str(bool(re.search(Regex_Pattern, input()))).lower())