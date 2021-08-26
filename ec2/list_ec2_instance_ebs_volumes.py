import boto3

AWS_REGION = 'us-east-1'
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-0bcbd56ef8c468dd5'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

device_mappings = instance.block_device_mappings

print(f'Volumes attached to the EC2 instance "{INSTANCE_ID}":')

for device in device_mappings:
    print(f"  - Volume {device['Ebs']['VolumeId']} attached as {device['DeviceName']}")