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

        start = time.time()
        lst_result = self.jss.RunSql("SELECT TOP 200 * FROM sen WHERE content LIKE '{}';".format(word))
        end = time.time()
        print(end - start)
        map_result = {}
        for item in lst_result:
            id ='{}-{}-{}'.format(item['doc_id'], item['pass_id'], item['sen_id'])
            map_result[id] = item['content']
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
            return result1 | result2
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
            out_lst = {}
            for item in result_lst:
                begin_pos = -1
                valid_item = True
                for word in word_lst:
                    find_pos = result_lst[item].find(word)
                    if (begin_pos != -1 and find_pos - begin_pos > 6):
                        valid_item = False
                        break

                    if (find_pos <= begin_pos):
                        valid_item = False
                        break
                    else:
                        begin_pos = find_pos

                if valid_item:
                    out_lst[item] = result_lst[item]

            return out_lst
        
        return {}

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
                lst_result_id.append(result)
            result = lst_result_id[0]
            for i in range(1, len(lst_result_id)):
                result = {k1:result[k1] for k1 in result if k1 in lst_result_id[i]}
        else:
            result = self.search_fast(search_tree.map_tree)
        

        return result


if __name__ == '__main__':

    cql_statements = [
        "[word = '克服一切困难']",
        "[word = '好的'][word = '不好的']",
        "[word = '文化'][word = '交流']",
        "[word = '把'][word = '给']",
        "[word = '与其'][word = '不如']",
        "[word = '把'|word='被'][word = '给']",
        "[word = '爱'][word = '不']",
        "[word = '宁可'|word = '也']",
        "[word = '洗'][word = '澡']",
        ]

    jssCql = JSSCql('./data/table/table.lst')

    for statement in cql_statements:
        print("cql statement = {}".format(statement))
        result = jssCql.cql_search(statement)
        print("result = {}".format(len(result)))
        total = 0
        for i, item in enumerate(result):

            print(i, item, result[item])
            break
            
        print()
