# 双向最长匹配：
# ①同时执行正向和逆向最长匹配，若两者的词数不同，则返回词数更少的那一个
# ②否则，返回两者中单字更少的那一个。当单字数也相同，则优先返回逆向最长匹配的结果。
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


def forward_segment(text, dic):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]
        for j in range(+1, len(text) + 1):
            word = text[i: j]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.append(longest_word)
        i += len(longest_word)
    return word_list


def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i]
        for j in range(0, i):
            word = text[j: i + 1]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
                    break
        word_list.append(longest_word)
        i -= len(longest_word)
    return word_list


def count_single_char(word_list):
    return sum(1 for word in word_list if len(word) == 1)


def bidirectionl_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):
        return f
    elif len(b) < len(f):
        return b
    else:
        if count_single_char(f) < count_single_char(b):
            return f
        else:
            return b


if __name__ == '__main__':
    dic = load_dictionary()
    print(bidirectionl_segment('商品和服务', dic))
