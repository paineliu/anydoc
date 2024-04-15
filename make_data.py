import os
import re
import json
import time
import jsslib
from pathlib import Path
import argparse
 
def parse_args():
    parser = argparse.ArgumentParser(description='anydoc index file create tools')
    parser.add_argument('-c', '--config_pathname', type=str, default='./config', required=False, help='config pathname')
    parser.add_argument('-t', '--text_pathname', type=str, default='./data/text/rmrb', required=False, help='text pathname')
    parser.add_argument('-d', '--json_pathname', type=str, default='./data/json', required=False, help='data pathname')
    parser.add_argument('-o', '--table_pathname', type=str, default='./data/table', required=False, help='table pathname')
    parser.add_argument('-T', '--test_filename', type=str, default='./test_sql.txt', required=False, help='test pathname')

    return parser.parse_args()

def txt_to_json(doc_id:int, txt_string:str, f_pass, f_sen):
    lines = txt_string.split('\n')
    passage_id = 0
    line_total = 0
    start_time = time.time()
    begin_time = start_time
    
    for line in lines:
        passage_str = line.strip()
        line_total += 1
        if len(passage_str) > 0:
            # print(doc_id, passage_id / len(lines))
            # print('{} {} {}\n'.format(doc_id, passage_id, passage_str))
            passage = {'doc_id':doc_id, 'pass_id':passage_id, "content":passage_str}
            f_pass.write('{}\n'.format(json.dumps(passage, ensure_ascii=False)))

            sentences = re.split(r"([.。!！?？\s+])", passage_str)
            sentences.append("")
            sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
            # print('\n'.join(sentences))
            sen_id = 0
            for _, sen in enumerate(sentences):
                if len(sen) > 0:
                    sentence = {'doc_id':doc_id, 'pass_id':passage_id, "sen_id":sen_id, "content":sen}
                    f_sen.write('{}\n'.format(json.dumps(sentence, ensure_ascii=False)))
                    sen_id += 1
            passage_id += 1

        end_time = time.time()
        if line_total == 1 or end_time - begin_time > 6:
            begin_time = end_time
            date_str = time.strftime('[%Y%m%d%H%M%S]', time.localtime())
            print('{} {:.1f}(m) line = {:.3%} ({}/{}) {}'.format(date_str, (end_time - start_time)/60, line_total / len(lines), line_total, len(lines), line))
    end_time = time.time()
    date_str = time.strftime('[%Y%m%d%H%M%S]', time.localtime())
    print('{} {:.1f}(m) line = {:.2%} ({}/{})'.format(date_str, (end_time - start_time)/60, line_total / len(lines), line_total, len(lines), line))


def make_data(text_pathname, data_pathname):
    doc_filename = os.path.join(data_pathname, "doc.jsonl")
    pass_filename = os.path.join(data_pathname, "pass.jsonl")
    sen_filename = os.path.join(data_pathname, "sen.jsonl")
    os.makedirs(data_pathname, exist_ok=True)
    f_doc = open(doc_filename, 'w', encoding='utf-8')
    f_pass = open(pass_filename, 'w', encoding='utf-8')
    f_sen = open(sen_filename, 'w', encoding='utf-8')
    doc_id = 0
        
    for parent, dirnames, filenames in os.walk(text_pathname):
        for filename in filenames:
            fullname = os.path.join(parent, filename)
            base_name = os.path.basename(fullname)
            doc = {}
            doc["doc_id"] = doc_id
            doc['filetype'] = Path(filename).suffix[1:].lower()
            doc["filename"] = filename
            filemt = time.localtime(os.stat(fullname).st_mtime)
            doc['modify_time'] = time.strftime("%Y-%m-%d %H:%M:%S", filemt)
            doc['filesize'] = os.path.getsize(fullname)
            doc['pathname'] = parent.replace('\\', '/')[len(text_pathname) + 1:]
            doc['fullname'] = fullname.replace('\\', '/')[len(text_pathname) + 1:]
           
            f_doc.write('{}\n'.format(json.dumps(doc, ensure_ascii=False)))
            with open(fullname, 'r', encoding='utf-8') as f:
                data = f.read()
                txt_to_json(doc_id, data, f_pass, f_sen)
            doc_id += 1

def make_table(json_pathname, config_pathname, output_pathname):
    pass

def test_table(table_lst_filename, test_filename):
    if (os.path.isfile(test_filename)):
        with open(test_filename, "r", encoding='utf-8') as file:
            sql_list = file.read().splitlines()
    else:
        sql_list = ["SELECT TOP 20 *, content FROM rmrb WHERE seg LIKE '我们';"]
        
    jss = jsslib.JSS(1)
    jss.LoadTable(table_lst_filename)
    for sql in sql_list:
        sql = sql.strip()
        print(sql)
        start = time.time()
        result = jss.RunSql(sql)
        end = time.time()
        print('cost =', end-start)
        print(result)

def create_text_index(config_pathname, text_pathname, data_pathname, table_pathname, test_filename=''):
    # make_data(text_pathname, data_pathname)
    # jss = jsslib.JSS(1)
    # jss.CreateTable('./config/rmrb.json', './data/rmrb-json-stanford', './data/rmrb-table-stanford')
    # jss.CreateTable('./config/rmrb.json', './data/rmrb-json-thulac', './data/rmrb-table-thulac')

    # make_table(data_pathname, config_pathname, table_pathname)
    # lst_filename = os.path.join(table_pathname, 'table.lst')
    test_table('./data/rmrb-table-stanford', test_filename)

if __name__ == '__main__':

    args = parse_args()

    create_text_index(args.config_pathname, args.text_pathname, args.json_pathname, args.table_pathname, args.test_filename)
