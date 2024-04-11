import jieba
import jieba.posseg
from stanfordcorenlp import StanfordCoreNLP
import pynlpir
import json
import thulac
from ltp import LTP
# https://blog.csdn.net/shuihupo/article/details/81540433

def stanford_pos_tag(sentence):
    def get_pos_tag(nlp, sentence):
        tokens = []
        props={'annotators': 'tokenize, pos','pipelineLanguage':'zh','outputFormat':'json'}
        text_string = nlp.annotate(sentence, properties=props)
        text_data = json.loads(text_string)

        for text in text_data['sentences'][0]['tokens']:
            tokens.append((text['word'], text['pos']))

        return tokens

    #java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 9000 -port 9000 -timeout 15000
    # with StanfordCoreNLP(r'd:/paineliu/anydoc/data/stanford-corenlp/stanford-corenlp-4.5.6', lang='zh') as nlp:
    with StanfordCoreNLP('http://localhost', port=9000, lang='zh') as nlp:
        pos_tagged = get_pos_tag(nlp, sentence)
        return pos_tagged
    
def jieba_pos_tag(sentence):
    tokens = []
    words =jieba.posseg.cut(sentence)
    for w in words:
        tokens.append((w.word, w.flag))
    return tokens

def nlpir_pos_tag(sentence):
    pynlpir.open()
    tokens = pynlpir.segment(sentence, pos_tagging=True)
    pynlpir.close()
    return tokens

def thulac_pos_tag(sentence):
    tokens = []
    thu1 = thulac.thulac()  # 默认模式
    text = thu1.cut(sentence, text=True)  # 进行一句话分词
    wp = text.split(' ')
    for t in wp:
        item = t.split('_')
        word = item[0]
        pos = item[1]
        tokens.append((word, pos))
    return tokens

def ltp_pos_tag(sentence):
    ltp = LTP()  # 默认加载 Small 模型
    tokens = []
    output = ltp.pipeline([sentence], tasks=["cws", "pos", "ner", "srl", "dep", "sdp"])
    # 使用字典格式作为返回结果
    for i in range(len(output.cws[0])):
        tokens.append((output.cws[0][i], output.pos[0][i]))
    return tokens


def test_seg_pos(sentence):
    print('Stanford', stanford_pos_tag(sentence))    
    print('结巴', jieba_pos_tag(sentence))
    print('中科院计算所', nlpir_pos_tag(sentence))
    print('清华大学', thulac_pos_tag(sentence))
    print('哈尔滨工业大学', ltp_pos_tag(sentence))


sentence = '在和平共处五项原则的基础上'
# test_seg_pos(sentence)
lst = ['和平共处五项原则','共处五项原则','五项原则','和谐','和平环境','项原则','原则',]
print(sorted(lst))

