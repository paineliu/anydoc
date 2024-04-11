import os
import json
g_pos = set()
g_doc_line_total = 0

def conv_to_jsonl(conllu_pathname, text_pathname):

    for parent, dirs, files in os.walk(conllu_pathname):
        for filename in files:
            fullname = os.path.join(parent, filename)
            text_fullname = os.path.join(text_pathname, filename[:-7])
            bak_fullname = text_fullname + '.bak'
            if filename.endswith('.conllu'):
                print(fullname, text_fullname)
                os.rename(text_fullname, bak_fullname)
    print("finished.")
conv_to_jsonl('./data/rmrb-conllu', './data/rmrb')