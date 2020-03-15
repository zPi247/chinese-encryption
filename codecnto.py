import json


# 密码
def passkey():
    password = input("密钥:")
    a = json.dumps(password)
    b = a[3:len(a)-1]
    num = int(b, 16)
    if num < 10000:
        return num
    else:
        return int(num/10)


# 输入文本
alltext = input("输入需转换文本：")

# 列表
l1 = []
l2 = []
result = ''
key = passkey()

# 变为unicode
for character in alltext:
    character_in_code = json.dumps(character)
    if len(character_in_code) > 3:
        l1.append(character_in_code[3:len(character_in_code)-1])

# 改变数字
for all_code in l1:
    num = int(all_code, 16)
    l2.append("\\u"+hex(num-key)[2:6])

# 转换回汉字
for i in l2:
    result += i.encode('utf-8').decode('unicode_escape')

# 打印解密后文本
print(result)

