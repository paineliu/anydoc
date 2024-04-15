import time
import os
from anydoc import JSSCql
import random
from statistics import mean

def test_blacklab_speed(data_name, cql_statement, f_out):
    f = open('./temp.txt', mode='w', encoding='utf_8')
    for i in range(12):
        f.write('{}\n'.format(cql_statement))
    f.close()
    os.system('java -cp "./tools/BlackLab-v4-alpha2/core/target/*" nl.inl.blacklab.tools.QueryTool -f ./temp.txt --mode performance ./data/{} > ./result.txt'.format(data_name))
    f = open('./result.txt', mode='r', encoding='utf_8')
    for each in f:
        items = each.strip().split('\t')
        if len(items) == 3:
            item_str = '{}\n'.format('\t'.join(items))
            f_out.write(item_str)
            print(item_str, end='')
    f.close()
    

def test_blacklab(data_name, input_filename, output_filename):
    f_out = open(output_filename, mode='w', encoding='utf_8')
    f = open(input_filename, encoding='utf_8')
    for each in f:
        cql_statement = each.strip()
        test_blacklab_speed(data_name, cql_statement, f_out)
    f_out.close()

def test_anydoc(data_name, input_filename, output_filename):
    f = open(input_filename, encoding='utf_8')
    f_out = open(output_filename, mode='w', encoding='utf_8')
    jssCql = JSSCql('./data/{}'.format(data_name))
    for each in f:
        statement = each.strip()
        if len(statement) > 0:
            statement = statement.replace('[]', '')
            for i in range(12):
                start = time.time()
                total, result = jssCql.cql_search(statement)
                cost = time.time() - start
                map_result = {}
                out_str = "{}\t{}\t{}\n".format(statement, int(cost * 1000), total)
                f_out.write(out_str)
                print(out_str, end='')
    
def rand_test_data():
    def is_chinese(word):
        for ch in word:
            if '\u4e00' > ch or ch > '\u9fff':
                return False
        return True
    f_out = open('./test_case.txt', mode='w', encoding='utf-8')
    f = open('./data/rmrb-conllu-stanford/2014-06.txt.conllu', mode='r', encoding='utf-8')
    lines = f.readlines()
    random.shuffle(lines)
    set_out = set()
    for i, line in enumerate(lines):
        items = line.split('\t')
        if len(items) > 1 and len(items[1]) > 1 and is_chinese(items[1]):
            if items[1] not in set_out:
                set_out.add(items[1])
                if i%5 != 0:
                    print("[word='{}']".format(items[1]))
                    f_out.write("[word='{}']\n".format(items[1]))
                else:
                    print("[word='{}'&pos='{}']".format(items[1], items[4]))
                    f_out.write("[word='{}'&pos='{}']\n".format(items[1], items[4]))
                if len(set_out) >= 450:
                    break

def speed_stat(filename):
    list_time = []

    f = open(filename, encoding='utf_8')
    map_stat = {}
    for each in f:
        items = each.strip().split()
        cql = items[0]
        time = int(items[1])
        if cql not in map_stat:
            map_stat[cql] ={'data':[]}
        if time > 0:
            map_stat[cql]['data'].append(time)

    for item in map_stat:
        data = map_stat[item]['data']
        if len(data) > 1:
            data.pop(data.index(max(data)))
            map_stat[item]['avg'] = mean(data)
            list_time.append(mean(data))

    return mean(list_time), map_stat

def speed_result_stat(anydoc_filename, blacklab_filename, csv_filename):
    avg_anydoc, map_anydoc = speed_stat(anydoc_filename)
    avg_blacklab, map_blacklab = speed_stat(blacklab_filename)
    f = open(csv_filename, 'w', encoding='utf_8_sig')
    f.write('"{}",{},{},{}\n'.format('cql', 'my', 'blacklab', 'speed'))
    print(avg_anydoc,avg_blacklab, 1 - avg_anydoc / avg_blacklab)
    print(len(map_anydoc))
    for cql in map_anydoc:
        if cql in map_blacklab:
            f.write('"{}",{},{},{}\n'.format(cql, map_anydoc[cql]['avg'], map_blacklab[cql]['avg'], map_anydoc[cql]['avg'] < map_blacklab[cql]['avg']))
        else:
            print(cql)

if __name__ == '__main__':

    # test_anydoc('rmrb-table-stanford', './speed_case.txt', './speed_test_anydoc_stanford_482.txt')
    # test_blacklab('rmrb-blacklab-stanford', './speed_case.txt', './speed_test_blacklab_stanford_482.txt')
    speed_result_stat('./speed_test_anydoc_stanford_482.txt', './speed_test_blacklab_stanford_482.txt', './speed_result.csv')
    