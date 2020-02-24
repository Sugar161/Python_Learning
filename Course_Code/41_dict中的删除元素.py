book_author_dict = {
    '朝花夕拾':'鲁迅',
    '繁星春水':'冰心',
    '骆驼祥子':'老舍',
    '西游记':'吴承恩',
    '水浒传':'施耐庵',
    '三国演义':'罗贯中'
}

# dict增加元素

book_author_dict['红楼梦'] = '曹雪芹'

for book, author in book_author_dict.items():
    print('著作：%s -- 作者：%s' % (book, author))

print('--------------------------')

print(book_author_dict)

print('--------------------------------------------------------------------------------')

# dict中的删除元素
# list : pop()
# dict中的pop() : 是根据key，来删除整个键值对

book_author_dict.pop('红楼梦')
print(book_author_dict)
