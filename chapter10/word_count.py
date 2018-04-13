"""计算一本书中单词个数"""

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        #可以使用pass语句占位表示捕获异常时什么都不做
        pass
    else:
        #计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("单词数:" + str(num_words))

count_words('alice.txt')
