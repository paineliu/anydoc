# https://www.cnblogs.com/sug-sams/p/12607662.html
import numpy as np
import json
import os
import faiss
import struct
import shutil
from FlagEmbedding import FlagModel
import argparse

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  #（保证程序cuda序号与实际cuda序号对应）
os.environ['CUDA_VISIBLE_DEVICES'] = "0"  #（代表仅使用第0，1号GPU）

def parse_args():
    parser = argparse.ArgumentParser(description='jss jsonl to embeding convert tools')
    parser.add_argument('-m', '--bge_model_path', type=str, required=True, help='bge model data pathname')
    parser.add_argument('-t', '--table_path', type=str, required=True, help='table data pathname')
    parser.add_argument('-T', '--test_file', type=str, required=True, help='test data filename')

    return parser.parse_args()

def get_sentence_embedding(model, sents):
    sent_embedding = model.encode(sents)
    sent_embedding_lst = sent_embedding.tolist()
    return sent_embedding_lst

def make_sub_item(id, field, data, lst_ids, map_data, win_size, step):
    if isinstance(data, str):
        for i in range(0, len(data), step):
            sub_data = data[i: i + win_size]
            sub_id = "{}-{}-{}~{}".format(id, field, i, len(sub_data))
            if (i > 0 and len(sub_data) < win_size):
                continue
            lst_ids.append(sub_id)
            map_data[sub_id] = sub_data
    elif isinstance(data, list):
        for t in range(len(data)):
            data_item = data[t]
            for i in range(0, len(data_item), step):
                sub_data = data_item[i: i + win_size]
                sub_id = "{}-{}-{}#{}~{}".format(id, field, t, i, len(sub_data))
                if (i > 0 and len(sub_data) < win_size):
                    continue
                lst_ids.append(sub_id)
                map_data[sub_id] = sub_data


    return ""

def json2field(json_filename, id_field, embed_fields, default_fields, passage_size, passgae_step, out_pathname):
    print('load', json_filename)
    list_data = []
    os.makedirs(out_pathname, exist_ok=True)
    f = open(json_filename, encoding='utf-8')
    for each in f:
        each = each.strip()
        if len(each) > 0:
            json_data = json.loads(each)
            list_data.append(json_data)
    f.close()

    map_all_data = {}
    lst_all_ids = []

    for field in embed_fields:
        map_data = {}
        lst_ids = []
        for i in range(len(list_data)):
            data = list_data[i][field]
            if len(data) > 0:
                make_sub_item(list_data[i][id_field], field, list_data[i][field], lst_ids, map_data, passage_size, passgae_step)
        field_json_filename = os.path.join(out_pathname, "em-" + field +".json")
        print('write', field_json_filename)
        f = open(field_json_filename, "w", encoding='utf-8') 
        json.dump(map_data, f, ensure_ascii=False)
        f.close()

        field_ids_filename = os.path.join(out_pathname, "em-" + field +".ids")
        print('write', field_ids_filename)
        f = open(field_ids_filename, "w", encoding='utf-8') 
        for line in lst_ids:
            f.write(line +'\n')
        f.close()

        if field in default_fields:
            for each in map_data:
                map_all_data[each] = map_data[each]
            lst_all_ids += lst_ids

    field = 'default'
    field_json_filename = os.path.join(out_pathname, "em-" + field +".json")
    print('write', field_json_filename)
    f = open(field_json_filename, "w", encoding='utf-8') 
    json.dump(map_all_data, f, ensure_ascii=False)
    f.close()

    field_ids_filename = os.path.join(out_pathname, "em-" + field +".ids")
    print('write', field_ids_filename)
    f = open(field_ids_filename, "w", encoding='utf-8') 
    for line in lst_all_ids:
        f.write(line +'\n')
    f.close()

def field2npy(model, json_filename, ids_filename, npy_filename):
    print('load', json_filename)
    with open(json_filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    lst_ids = [line.strip() for line in open(ids_filename, encoding='utf-8')] 
    lst_text = []
    for id in lst_ids:
        lst_text.append(json_data[id])
    npy_data = model.encode(lst_text)
    print('save', npy_filename)
    np.save(npy_filename, npy_data)

def json2npy(bge_pathname, json_filename, id_field, embed_fields, default_fields, passage_size, passgae_step, out_pathname):
    json2field(json_filename, id_field, embed_fields, default_fields, passage_size, passgae_step, out_pathname)
    print('load', bge_pathname)
    model = FlagModel(bge_pathname, query_instruction_for_retrieval="为这个句子生成表示以用于检索相关文章：")

    for field in embed_fields:
        txt_filename = os.path.join(out_pathname, "em-" + field +".json")
        ids_filename = os.path.join(out_pathname, "em-" + field +".ids")
        npy_filename = os.path.join(out_pathname, "em-" + field +".npy")
        field2npy(model, txt_filename, ids_filename, npy_filename)
    if len(default_fields) > 0:
        field = 'default'
        txt_filename = os.path.join(out_pathname, "em-" + field +".json")
        ids_filename = os.path.join(out_pathname, "em-" + field +".ids")
        npy_filename = os.path.join(out_pathname, "em-" + field +".npy")
        field2npy(model, txt_filename, ids_filename, npy_filename)

def write_faiss(xb, d, idx_filename):
    index = faiss.IndexFlatL2(d)   # build the index
    index.add(xb)                  # add vectors to the index
    faiss.write_index(index, idx_filename)

def write_faiss_ivf_pq(xb, d, idx_filename):
    try:
        nlist = int(len(xb)**0.5) # how many cells
        nlist = int((nlist + 3) / 4) * 4 
        m = 32   # number of centroid IDs in final compressed vectors
        bits = 8 # number of bits in each centroid # 8 specifies that each sub-vector is encoded as 8 bits
        quantizer = faiss.IndexFlatL2(d)  # this remains the same
        index = faiss.IndexIVFPQ(quantizer, d, nlist, m, bits)
        # index = faiss.index_factory(d, "IVF100,PQ8")
        index.train(xb)
        index.add(xb)
        faiss.write_index(index, idx_filename)
    except:
        index = faiss.IndexFlatL2(d)   # build the index
        index.add(xb)                  # add vectors to the index
        faiss.write_index(index, idx_filename)

def write_faiss_dat_file(npy_filename, dat_filename):
    print('save', dat_filename)
    np_data = np.load(npy_filename)
    write_faiss_ivf_pq(np_data, 768, dat_filename)

def write_faiss_idx_file(txt_filename, idx_filename):
    print('save', idx_filename)
    f = open(txt_filename, encoding='utf-8')
    label_list = [line.strip().encode('utf8') for line in f]
    label_head = []
    label_head.append(0)
    label_len_total = 0
    for label in label_list:
        label_len_total += len(label) + 1
        label_head.append(label_len_total)

    with open(idx_filename, 'wb')as fp:
        fp.write(struct.pack('Q', len(label_head)))
        for head in label_head:
            fp.write(struct.pack('Q', head))
                        
        fp.write(struct.pack('Q', label_len_total))
        for label in label_list:
            fp.write(label)
            fp.write(struct.pack('B', 0))

def npy2faiss(in_pathname, out_pathname, embed_fields, default_fields):
    if len(default_fields) > 0:
        field = 'default'
        ids_filename = os.path.join(in_pathname, "em-" + field +".ids")
        npy_filename = os.path.join(in_pathname, "em-" + field +".npy")

        dat_filename = os.path.join(out_pathname, "em-" + field +".dat")
        idx_filename = os.path.join(out_pathname, "em-" + field +".idx")
        write_faiss_dat_file(npy_filename, dat_filename)
        write_faiss_idx_file(ids_filename, idx_filename)

    for field in embed_fields:
        ids_filename = os.path.join(in_pathname, "em-" + field +".ids")
        npy_filename = os.path.join(in_pathname, "em-" + field +".npy")

        dat_filename = os.path.join(out_pathname, "em-" + field +".dat")
        idx_filename = os.path.join(out_pathname, "em-" + field +".idx")
        write_faiss_dat_file(npy_filename, dat_filename)
        write_faiss_idx_file(ids_filename, idx_filename)

def test_faiss(model, dat_filename, label_filename, json_filename, test_sentence_list):
    print('load', dat_filename)
    index = faiss.read_index(dat_filename)
    label_data = [line.strip() for line in open(label_filename, 'r', encoding='utf-8')]
    f = open(json_filename, encoding='utf-8')
    json_data = json.load(f)
    f.close()
    index.nprobe = 10

    for sentence in test_sentence_list:
        print(sentence)
        enc = get_sentence_embedding(model, sentence)
        xq = np.asarray([enc])
        k = 5
        D, I = index.search(xq, k)
        for i, idx in enumerate(I[0]):
            text = json_data[label_data[idx]]
            text = text.replace('\n', '')
            print(i, idx, label_data[idx], D[0][i], text)
        print()

def test_embed_data(bge_pathname, dat_pathname, embed_fields, test_filename):
    print('load', bge_pathname)
    model = FlagModel(bge_pathname, query_instruction_for_retrieval="为这个句子生成表示以用于检索相关文章：")
    sentences = []
    if os.path.isfile(test_filename):
        f = open(test_filename, 'r', encoding='utf-8')
        for each in f:
            each = each.strip()
            if len(each) > 0:
                sentences.append(each)
        f.close()
    else:
        sentences.append("你喜欢什么？")

    if len(embed_fields) == 0:
        field = 'default'
        dat_filename = os.path.join(dat_pathname, "em-" + field +".dat")
        ids_filename = os.path.join(dat_pathname, "em-" + field +".ids")
        json_filename = os.path.join(dat_pathname, "em-" + field +".json")
        test_faiss(model, dat_filename, ids_filename, json_filename, sentences)
    else:
        for field in embed_fields:
            dat_filename = os.path.join(dat_pathname, "em-" + field +".dat")
            ids_filename = os.path.join(dat_pathname, "em-" + field +".ids")
            json_filename = os.path.join(dat_pathname, "em-" + field +".json")
            test_faiss(model, dat_filename, ids_filename, json_filename, sentences)

def make_embed_data(bge_pathname, json_filename, id_field, embed_fields, default_fields, passage_size, passgae_step, out_pathname):
    json2npy(bge_pathname, json_filename, id_field, embed_fields, default_fields, passage_size, passgae_step, out_pathname)
    npy2faiss(out_pathname, out_pathname, embed_fields, default_fields)

def make_embed_data_by_config(bge_pathname, config_filename, json_filename, out_pathname):
    f = open(config_filename, encoding='utf-8')
    config_data = json.load(f)
    f.close()
    id_field = config_data['sem']['id']
    embed_fields = config_data['sem']['field']
    default_fields = config_data['sem']['default']
    if 'passage' in config_data['sem']:
        passage_size = config_data['sem']['passage']['size']
        passage_step = config_data['sem']['passage']['step']
    else:
        passage_size = 320
        passage_step = 300
    make_embed_data(bge_pathname, json_filename, id_field, embed_fields, default_fields, passage_size, passage_step, out_pathname)

def create_embed_index(bge_model_path, table_pathname, lst_table, test_filename = ''):
    
    for table in lst_table:
        config_file = os.path.join(table_pathname, '{}/config.json'.format(table))
        jsonl_path = os.path.join(table_pathname, '{}/{}.jsonl'.format(table, table))
        table_path = os.path.join(table_pathname, '{}'.format(table))
        make_embed_data_by_config(bge_model_path, config_file, jsonl_path, table_path)
        test_embed_data(bge_model_path, table_path, [], test_filename)
        embed_filename = os.path.join(table_pathname, 'embed.json')
    shutil.copy('./embed.json', embed_filename)
    
if __name__=='__main__':

    # bge_model_path = './bge/bge-base-zh-v1.5'
    # table_path = './table'
    # test_file = './test_embed.txt'

    args = parse_args()
    bge_model_path = args.bge_model_path
    table_path = args.table_path
    test_file = args.test_file
    if os.path.isdir(bge_model_path):
        create_embed_index(bge_model_path, table_path, ['picture', 'video'], test_file)