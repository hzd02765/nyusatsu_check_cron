# -*- coding: utf-8 -*-

import datetime

import config

class Logger:

    def __init__(self, file_path):
		self.file_path = file_path
		self.log = ""

    def set_log(self, log):
		log = log.replace('\n', '');
	
		log_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
		log_line = log_line + log
		log_line = log_line + "\n"
		self.log = self.log + log_line

    def print_log(self):
		file = open(self.file_path, "a")
		file.write(self.log)
		file.close

# テスト用
if __name__ == '__main__':
	file_name = "access_log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
	logger = Logger(file_name)
	text = u'''
insert into j_nyusatsu(
	upd_date
)
values(
	%s, 
	%s, 
	0, 
	0, 
	now(), 
	now()
)

'''
	logger.set_log("aa")
	logger.set_log(text)
	logger.print_log()