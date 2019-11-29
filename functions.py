import json
import boto3

def get_instances(e,c):
    client = boto3.client('ec2')
    if isinstance(e, dict):
        query_string_prameters = e['queryStringParameters']
        # null = None
        # key: value
        # state: running
        state = None
        args = {}
        if query_string_prameters:
            state = query_string_prameters.get('state')

        if state:
            args = {
                "Filters":[
                    {
                        "Name": 'instance-state-name',
                        "Values": [
                            state
                        ]
                    }
                ]
            }


        results = client.describe_instances(**args)

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
            'body': json.dumps({"instances": processed_instances})
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

if __name__ == '__main__':

    get_instances({'queryStringParameters': {'state': 'running'}},2)
