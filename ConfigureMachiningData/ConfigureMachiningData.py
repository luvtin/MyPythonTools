import re
import os

# 打开文件
read_txt = open("MachiningData.txt", "r", encoding='utf-8')
# 读取所有行
lines = read_txt.readlines()
# 创建一个新的列表
new_lines = []

# 指定要检索的文件夹路径
file_path = "FIVE_AXIS"
# 获取该路径下的所有文件或文件夹的名字
files_Name = os.listdir(file_path)
# 创建一个新的文件名列表
new_files_Name = []

# 遍历文件列表
for file_name in files_Name:
    # 将排除掉文件类型的文件名加入新的列表中
    new_files_Name.append(file_name.split(".")[0])

# 遍历每一行
for line in lines:
    # 正则表达式：
    # [ 匹配左方括号
    # \s* 匹配零个或多个空白字符
    # +? 匹配零个或一个加号
    # (-?\d+) 匹配一个可选的负号和一个或多个数字，并捕获为一个分组
    # \s* 匹配零个或多个空白字符
    # ] 匹配右方括号
    res = re.findall(r"\[\s*\+?(-?\d+)\s*\]", line)
    # 如果[]内的数字能在new_files_Name列表中找到
    if res[0] in new_files_Name:
        # 直接赋值原始值
        new_line = line
    else:
        # 将原始值中的FN替换为FN.
        new_line = line.replace("FN", "FN.")
    # 添加到新的列表中
    new_lines.append(new_line)

# 打开文件
write_txt = open('NewMachiningData.txt', 'w', encoding='utf-8')
# 写入新的列表
write_txt.writelines(new_lines)

# 关闭两个文件
read_txt.close()
write_txt.close()
