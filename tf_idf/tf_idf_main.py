#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
参考:https://www.jianshu.com/p/f3b92124cd2b
1.gensim库来计算tfidf值
2.sklearn库来计算tfidf值
3.python手动实现tfidf的计算
"""

corpus = [
    'this is the first document',
    'this is the second second document',
    'and the third one',
    'is this the first document'
]

def gensim_tfidf():
    from gensim import corpora
    # 空格分词
    word_list = []
    for i in range(len(corpus)):
        word_list.append(corpus[i].split(' '))
    print('空格分词:')
    print(word_list)
    # # 赋给语料库中每个词(不重复的词)一个整数id
    dictionary = corpora.Dictionary(word_list)
    new_corpus = [dictionary.doc2bow(text) for text in word_list]
    print('词典:')
    print(new_corpus)

def sklearn_tfidf():
    pass

def python_tfidf():
    pass


if __name__ == '__main__':
    gensim_tfidf()
    print('aa')