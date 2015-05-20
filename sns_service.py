import boto.sns

ACCESS_KEY = USER_ACCESS_KEY
SECRET_KEY = USER_SECRET_KEY

conn = boto.sns.connect_to_region("us-east-1", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
print conn

regions = boto.sns.regions()
print regions

topic = conn.create_topic("myTopic")
print topic

response = conn.publish(topic='arn:aws:sns:us-east-1::myTopic', message='This is a first message')
print response