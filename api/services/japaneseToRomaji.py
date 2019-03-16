# coding=utf-8
import MeCab
from pykakasi import kakasi,wakati
import json
import re

## Prepare the libs
mecab_tagger = MeCab.Tagger("")

kakasi = kakasi()
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion

def is_number(s):
    """ Returns True is string is a number. """
    return s.replace('.','',1).isdigit()


def is_cjk(char):
    ranges = [
      {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
      {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
      {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
      {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
      {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
      {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
      {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
      {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
      {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
      {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
      {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
      {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
      {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
    ]    

    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])

def is_japanese(string):
    i = 0
    while i<len(string):
        if is_cjk(string[i]):
            return True
        i += 1

    return False    


class JapaneseToRomaji():

    def convert(self, inputText):

        input = inputText
        input = input.replace(" ", "**SPACE**")
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

                # ignore calculation if initial string is numeric
                if is_number(i[0]):
                    finalResult = ""+i[0]

                # ignore calculation if string has non JP chars
                if finalResult == None and is_japanese(i[0]) == False:
                    finalResult = i[0]                    

                if finalResult == None:    
                    result1 = None
                    if len(i) == 2 and len(i[1]) > 8:
                        result1 = conv.do(i[1][7])

                    result2 = conv.do(i[0])

                    if result1 == None:
                        finalResult = result2+" "
                    elif result1 != None and result2 != result1:
                        finalResult = result1+" "
                    else:
                        finalResult = result2+" "


                romanizedLine.append(finalResult)


            pair = {}    
            romanizedLine = "".join(romanizedLine)
                

            romanizedLine = romanizedLine.replace(" ha ", " wa ")

            ## Collapse っ
            #k
            romanizedLine = romanizedLine.replace("tsu ka ", "tsuka")
            romanizedLine = romanizedLine.replace("tsu ke ", "kke")
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

            ## Extended letters
            romanizedLine = romanizedLine.replace("a-", "ā")
            romanizedLine = romanizedLine.replace("e-", "ē")
            romanizedLine = romanizedLine.replace("i-", "ī")
            romanizedLine = romanizedLine.replace("o-", "ō")
            romanizedLine = romanizedLine.replace("u-", "ū")
            
            ## Special characters / Punctuation
            ## https://en.wikipedia.org/wiki/List_of_Japanese_typographic_symbols

            romanizedLine = romanizedLine.replace("「", "'")
            romanizedLine = romanizedLine.replace("」", "'")
            romanizedLine = romanizedLine.replace("『", "\"")
            romanizedLine = romanizedLine.replace("』", "\"")
            romanizedLine = romanizedLine.replace("（", "(")
            romanizedLine = romanizedLine.replace("）", ")")
            romanizedLine = romanizedLine.replace("〔", "[")
            romanizedLine = romanizedLine.replace("〕", "]")
            romanizedLine = romanizedLine.replace("［", "[")
            romanizedLine = romanizedLine.replace("］", "]")
            romanizedLine = romanizedLine.replace("｛", "{")
            romanizedLine = romanizedLine.replace("｝", "}")
            romanizedLine = romanizedLine.replace("｟", "((")
            romanizedLine = romanizedLine.replace("｠", "))")
            romanizedLine = romanizedLine.replace("〈", "‹")
            romanizedLine = romanizedLine.replace("〉", "›")
            romanizedLine = romanizedLine.replace("《", "«")
            romanizedLine = romanizedLine.replace("》", "»")
            romanizedLine = romanizedLine.replace("【", "[")
            romanizedLine = romanizedLine.replace("】", "]")
            romanizedLine = romanizedLine.replace("〖", "[")
            romanizedLine = romanizedLine.replace("〗", "]")
            romanizedLine = romanizedLine.replace("〘", "[")
            romanizedLine = romanizedLine.replace("〙", "]")
            romanizedLine = romanizedLine.replace("〚", "[")
            romanizedLine = romanizedLine.replace("〛", "]")
            romanizedLine = romanizedLine.replace("。", ".")
            romanizedLine = romanizedLine.replace("、", ",")
            romanizedLine = romanizedLine.replace("・", "·")
            romanizedLine = romanizedLine.replace("゠", "–")
            romanizedLine = romanizedLine.replace("＝", "—")
            romanizedLine = romanizedLine.replace("…", "...")
            romanizedLine = romanizedLine.replace("‥", "..")            
            
            ## Custom tokens and fixes
            romanizedLine = romanizedLine.replace("**SPACE**", " ")

            ## Remove multiple spaces
            romanizedLine = romanizedLine.strip()
            romanizedLine = " ".join(romanizedLine.split())

            

            pair[text] = romanizedLine.strip()
            romanized.append(pair)

        return romanized


r = JapaneseToRomaji()
print(r.convert("日本語を書いてください1996 5.99 6AM"))