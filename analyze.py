import jieba

stopwords_path = 'stopwords/cn_stopwords.txt'


def corpus2list(username, corpus):
    word_lst = []
    for item in corpus[username]:
        word_lst += jieba.lcut(item['content'].strip())
    return word_lst


def clean_stopwords(word_lst):
    stopwords = [line.strip() for line in open(stopwords_path, 'r', encoding='utf-8').readlines()]
    word_lst = [word for word in word_lst if word not in stopwords]
    return word_lst
