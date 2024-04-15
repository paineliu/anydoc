import jsslib
import time
from antlr4 import *
from cqlparser.CQLLexer import CQLLexer
from cqlparser.CQLParser import CQLParser
from cqlparser.CQLListenerEx import CQLListenerEx, SearchTree

class JSSCql:

    def __init__(self, lst_filename):
        self.jss = jsslib.JSS(1)
        self.jss.LoadTable(lst_filename)

    def search_jss(self, word):

        # start = time.time()
        lst_result = self.jss.RunSql("SELECT TOP 1 * FROM rmrb WHERE seg like '{}';".format(word))
        # lst_result = self.jss.RunSql("SELECT TOP 20 * FROM rmrb WHERE pos = '{}';".format('n'))
        # end = time.time()
        # print(end - start)
        map_result = {}
        map_result['total'] = lst_result['total']
        map_result['data'] = {}
        # for item in lst_result['results']:
        #     id ='{}'.format(item['id'])
        #     map_result['data'][id] = item['sentence']
        return map_result

    def search_exp(self, node):
        type = node.get('expr', None)
        if type  == 'and':
            result1 = self.search_exp(node.get('exp_node1', None))
            result2 = self.search_exp(node.get('exp_node2', None))
            result = {k1:result1[k1] for k1 in result1 if k1 in result2}
            return result
        elif type == 'or':
            result1 = self.search_exp(node.get('exp_node1', None))
            result2 = self.search_exp(node.get('exp_node2', None))
            result_or = {}
            result_or['data'] = result1['data']
            for item in result2['data']:
                result_or['data'][item] = result2['data'][item]
            return {'total': result1['total'] + result2['total'], 'data':result1['data'] | result2['data']}
        else:
            if 'exp_node1' in node:
                word = node['exp_node1']['value'].replace("'", "")
            else:
                word = node['value'].replace("'", "")
            return self.search_jss(word)
        
    def is_or_node(self, node):
        type = node.get('expr', None)
        if type  == 'and':
            if self.is_or_node(node.get('exp_node1', None)):
                return True
            if self.is_or_node(node.get('exp_node2', None)):
                return True
        elif type == 'or':
            return True
        else:
            return False

    def get_search_string(self, node, search_string):

        type = node.get('expr', None)
            
        if type  == 'and':
            if self.get_search_string(node.get('exp_node1', None), search_string):
                return True
            if self.get_search_string(node.get('exp_node2', None), search_string):
                return True
        elif type == 'or':
            return ''
        else:
            if 'exp_node1' in node:
                search_string.append(node['exp_node1']['value'].replace("'", ""))
            else:
                search_string.append(node['value'].replace("'", ""))

    def is_or_tree(self, map_tree):
        or_node_exist = False
        for node in map_tree:
            if self.is_or_node(node):
                or_node_exist = True
                break
        return or_node_exist
    
    def search_fast(self, map_tree):
        if not self.is_or_tree(map_tree):
            word_lst = []
            for node in map_tree:
                self.get_search_string(node, word_lst)
            result_lst = self.search_jss(' '.join(word_lst))
            if len(word_lst) > 0:
                out_lst = {}
                for item in result_lst['data']:
                    begin_pos = -1
                    valid_item = True
                    if len(word_lst) > 1:
                        if word_lst[0] != word_lst[1]:
                            for word in word_lst:
                                find_pos = result_lst['data'][item].find(word)
                                if (begin_pos != -1 and find_pos - begin_pos < 0):
                                    valid_item = False
                                    break

                                if (find_pos <= begin_pos):
                                    valid_item = False
                                    break
                                else:
                                    begin_pos = find_pos
                        else:
                            word = word_lst[0]
                            find_pos = result_lst['data'][item].find(word)
                            r_find_pos  = result_lst['data'][item].rfind(word)

                            valid_item = find_pos != r_find_pos
                    else:
                        word = word_lst[0]
                        find_pos = result_lst['data'][item].find(word)
                        valid_item = find_pos != -1
                    if valid_item:
                        out_lst[item] = result_lst['data'][item]

                return result_lst['total'], out_lst
        
        return 0, {}

    def cql_search(self, cql_statement):

        lexer = CQLLexer(InputStream(cql_statement))
        stream = CommonTokenStream(lexer)
        parser = CQLParser(stream)
        tree = parser.query()
        printer = CQLListenerEx(False)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        query_tree = printer.getTree()
        log_message =[]
        bin_tree = []
        search_tree = SearchTree(True)
        search_tree.walker_tree(query_tree, bin_tree, log_message)
            
        lst_result_id = [] 
        if self.is_or_tree(search_tree.map_tree):  
            for node in search_tree.map_tree:
                result = self.search_exp(node)
                lst_result_id.append(result['data'])
            result = lst_result_id[0]
            for i in range(1, len(lst_result_id)):
                result = {k1:result[k1] for k1 in result if k1 in lst_result_id[i]}
            return 0, result
        else:
            result = self.search_fast(search_tree.map_tree)
        

        return result


if __name__ == '__main__':

    # cql_statements = [
    #     # "[word = '克服一切困难']",
    #     # "[word = '好的'][word = '不好的']",
    #     # "[word = '文化'][word = '交流']",
    #     # "[word = '把'][word = '给']",
    #     # "[word = '与其'][word = '不如']",
    #     "[word = '把'|word='被'][word = '给']",
    #     # "[word = '爱'][word = '不']",
    #     # "[word = '宁可'|word = '也']",
    #     # "[word = '洗'][word = '澡']",
    #     # "[word = '克服一切困难']",
    #     # "[word = '克服'][word='一切困难']",
    #     "[word = '把' | word = '被'][]{0,4}[word='变成']",
    #     "[word = '我们'",
    #     "[word = '拆分'",
    #     "[word = '文档'",
    #     "[word = '拭目以待']",
    #             ]
    f = open('./test_cql.txt', encoding='utf_8')
    f_out = open('./test_cql_anydoc.txt', mode='w', encoding='utf_8')
    jssCql = JSSCql('./data/rmrb-table-stanford')
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
            
