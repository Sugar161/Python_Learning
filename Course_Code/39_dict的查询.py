# dict : dictionary 字典
# key : 键
# value : 值
# 键值对
book_author_dict = {
    '朝花夕拾':'鲁迅',
    '繁星春水':'冰心',
    '骆驼祥子':'老舍',
    '西游记':'吴承恩',
    '水浒传':'施耐庵',
    '三国演义':'罗贯中'
}

# dict的基本用法：增、删、改、、查
# 查询单个内容：是根据Key去查找Value
print(book_author_dict['朝花夕拾'])
print('------')
print(book_author_dict.get('朝花夕拾'))
print('------')

# 查找全部的key
for book in book_author_dict:
    print(book)
print('---------')

# 查找全部的key和全部的value
for book in book_author_dict:
    print('著作：%s--作者：%s' % (book, book_author_dict.get(book)))
print('--------------------------')

# 查找全部的key和value
for book, author in book_author_dict.items():
    print('著作：%s--作者：%s' % (book, author))
