
# Sam Pickering

# Script for converting simplified Hanzi to traditional Hanzi
# Utilizing open source packages such as Open Chinese Convert

# Takes user text file of hanzi
# reads file 
# converts hanzi and writes to a new file

# future additions
# implement a gui where a user can copy and paste hanzi 
# implement phonetic notation for each character



import opencc
import pypinyin
from pypinyin import pinyin, style, lazy_pinyin
# make into a function and duplicate for the other json file configs
#s2tw = simp to trad taiwan standard
#s2t simp to traditional 
# t2s traditional to simplified
#simp chines to trad chinese hong king standard

# include in function for each type

#print(pypinyin.__version__)
#print(pypinyin.__file__)
#print('bopomofo' in dir(pypinyin.style))

#help()

#print(pinyin("中心", style= pypinyin.BOPOMOFO))

# first tone is not indicated for the bopomofo

def trad_taiwan_zhuyin(input_filename: str, output_filename: str = "convhanzi_output.txt"):
    
    converter_s2tw = opencc.OpenCC('s2tw.json') #simp to trad config json
    with open (input_filename, 'r', encoding='utf-8') as file, open("convhanzi_output.txt", "w", encoding='utf-8') as outfile:
        for line in file:
            convhanzi = converter_s2tw.convert(line.strip('')) 
            zhuyin_notation = pinyin(convhanzi, style= pypinyin.BOPOMOFO, heteronym=False)
            zhuyin_notation_flat = [item[0].strip() for item in zhuyin_notation]
            hanzi_zhuyin = f"{convhanzi.strip()} {' '.join(zhuyin_notation_flat)}"
            outfile.write(hanzi_zhuyin + '\n' )
            print(f"Conversion completed → {output_filename}")

trad_taiwan_zhuyin("hanzi.txt")
