from pyhanlp import *


def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())


def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            word = text[i:j]
            if word in dic:
                word_list.append(word)
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()
    print(fully_segment('商品和服务', dic))
