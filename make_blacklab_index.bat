# 编译BlackLab 4.0 Alpha2
mvn clean package

# 创建索引文件
java -cp "*" nl.inl.blacklab.tools.QueryTool -f .\test.txt --mode  performance -e gbk ..\..\..\..\data\rmrb-blacklab\

# 查询索引文件
java -cp "*" nl.inl.blacklab.tools.IndexTool create ..\..\..\..\data\rmrb-blacklab ..\..\..\..\data\rmrb-conllu conll-u

