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


def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i]
        for j in range(0, i):
            word = text[j: i+1]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
                    break
        word_list.append(longest_word)
        i -= len(longest_word)
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()
    print(backward_segment('商品和服务', dic))
