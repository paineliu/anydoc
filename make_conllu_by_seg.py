import os
import json
import re
from segtool import SegTool

g_pos = set()
g_doc_line_total = 0

def passage_to_sentences(passage):
    sentences = re.split(r"([.。!！?？\s+])", passage)
    sentences.append("")
    sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
    return sentences

def conllu_txt_to_conllu_file(segTool:SegTool, txt_filename, conllu_filename):
    print(txt_filename, conllu_filename)
    os.makedirs(os.path.dirname(conllu_filename), exist_ok=True)
    f = open(txt_filename, encoding='utf_8')
    f_c = open(conllu_filename, mode='w', encoding='utf_8')

    for each in f:
        passage = each.strip()
        sentences = passage_to_sentences(passage)
        for sentence in sentences:
            if len(sentence) > 0:
                tokens = segTool.nlpir_pos_tag(sentence)
                if len(tokens) > 1:
                    for i, token in enumerate(tokens):
                        conllu_line = '{}\t{}\t{}\t_\t{}\t_\t_\t_\t_\n'.format(i+1, token[0], token[0], token[1].replace(' ', '-'))
                        f_c.write(conllu_line)                        
                    f_c.write('\n')
                    
 

def conv_to_conllu(data_pathname, conllu_pathname):
    segTool = SegTool()
    for parent, dirs, files in os.walk(data_pathname):
        for filename in files:
            fullname = os.path.join(parent, filename)
            out_pathname = conllu_pathname + fullname[len(data_pathname):]
            if filename.endswith('.txt'):
                conllu_txt_to_conllu_file(segTool, fullname, out_pathname)
    print("finished.")

conv_to_conllu('./data/rmrb-text', './data/rmrb-conllu-nlpir')
