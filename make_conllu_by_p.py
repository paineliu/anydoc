# import os
# import json
import re
from segtool import SegTool
import multiprocessing
from multiprocessing import freeze_support
import os, time, random

# import time
# from multiprocessing import Process, Queue, freeze_support

# # import queue
# # import threading



def passage_to_sentences(passage):
    sentences = re.split(r"([.。!！?？\s+])", passage)
    sentences.append("")
    sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
    return sentences

def conllu_txt_to_conllu_file(txt_filename, conllu_filename):
    print(txt_filename, conllu_filename)
    segTool = SegTool()
    os.makedirs(os.path.dirname(conllu_filename), exist_ok=True)
    f = open(txt_filename, encoding='utf_8')
    f_c = open(conllu_filename, mode='w', encoding='utf_8')
    start_time = time.time()
    begin_time = time.time()
    line_total = 0
    for each in f:
        passage = each.strip()
        sentences = passage_to_sentences(passage)
        line_total += 1
        end_time = time.time()
        if (end_time - begin_time > 6):
            begin_time = end_time
            print(txt_filename, line_total)
        for sentence in sentences:
            if len(sentence) > 0:
                tokens = segTool.thulac_pos_tag(sentence)
                if len(tokens) > 1:
                    for i, token in enumerate(tokens):
                        conllu_line = '{}\t{}\t{}\t_\t{}\t_\t_\t_\t_\n'.format(i+1, token[0], token[0], token[1].replace(' ', '-'))
                        f_c.write(conllu_line)                        
                    f_c.write('\n')
                    
 
def conv_to_conllu(data_pathname, conllu_pathname):
    lst_file = []
    for parent, dirs, files in os.walk(data_pathname):
        for filename in files:
            fullname = os.path.join(parent, filename)
            out_pathname = conllu_pathname + fullname[len(data_pathname):]
            if filename.endswith('.txt'):
                map_param = { 'inFile':fullname, 'outFile':out_pathname}
                lst_file.append(map_param)
    return lst_file

    


def work(inFile, outFile):
    t_start = time.time()
    print("pid = %d" % os.getpid())
    conllu_txt_to_conllu_file(inFile, outFile)
    t_end = time.time()

    print("耗时%06.2f" % (t_end-t_start))




def main():
    po = multiprocessing.Pool(processes=12)
    print("main start")
    print(po)
    lst_file = conv_to_conllu('./data/rmrb-text', './data/rmrb-conllu-thulac')
    for i in lst_file:
        po.apply_async(work,args=(i['inFile'], i['outFile']))

    po.close()
    po.join()

    print("main end")

if __name__ == '__main__':
    freeze_support()
    main()