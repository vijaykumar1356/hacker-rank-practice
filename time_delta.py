# time_delta problem in Hacker Rank website
import datetime
fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs(datetime.datetime.strptime(input(), fmt) - datetime.datetime.strptime(input(), fmt)).total_seconds()))
