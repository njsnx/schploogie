import json
import boto3

def get_instances(e,c):
    client = boto3.client('ec2')
    results = client.describe_instances()
    print(results)

def get_health_events(e, c):
    client = boto3.client('health')
    health = client.describe_events()
    print(health)

if __name__ == '__main__':
    
    get_instances(1,2)