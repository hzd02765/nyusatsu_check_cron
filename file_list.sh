#!/bin/sh

# ファイルやディレクトリを検索し、ファイルに書き出す

# find : ファイルやディレクトリを検索
# -type c
# 指定したファイル・タイプを検索する。
# cはdがディレクトリを、fが通常ファイルを、lがシンボリック・リンクを表す
# -name pattern
# ファイル名がpatternと同じファイルを検索する。
# ワイルド・カードを用いることができる

# find /usr/local/app/nyusatsu_check_cron -type f -name "*.py" | sort > file_list.txt
find -type f -name "*.py" | sort > file_list.txt
