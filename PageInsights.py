import urllib2
import json
import csv
import datetime
import time

def get_page_data(page_id,access_token,dt_time):
    api_endpoint = "https://graph.facebook.com/v2.6/"
    fb_graph_url = api_endpoint+page_id+"/insights/?fields=name,title,description,values,period&since="+str(dt_time)+"&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "14044019798" # username or id
token = "EAACEdEose0cBAItzYjtxKoGXLyMGARrQ1C33m2ePhOLg8GWYSMeVfAkoGAuLzTng79MdsPGzN1PmAtlIoFxH402ivUHB96KeT69RAvbBqes63c7gZAssW2nCJN90amRdjAw4ZCKI917C0RKSuwbJSd22RLNeBIrMMSncWXTHjUbjqZAfVlT"  # Access Token
dtime = datetime.datetime.now()- datetime.timedelta(days=1)
dt_time=time.mktime(dtime.timetuple())
page_data = get_page_data(page_id,token,dt_time)
#dict =page_data
dict=page_data[u'data']
csvFile=open('PageInsights.csv', 'w+') 
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
csvWriter.writerow(['Metric Name', 'Metric Title','Metric Long Description,Data'])
for x in range(100):
 #r=dict[x] 
 q=dict[x][u'values']
 s=q[0]
 csvWriter.writerow([dict[x][u'name'],dict[x][u'title'],dict[x][u'description'],s[u'value']])
csvFile.close()
