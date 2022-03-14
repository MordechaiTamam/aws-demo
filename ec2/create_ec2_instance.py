import boto3


def create_instance(security_group,key_name):
    ec2_client = boto3.resource("ec2")
    response = ec2_client.create_instances(
        ImageId="ami-0c2b8ca1dad447f8a",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName=key_name,
        SecurityGroupIds=[
            security_group,
        ],
        BlockDeviceMappings = [{"DeviceName": "/dev/xvda", "Ebs": {"VolumeSize": 10}}]
    )
    instance_ = response[0]
    print(f"Successfully created instance:\n {instance_}")
    return instance_


if __name__ == "__main__":
    import time
    instance = create_instance('<ENTER_THE_SECURITY_GROUP_ID>','ubuntu-devops-experts')
    instance.wait_until_running()
    instance.load()
    print(f"created instance with id: {instance.id}")
    time.sleep(60)
    print(instance.public_dns_name)
