# coding=utf-8
import MeCab
from pykakasi import kakasi,wakati

## Prepare the libs
mecab_tagger = MeCab.Tagger("")

kakasi = kakasi()
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion

## Prepare the input text
text = u"ずっと前から言っていた"
parsed = [[chunk.split('\t')[0], tuple(chunk.split('\t')[1].split(','))] for chunk in mecab_tagger.parse(text).splitlines()[:-1]]

## Prepare response with dict
romanized = []

## Parse
for i in parsed:
    #now for each i[0] do romaji
    conv = kakasi.getConverter()
    result = conv.do(i[0])
    
    pair = {}
    pair[i[0]] = result;
    
    romanized.append(pair)
    
    # print(i[0])
    # print(result)

print(romanized)
