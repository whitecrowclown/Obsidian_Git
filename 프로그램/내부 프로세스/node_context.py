import markdown

file = open("C:\\Users\\ssmma\\Documents\\신성민\\open.md", "r", encoding = "utf8")
content = file.read()
print(len(content))
print(content)
file.close()