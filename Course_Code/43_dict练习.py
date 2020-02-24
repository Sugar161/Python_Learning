book_author_dict = {
    '朝花夕拾':'鲁迅',
    '繁星春水':'冰心',
    '骆驼祥子':'老舍',
    '西游记':'吴承恩',
    '水浒传':'施耐庵',
    '三国演义':'罗贯中'
}

# 查找冰心对应的著作是什么？

# 1.构建一个新的字典

# 2.新字典中:作者作为key，book作为value

# 3.查找作者对应的著作

# 定义一个空字典
author_book_dict = {}
# 将原字典中的书和作者的键值对颠倒之后存入新的字典
for book, author in book_author_dict.items():
    author_book_dict[author] = book

# 查找冰心对应的著作是什么？
print(author_book_dict['冰心'])
