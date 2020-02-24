book_author_dict = {
    '朝花夕拾':'鲁迅',
    '繁星春水':'冰心',
    '骆驼祥子':'老舍',
    '西游记':'吴承恩',
    '水浒传':'施耐庵',
    '三国演义':'罗贯中'
}



# list和dict的嵌套使用
# 书籍的名称、作者、价格、出版社
# 一个字点就能表示一本书了
book_dict_01 = {'name':'朝花夕拾', 'author':'鲁迅',
             'price':'39.9', 'publish':'北京大学出版社'
}
book_dict_02 = {'name':'朝花夕拾', 'author':'鲁迅',
             'price':'39.9', 'publish':'北京大学出版社'
}
book_dict_03 = {'name':'朝花夕拾', 'author':'鲁迅',
             'price':'39.9', 'publish':'北京大学出版社'
}

# 如何表示多本书

book_list = [book_dict_01, book_dict_02, book_dict_03]
