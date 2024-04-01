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

    def search_jss(self, node):
        if 'exp_node1' in node:
            word = node['exp_node1']['value'].replace("'", "")
        else:
            word = node['value'].replace("'", "")
        start = time.time()
        lst_result = self.jss.RunSql("SELECT doc_id, pass_id, sen_id, content FROM sen WHERE content LIKE '{}';".format(word))
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
            return self.search_jss(node)

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
        for node in search_tree.map_tree:
            result = self.search_exp(node)
            lst_result_id.append(result)
        
        result = lst_result_id[0]
        for i in range(1, len(lst_result_id)):
            result = {k1:result[k1] for k1 in result if k1 in lst_result_id[i]}

        return result


if __name__ == '__main__':

    cql_statements = [
        "[word = '深圳' & word = '上海']{0,1}[word = '天气']",
        "[word = '哈尔滨' | word = '深圳']{0,1}[word = '温度']"]

    jssCql = JSSCql('./data/table/table.lst')

    for statement in cql_statements:
        print("cql statement = {}".format(statement))
        result = jssCql.cql_search(statement)
        print("result = {}".format(len(result)))
        for i, item in enumerate(result):
            print(i, result[item])
        print()
