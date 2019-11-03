import os
import boto3
import codecs
from memory_profiler import profile
from smart_open import open
from dotenv import load_dotenv


test_bucket='polyglot-computing.data'
test_key='test/emails_sm.dat'

# python -m memory_profiler stream_file.py

@profile
def load_s3():
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_secret)
    data = s3.get_object(Bucket=test_bucket, Key=test_key)
    contents = data['Body'].read()
    print(contents)

@profile
def stream_s3():
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_secret)
    obj = s3.get_object(Bucket=test_bucket, Key=test_key)
    body = obj['Body']
    cnt = 0
    for ln in codecs.getreader('utf-8')(body):
        cnt += 1
        if cnt % 10000 == 0:
            print(ln.rstrip())

@profile
def stream_s3_smart_open():
    cnt = 0
    for line in open("s3://{}/{}".format(test_bucket, test_key)) :
        cnt += 1
        if cnt % 10000 == 0:
            print(line.rstrip())

# python -m memory_profiler stream_file.py
if __name__ == '__main__':

    global aws_access_key
    global aws_access_secret

    load_dotenv()

    aws_access_key = os.getenv("aws_access_key")
    aws_access_secret = os.getenv("aws_access_secret")
    print('AWS - {} / {}'.format(aws_access_key, aws_access_secret))
    
    #load_s3()
    #stream_s3()
    stream_s3_smart_open()