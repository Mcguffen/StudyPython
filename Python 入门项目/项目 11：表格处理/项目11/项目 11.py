'''
项目 11


本次作业要给一张表格添加一列数据
表格的内容格式如下，第一行是 4 个表头，用英文逗号隔开
接下来的每一行都是 4 个数据，其中产地是区、县
需要特别注意的是，产地一栏的数据有可能是全称 商河县 也可能是 商河

序号,商品名,产地,价格
1,水,商河县,10
2,刀,商河,11


我们的程序要把上面的表格内容进行处理，得到下面的新表格
新表格加入了一列 产地（省）
这样的工作在非常多的公司中都是手动去添加的

序号,商品名,产地（省）,产地,价格
1,水,山东省,商河县,10



省、自治区、直辖市和下辖区县的关系，可以从下面的民政部链接数据中获取到
http://www.mca.gov.cn/article/sj/tjbz/a/2017/201801/201801151447.html

具体的思路是把网页上的数据复制到一个文件中
在 py 中打开并分析这个文件
行政区划代码的格式是 xxyyzz, xx 是省，yy 是市，zz 是区、县
前两位是省代码，根据省代码就可以知道这个区、县是哪个省的


有思路上的问题请在群内讨论


需要处理的文件 11-info.csv 在群文件中
'''


