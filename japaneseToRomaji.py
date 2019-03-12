# coding=utf-8
import MeCab
from pykakasi import kakasi,wakati
import json

## Prepare the libs
mecab_tagger = MeCab.Tagger("")

kakasi = kakasi()
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion

## Prepare the input text
#text = u"ずっと前から言っていた"

input = u"""
ずっと前から言っていた
あーだのこーだの愛されたい
ずっと前から言っていた
安心探して粗探し
ずっと前から知っていた
好きと嫌いの取っ組み合い
「ずっと前から知っていた。」
みたいだって話したあの日
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれない
どうして
純情
論争
あなたのそういうところが嫌いです
やかましいし騒がしいし
好きも嫌いもあなた次第
ずっと前から知っていた
いやよいやよも好きのうち
ずっと前から知っていた
狂ったふりしてすっからかん
ずっと前から知っていた
狐につままれたら気付けって
嘘の自分で好かれるよりもホントの自分で嫌われよう
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれない
どうして
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも素直になれない嫌い嫌いと言ってないで
だってだって大大嫌いになってもまた思い出して
相思相愛そうそうにない想像して溺れちゃって
だから
純情
論争
あなたのそういうところが嫌いです
やかましいし騒がしいけど
だけどそんなに嫌いじゃない
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも嫌いになれないどうして
純情
論争
あなたのそういうところが嫌いです
嫌いです
でも素直になれない嫌い嫌いと言ってないで
だってだって毎回期待を裂いてはまたなぞっちゃって
好機到来
構想未来
行動して求めちゃって
だから
純情
論争
あなたのそういうところが嫌いです
狂おしいほど悩ましいけど
だけどそんなに嫌いじゃない
狂おしいほど噛みしめたい
"""

class JapaneseToRomaji():

    def convert(self, input):
        lines = input.splitlines()

        ## Prepare response with dict
        romanized = []

        for line in lines:
            text = line
            parsed = [[chunk.split('\t')[0], tuple(chunk.split('\t')[1].split(','))] for chunk in mecab_tagger.parse(text).splitlines()[:-1]]

            ## Parse
            romanizedLine = []
            for i in parsed:
                #now for each i[0] do romaji
                conv = kakasi.getConverter()
                result = conv.do(i[0])
                romanizedLine.append(result)

            pair = {}
            pair[text] = " ".join(romanizedLine); 
            romanized.append(pair)

        return romanized
#        return json.dumps(romanized, ensure_ascii=False)



# toRomaji = JapaneseToRomaji()
# jsonRomanized = toRomaji.convert(input)
# print(jsonRomanized)
