import boto3

client=boto3.client('datapipeline')

response =client.list_pipelines()

response= response[u'pipelineIdList']

for x in range(len(response)):
 print response[x][u'name']
