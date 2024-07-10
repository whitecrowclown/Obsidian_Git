file = open("C:\\Users\\ssmma\\Documents\\신성민\\데이터\\기타\\close.md", "r", encoding = "utf8")
content = file.read()
if len(content) == 0:
    print("Empty")
file.close()