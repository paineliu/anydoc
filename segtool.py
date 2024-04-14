import jieba
import jieba.posseg
from stanfordcorenlp import StanfordCoreNLP
import pynlpir
import json
import thulac
import logging
from ltp import LTP
# https://blog.csdn.net/shuihupo/article/details/81540433

class SegTool():
    def __init__(self):
        self.stanford_nlp =  StanfordCoreNLP('./tools/stanford-corenlp-4.5.6', lang='zh')
        self.ltp_nlp = LTP('tools/LTP/small')  # 默认加载 Small 模型
        self.thul = thulac.thulac()  # 默认模式
        jieba.setLogLevel(log_level=logging.ERROR)
        

    def stanford_pos_tag(self, sentence):
        def get_pos_tag(nlp, sentence):
            tokens = []
            props={'annotators': 'tokenize, pos','pipelineLanguage':'zh','outputFormat':'json'}
            text_string = nlp.annotate(sentence, properties=props)
            text_data = json.loads(text_string)

            for text in text_data['sentences'][0]['tokens']:
                tokens.append((text['word'], text['pos']))

            return tokens

        #java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 9000 -port 9000 -timeout 15000
        # with StanfordCoreNLP('./tools/stanford-corenlp-4.5.6', lang='zh') as nlp:
        # with StanfordCoreNLP('http://localhost', port=9000, lang='zh') as nlp:
        pos_tagged = get_pos_tag(self.stanford_nlp, sentence)
        return pos_tagged
    
    def jieba_pos_tag(self, sentence):
        tokens = []
        words =jieba.posseg.cut(sentence)
        for w in words:
            tokens.append((w.word, w.flag))
        return tokens

    def nlpir_pos_tag(self, sentence):
        pynlpir.open()
        tokens = pynlpir.segment(sentence, pos_tagging=True)
        pynlpir.close()
        return tokens

    def thulac_pos_tag(self, sentence):
        tokens = []
        text = self.thul.cut(sentence, text=True)  # 进行一句话分词
        wp = text.split(' ')
        for t in wp:
            item = t.split('_')
            word = item[0]
            pos = item[1]
            tokens.append((word, pos))
        return tokens

    def ltp_pos_tag(self, sentence):
        tokens = []
        #output = self.ltp_nlp.pipeline([sentence], tasks=["cws", "pos", "ner", "srl", "dep", "sdp"])
        output = self.ltp_nlp.pipeline([sentence], tasks=["cws", "pos"])
        # 使用字典格式作为返回结果
        for i in range(len(output.cws[0])):
            tokens.append((output.cws[0][i], output.pos[0][i]))
        return tokens
    
    def get_sentence(self, segPos):
        sentence = ''
        for each in segPos:
            sentence += each[0] + ' '
        return sentence
    
    def check_stanford_diff(self, sentance):
        sentance_map = {}
        
        seg = self.get_sentence(self.stanford_pos_tag(sentance))
        sentance_map[seg] = sentance_map.get(seg, 0) + 1
        stanford = seg
        sentance_map['stanford'] = seg

        seg = self.get_sentence(self.jieba_pos_tag(sentance))
        sentance_map[seg] = sentance_map.get(seg, 0) + 1
        jieba = seg
        sentance_map['jieba'] = seg

        seg = self.get_sentence(self.nlpir_pos_tag(sentance))
        sentance_map[seg] = sentance_map.get(seg, 0) + 1
        nlpir = seg
        sentance_map['nlpir'] = seg

        seg = self.get_sentence(self.thulac_pos_tag(sentance))
        sentance_map[seg] = sentance_map.get(seg, 0) + 1
        thulac = seg
        sentance_map['thulac'] = seg

        seg = self.get_sentence(self.ltp_pos_tag(sentance))
        sentance_map[seg] = sentance_map.get(seg, 0) + 1
        ltp = seg
        sentance_map['ltp'] = seg

        if sentance_map[thulac] > 2 and sentance_map[stanford] == 1:
            return 0, sentance_map
        elif len(sentance_map) == 1:
            return 1, sentance_map
        else:
            return -1, sentance_map

if __name__ == '__main__':

    segTool = SegTool()
    line_total = 0
    line_right = 0
    line_ambig = 0
    line_error = 0
    f_log = open('./data/stanford_thulac_diff.csv', mode='w', encoding='utf_8_sig')
    f_log.write('{},{},{},{}\n'.format('句子','长度','斯坦福','清华'))
    f = open ('./data/rmrb-json-stanford/rmrb.jsonl', encoding='utf_8')
    for each in f:
        jdata = json.loads(each)
        sentance = jdata['sentence']
        if 5 < len(sentance) < 15:
            ret, sentance_map = segTool.check_stanford_diff(sentance)
            if ret == 0:
                line_error += 1
                line_total += 1
                # print(ret, line_right / line_total, line_right, line_total, sentance_map)
                print(line_error, sentance, 'stanford', sentance_map['stanford'], '清华', sentance_map['thulac'])
                f_log.write('{},{},{},{}\n'.format(sentance,len(sentance),sentance_map['stanford'],sentance_map['thulac']))
            elif ret == 1:
                line_right += 1
                line_total += 1
                # print(ret, line_right / line_total, line_right, line_total, sentance_map)
            if line_error > 100:
                break
            
# def test_seg_pos(sentence):
#     segPos.check_seg(sentence)

# sentence = '在和平共处五项原则的基础上'
# test_seg_pos(sentence)
# lst = ['和平共处五项原则','共处五项原则','五项原则','和谐','和平环境','项原则','原则',]
# print(sorted(lst))

