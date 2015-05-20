from boto.s3.connection import S3Connection
from boto.s3.connection import Location
import uuid

ACCESS_KEY = USER_ACCESS_KEY
SECRET_KEY = USER_SECRET_KEY

# create a connection to the service
conn = S3Connection(ACCESS_KEY, SECRET_KEY)

# create a bucket in default region
bucket_name = 'awsbucket' + uuid.uuid1().hex
bucket = conn.create_bucket(bucket_name)
print bucket

# create a bucket in specified location
bucket_name1 = 'awsbucket' + uuid.uuid1().hex
bucket =  conn.create_bucket(bucket_name, location=Location.USWest)
print bucket

# 
# delete the buckets
conn.delete_bucket(bucket_name)
conn.delete_bucket(bucket_name1)



