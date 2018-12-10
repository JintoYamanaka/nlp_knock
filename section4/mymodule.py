import MeCab
import collections

def create_morphemes():
    with open("neko.txt.mecab") as parsed_file:
        morphemes = [] # 一文ごとの形態素解析のリスト
        one_sentence_morphemes = [] # 一文の形態素解析（一単語ずつのリスト）
        for line in parsed_file:
            '''
            mecabの出力フォーマットは
            表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            '''
            cols = line.split("\t")

            # 最終行到達
            if len(cols) < 2:
                break

            res_cols = cols[1].split(",")

            one_sentence_morpheme = {  # 一単語の形態素解析
                "surface":cols[0],
                "base":res_cols[6],
                "pos":res_cols[0],
                "pos1":res_cols[1]
            }

            one_sentence_morphemes.append(one_sentence_morpheme)

            # 一文ずつ出力
            if cols[0] == "。":
                morphemes.append(one_sentence_morphemes)
                one_sentence_morphemes = []

    return morphemes

def create_words(morphemes, mode="sorted"):
    words = []
    for morpheme in morphemes:
        for line in morpheme:
            words.append(line["surface"])
    
    if mode == "sorted":
        words_count = collections.Counter(words)
        return words_count.most_common()
    else:
        return words
