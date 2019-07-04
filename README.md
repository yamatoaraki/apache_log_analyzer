# ツール・ライブラリの名前

Apache log analyzer

## 簡単な説明

Apacheのログを解析するツールです。
ホストごとのアクセス件数と時間帯別のアクセス件数を出力します。

***動作イメージ***

![動作イメージ](https://user-images.githubusercontent.com/39017068/60689748-a85a9780-9efb-11e9-8d7f-ce6962fa225c.png)

## 必要要件

- python 3.7以上

- apache_log_parserのインストール
```

　$ pip install apache_log_parser

```
## 使い方

1. 基本的な使い方
   -input_fileオプションを指定しログファイルを引数として与える。引数のファイルの数はいくらでも良い。
```

  （例）python apache_log_analyzer.py -input_file access_log1
  （例）python apache_log_analyzer.py -input_file access_log1 access_log2

```

2. 期間を指定する。-termオプションを指定し引数としてisoフォーマット形式で２つの引数を与える。この際に始まりの日時と終わりの日時の順番は問わない。
```

  （例）python apache_log_analyzer.py -input_file access_log1 -term 2018-06-18T23:59:59 2018-06-18T00:00:00
  （例）python apache_log_analyzer.py -input_file access_log1 -term 2018-06-18T00:00:00 2018-06-18T23:59:59
  （例）python apache_log_analyzer.py -input_file access_log1 access_log2 -term 2018-06-18T23:59:59 2018-06-18T00:00:00

```
## 試してみる

```
$ git clone https://github.com/yamatoaraki/apache_log_analyzer.git
$ cd apache_log_analyzer
$ python apache_log_analyzer.py -input_file access_log1 access_log2 -term 2018-06-17T23:59:59 2018-06-17T00:00:00

```
