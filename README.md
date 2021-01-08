# data-visualization

> A Vue.js project with echarts

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080

npm run dev

```

## Dataset

``` url
https://www.kaggle.com/danofer/dbpedia-classes

```

本项目所使用的数据集来自 Kaggle， 名为 DBPedia Classes， 是一个包括文本信息， 层次信息可适用于多个任务的文本数据集， 文件类型为 csv 文件， 主要记录了维基百科中众多文章信息， 并进过了一定的清洗与整理， 本课题主要关注于其三层类别的层次信息。

在类别层次信息上， 第一层级为 9 类， 第二层为 70 类， 第三层为 219 类， 共 342782 篇维基百科文章数据， 每一个数据条目分别包括了文章内容， 第一层类别， 第二层类别， 第三层类别， 文章标题， 文章的字数共 6 个字段。

## Details

src\assets\makecsv.py用来从csv文件中选取数据

src\assets\makejson.py用来根据生成的csv数据文件生成json格式的文件（关键）

src\assets\DBP_wiki1000.csv 为从所有数据中随机选取出的1000条数据

test5.json对应的就是1000条数据的json数据
