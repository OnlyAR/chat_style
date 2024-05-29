import wordcloud
from reader import read_messages
from analyze import corpus2list, clean_stopwords

username = 'XXX'
user_alias = {
    username: [
        'aaa',
    ]
}


def draw(username):
    corpus = read_messages(user_alias)
    word_lst = corpus2list(username, corpus)
    word_lst = clean_stopwords(word_lst)
    wc = wordcloud.WordCloud(
        font_path='fonts/SimHei.ttf',
        background_color='white',
        width=1000,
        height=800,
        max_font_size=100,
        min_font_size=20,
        max_words=1000,
        collocations=False
    )
    wc.generate(' '.join(word_lst))
    wc.to_file('images/{}.png'.format(username))


if __name__ == '__main__':
    draw(username)
