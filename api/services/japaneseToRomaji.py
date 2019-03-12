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
            chunklines = mecab_tagger.parse(text).splitlines()[:-1]

            parsed = [[chunk.split('\t')[0], tuple(chunk.split('\t')[1].split(',')) ] for chunk in chunklines]


            ## Parse
            romanizedLine = []
            for i in parsed:
                #now for each i[0] do romaji
                conv = kakasi.getConverter()
                finalResult = None

                result1 = None
                if len(i) == 2 and len(i[1]) > 8:
                    result1 = conv.do(i[1][7])

                result2 = conv.do(i[0])

                if result1 == None:
                    finalResult = result2
                elif result1 != None and result2 != result1:
                    finalResult = result1
                else:
                    finalResult = result2


                romanizedLine.append(finalResult)


            pair = {}
            romanizedLine.append(" ")
            romanizedLine = " ".join(romanizedLine)

            romanizedLine = romanizedLine.replace(" ha ", " wa ")

            ## Collapse っ
            #k
            romanizedLine = romanizedLine.replace("tsu ka ", "tsuka")
            romanizedLine = romanizedLine.replace("tsu ke ", "ke")
            romanizedLine = romanizedLine.replace("tsu ki ", "kki")
            romanizedLine = romanizedLine.replace("tsu ko ", "kko")
            romanizedLine = romanizedLine.replace("tsu ku ", "kku")

            ## Collapse っ
            #s
            romanizedLine = romanizedLine.replace("tsu sa ", "ssa")
            romanizedLine = romanizedLine.replace("tsu se ", "sse")
            romanizedLine = romanizedLine.replace("tsu si ", "ssi")
            romanizedLine = romanizedLine.replace("tsu so ", "sso")
            romanizedLine = romanizedLine.replace("tsu su ", "ssu")

            ## Collapse っ
            #t
            romanizedLine = romanizedLine.replace("tsu ta ", "tta")
            romanizedLine = romanizedLine.replace("tsu te ", "tte")
            romanizedLine = romanizedLine.replace("tsu ti ", "tti")
            romanizedLine = romanizedLine.replace("tsu to ", "tto")
            romanizedLine = romanizedLine.replace("tsu tu ", "ttu")

            ## Collapse っ
            #p
            romanizedLine = romanizedLine.replace("tsu pa ", "ppa")
            romanizedLine = romanizedLine.replace("tsu pe ", "ppe")
            romanizedLine = romanizedLine.replace("tsu pi ", "ppi")
            romanizedLine = romanizedLine.replace("tsu po ", "ppo")

            ## Dangling letters
            romanizedLine = romanizedLine.replace(" u ", "u ")
            romanizedLine = romanizedLine.replace(" i ", "i ")

            ## Other fixes, after tsu particle
            romanizedLine = romanizedLine.replace(" nai ", "nai ")
            romanizedLine = romanizedLine.replace(" ta ", "ta ")
            romanizedLine = romanizedLine.replace(" te ", "te ")
            romanizedLine = romanizedLine.replace(" ten ", "ten ")
            romanizedLine = romanizedLine.replace(" ku ", "ku ")
            romanizedLine = romanizedLine.replace(" ba ", "ba ")
            romanizedLine = romanizedLine.replace(" ka ", "ka ")
            romanizedLine = romanizedLine.replace(" ze ", "ze ")
            romanizedLine = romanizedLine.replace(" ga ", "ga ")
            romanizedLine = romanizedLine.replace(" re ", "re ")

            ## Remove multiple spaces
            romanizedLine = romanizedLine.strip()
            romanizedLine = " ".join(romanizedLine.split())

            pair[text] = romanizedLine.strip()
            romanized.append(pair)

        return romanized


