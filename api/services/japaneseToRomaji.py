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

class JapaneseToRomaji():

    def convert(self, input):
        lines = input.splitlines()

        ## Prepare response with dict
        romanized = []

        for line in lines:
            text = line
            chunked = [chunk.split('\t')[0], tuple(chunk.split('\t')[1].split(','))]
            parsed = [chunked for chunk in mecab_tagger.parse(text).splitlines()[:-1]]

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


