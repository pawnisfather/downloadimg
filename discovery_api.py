# cat java_discovery.py
# /usr/bin/python3
# This script is used to discovery disk on the server
import os
import json
import sys


api_name_file = sys.argv[1]
apis = []
if os.path.isfile(api_name_file):
    f=open(api_name_file)
    t=f.readlines()
#     #   print 'java_names_file exists!
#     #####
#     ##### here should use % (java_names_file) instead of using the python variable java_names_file directly inside the '''   ''' quotes
#     #####
#
#     args = '''awk -F':' '{print $1':'$2}' %s''' % (java_names_file)
#     t = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE).communicate()[0]
# # elif glob.glob('/opt/xx/*_tomcat') and not os.path.isdir('/opt/logs/logstash') and not os.path.isdir('/opt/app/elasticsearch/config'):
# elif glob.glob('/data/open/*.jar'):
#     t = subprocess.Popen('cd /data/open && ls *.jar|grep jar', shell=True, stdout=subprocess.PIPE)

    for api in t:
        if len(api) != 0:
            apis.append({'{#API_NAME}': api.strip('\n').strip(':')})
print(json.dumps({'data': apis}, indent=4, separators=(',', ':')))
