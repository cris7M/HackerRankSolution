import re

String = input()

print(re.match(r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$', String))

