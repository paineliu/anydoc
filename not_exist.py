import time
import os
from anydoc import JSSCql
import random
from statistics import mean

def not_exist_blacklab_test(data_name, test_filename, result_filename):
    f_out = open(result_filename, 'w', encoding='utf_8')
    # os.system('java -cp "./tools/BlackLab-v4-alpha2/core/target/*" nl.inl.blacklab.tools.QueryTool -f {} --mode performance {} > ./result.txt'.format(test_filename, data_name))
    os.system('java -cp "./tools/BlackLab-v4-alpha2/core/target/*" nl.inl.blacklab.tools.QueryTool -f {} {} > ./result.txt'.format(test_filename, data_name))
    f = open('./result.txt', mode='r', encoding='utf_8')
    for each in f:
        items = each.strip().split('\t')
        if len(items) == 3:
            item_str = '{}\n'.format('\t'.join(items))
            f_out.write(item_str)
            print(item_str, end='')
    f.close()


if __name__ == '__main__':

    # test_anydoc('rmrb-table-stanford', './speed_case.txt', './speed_test_anydoc_stanford_482.txt')
    # test_blacklab('rmrb-blacklab-stanford', './speed_case.txt', './speed_test_blacklab_stanford_482.txt')
    not_exist_blacklab_test('./data/rmrb-blacklab-stanford', './not_exist.txt', './not_exist_stanford_result.csv')
    not_exist_blacklab_test('./data/rmrb-blacklab-thulac', './not_exist.txt', './not_exist_thulac_result.csv')
    