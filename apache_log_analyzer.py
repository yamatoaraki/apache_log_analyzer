import apache_log_parser
import sys
import collections
import datetime
import argparse

start = []
host = []
time = []

def arg_parse():
    parse_argv = argparse.ArgumentParser(description='Apache log 解析ツール')
    parse_argv.add_argument('-input_file', nargs='*')
    parse_argv.add_argument('-term',nargs=2)
    args = parse_argv.parse_args()
    if args.term == None:
        return args
    else:
        for period in args.term:
            dt = datetime.datetime.fromisoformat(period)
            start.append(dt)
        start.sort()
        return args

def log_analyze():
    argument = arg_parse()
    for input in argument.input_file:
        log_file = open("./" + input)
        parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"')
        raw_log = log_file.readline()
        while raw_log:
            try:
                log_data = parser(raw_log)
            except:
                print("正しいApacheのログファイルであるか確認してください。")
                sys.exit()
            str_to_datetimeobj = datetime.datetime.fromisoformat(log_data['time_received_isoformat'])
            if argument.term != None:
                if start[0] <= str_to_datetimeobj <= start[1]:
                    host.append(log_data['remote_host'])
                    time.append(str(str_to_datetimeobj.hour) + "時")
            else:
                host.append(log_data['remote_host'])
                time.append(str(str_to_datetimeobj.hour) + "時")
            raw_log = log_file.readline()

def output_result():
    for list in [host,time]:
        result = collections.Counter(list).most_common()
        for item in result:
            print(item[0]+ " " + str(item[1]) + "件")

log_analyze()
output_result()
