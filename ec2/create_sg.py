import boto3


def create_security_group(name, ip_addr):
    ec2_client_ = boto3.resource('ec2')

    security_group = ec2_client_.create_security_group(
        Description='Allow inbound traffic',
        GroupName=name,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name
                    },
                ]
            },
        ],
    )

    security_group.authorize_ingress(
        CidrIp=ip_addr + '/32',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp',
    )
    security_group.authorize_ingress(
        CidrIp=ip_addr + '/32',
        FromPort=80,
        ToPort=80,
        IpProtocol='tcp',
    )

    print(f'Security Group {security_group.id} has been created')
    return security_group


if __name__ == "__main__":
    from requests import get
    ip = get('http://ifconfig.me/ip').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))
    create_security_group("Just my SG",ip)
