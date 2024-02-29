# 打开原始txt文件
read_txt = open('ProgramCode.txt', 'r', encoding='utf-8')
# 按行读取文件内容
lines = read_txt.readlines()
# 给每行添加序号
lines = enumerate(lines, start=1)

# 打开新的txt文件
write_txt = open('NewProgramCode.txt', 'w', encoding='utf-8')

# 遍历每行并写入新文件
for num, line in lines:
    # 拼接序号和内容
    new_line = str(num) + ' ' + line
    # 写入新文件
    write_txt.write(new_line)

# 关闭两个文件
read_txt.close()
write_txt.close()
