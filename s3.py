import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    #for key in bucket.objects.all():
        print "Buckets are "+ (bucket.name)
       # print "Objects are "+ (key.key)


acl = bucket.Acl()
for grant in acl.grants:
    print(grant['Grantee']['DisplayName'], grant['Permission'])
