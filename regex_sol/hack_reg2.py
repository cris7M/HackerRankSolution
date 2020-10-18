import re

string = "123.456.abc.def"
print(len(string))
print(re.match(r'^...\....\....\....$',string))