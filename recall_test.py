import time
import os
from segtool import SegTool
from anydoc import JSSCql
import random
import re
from statistics import mean


def txt_to_json(filename):
    sen_lst = []
    f = open(filename, 'r', encoding='utf-8')
    for each in f:
        line = each.strip()
        passage_str = line.strip()

        if len(passage_str) > 0:
            sentences = re.split(r"([.。!！?？\s+])", passage_str)
            sentences.append("")
            sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
            # print('\n'.join(sentences))
            sen_id = 0
            for _, sen in enumerate(sentences):
                if 5 < len(sen) <= 20:
                    sen_lst.append(sen)
    return sen_lst

if __name__ == '__main__':
    lst_sen = txt_to_json('./data/rmrb-text/2015-06.txt')
    f = open('./recall_case.txt', 'w', encoding='utf_8')
    random.shuffle(lst_sen)
    segTool = SegTool()
    sand_err = 0
    thu_err = 0
    total = 0
    for i, sen, in enumerate(lst_sen[:1000]):
        jeba_pos = segTool.jieba_pos_tag(sen, False)
        sand_pos = segTool.stanford_pos_tag(sen, False)
        thu_pos = segTool.thulac_pos_tag(sen, False)
        
        if sand_pos != thu_pos and segTool.check_jieba(sen):
            for item in jeba_pos:
                if (len(item) > 1  and item not in sand_pos):
                    print('san', sand_err, total, item,  jeba_pos, sand_pos)
                    if len(segTool.stanford_pos_tag(item, False)) > 0:
                        sand_err +=1
                        break
            for item in jeba_pos:
                if (len(item) > 1  and item not in thu_pos):
                    if len(segTool.thulac_pos_tag(item, False)) > 0:
                        thu_err +=1
                        print('thu', thu_err, total, item, jeba_pos, thu_pos)
                        break
        total += 1
        f.write(sen + '\n')
    f.close()
    print(sand_err, thu_err, total)
        


    # test_anydoc('rmrb-table-stanford', './speed_case.txt', './speed_test_anydoc_stanford_482.txt')
    # test_blacklab('rmrb-blacklab-stanford', './speed_case.txt', './speed_test_blacklab_stanford_482.txt')
    #speed_result_stat('./speed_test_anydoc_stanford_482.txt', './speed_test_blacklab_stanford_482.txt', './speed_result.csv')
    