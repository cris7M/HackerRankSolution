import re
# '''
# Backreferences To Failed Groups

# '''


Regex_Pattern = r'^(\d{8}|\d{2}-\d{2}-\d{2}-\d{2})$'	

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())