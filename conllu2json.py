import os
import json
g_pos = set()
g_doc_line_total = 0

def conllu_file_to_json_file(fullname, f_doc_json):
    global g_doc_line_total
    print(fullname)
    base_filename = os.path.basename(fullname)
    word_list = []
    f = open(fullname, encoding='utf_8')
    for each in f:
        items = each.strip().split('\t')
        if len(items) != 10:
            # if len(sent_list) != 0:
            #     print(sent_list)
            out_data = {}
            out_data['id'] = g_doc_line_total
            g_doc_line_total += 1
            out_data['filename'] = base_filename
            out_data['content'] = word_list
            f_doc_json.write('{}\n'.format(json.dumps(out_data,ensure_ascii=False)))
            word_list.clear()
        else:
            word_list.append((items[2], items[4]))
            g_pos.add(items[4])
    pass

def conv_to_jsonl(data_pathname, jsonl_filename):
    print('write {}'.format(jsonl_filename))
            
    os.makedirs(os.path.dirname(jsonl_filename), exist_ok=True)
    f_doc_json = open(jsonl_filename, 'w', encoding='utf-8')
    for parent, dirs, files in os.walk(data_pathname):
        for filename in files:
            fullname = os.path.join(parent, filename)
            if filename.endswith('.conllu'):
                conllu_file_to_json_file(fullname, f_doc_json)
    print("finished.")
conv_to_jsonl('./data/rmrb-conllu', './data/rmrb-json/rmrb.jsonl')