import os

# 기본 위치
path = "C:\\Users\\ssmma\\Documents\\신성민\\데이터"
file_list = os.listdir(path)
for file in file_list:
    print("*", file, "*")

# 선택 위치
select = input("어떤 파일을 확인하시겠습니까? ")
seleceted_file = file_list[int(select) - 1]
print(seleceted_file)
path = path + "\\" + seleceted_file

# 총 합 결과
file_list = os.listdir(path)
print(file_list)