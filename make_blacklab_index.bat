
java -cp "./tools/BlackLab-v4-alpha2/core/target/*" nl.inl.blacklab.tools.IndexTool --index-type integrated create .\data\rmrb-blacklab-2005 .\data\rmrb-conllu-2005 conll-u
# 编译BlackLab 4.0 Alpha2
#mvn clean package

# 创建索引文件
#java -cp "*" nl.inl.blacklab.tools.QueryTool -f .\test.txt --mode  performance -e gbk ..\..\..\..\data\rmrb-blacklab\

# 查询索引文件
#java -cp "*" nl.inl.blacklab.tools.IndexTool create ..\..\..\..\data\rmrb-blacklab ..\..\..\..\data\rmrb-conllu conll-u

