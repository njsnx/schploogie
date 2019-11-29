import json
import boto3

def get_instances(e,c):
    client = boto3.client('ec2')
    results = client.describe_instances()
    # print(results)
    processed_instances = []

    for reservations in results['Reservations']:
        # print(reservations)
        for instance in reservations['Instances']:
            processed_instance = {}

            processed_instance['instance_id'] = instance['InstanceId'] 
            processed_instance['instance_state'] = instance['State']['Name']
            
            for tags in instance['Tags']:
                if tags["Key"] == 'Name':
                    # print(tags["Value"])
                    processed_instance['name'] = tags['Value']
            processed_instances.append(processed_instance)
    
    response = {
        'statusCode': 200,
        'body': {
            "instances": json.dumps(
            processed_instances
        )
        }
    }

    print(json.dumps(response))
    return response

    #
    # {
    #     body: {
    #         "instances": [
    #             {
    #                 "instance-id":12312312
    #                 "instance-name":adasdsad
    #                 "state": dasdada
    #             }
    #         ]
    #     }
    # }

def get_health_events(e, c):
    client = boto3.client('health')
    health = client.describe_events()
    print(health)

if __name__ == '__main__':
    
    get_instances(1,2)