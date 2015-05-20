import boto.sqs
from boto.sqs.message import Message

ACCESS_KEY = USER_ACCESS_KEY
SECRET_KEY = USER_SECRET_KEY

# create a connection
conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
print conn

# create a queue
q = conn.create_queue('myqueue')
print q

# listing all the queues for this account
list = conn.get_all_queues()
print list

# getting a queue by name
my_queue = conn.get_queue('myqueue')
print my_queue

# writing a message in queue
m = Message()
m.set_body('This is my first message.')
q.write(m)

# reading messages from queue
rs = q.get_messages()
print len(rs)
m = rs[0]
print m.get_body()

# Delete message 
q.delete_message(m)

# Delete the queue
conn.delete_queue(q)

