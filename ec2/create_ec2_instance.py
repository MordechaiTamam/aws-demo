import boto3


def create_instance(security_group):
    ec2_client = boto3.resource("ec2")
    response = ec2_client.create_instances(
        ImageId="ami-0c2b8ca1dad447f8a",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ubuntu-devops-experts",
        SecurityGroupIds=[
            security_group,
        ],
        # SubnetId='string',
        # TagSpecifications=[
        #     {
        #         'ResourceType': 'client-vpn-endpoint' | 'customer-gateway' | 'dedicated-host' | 'dhcp-options' | 'egress-only-internet-gateway' | 'elastic-ip' | 'elastic-gpu' | 'export-image-task' | 'export-instance-task' | 'fleet' | 'fpga-image' | 'host-reservation' | 'image' | 'import-image-task' | 'import-snapshot-task' | 'instance' | 'instance-event-window' | 'internet-gateway' | 'key-pair' | 'launch-template' | 'local-gateway-route-table-vpc-association' | 'natgateway' | 'network-acl' | 'network-interface' | 'network-insights-analysis' | 'network-insights-path' | 'placement-group' | 'reserved-instances' | 'route-table' | 'security-group' | 'security-group-rule' | 'snapshot' | 'spot-fleet-request' | 'spot-instances-request' | 'subnet' | 'traffic-mirror-filter' | 'traffic-mirror-session' | 'traffic-mirror-target' | 'transit-gateway' | 'transit-gateway-attachment' | 'transit-gateway-connect-peer' | 'transit-gateway-multicast-domain' | 'transit-gateway-route-table' | 'volume' | 'vpc' | 'vpc-peering-connection' | 'vpn-connection' | 'vpn-gateway' | 'vpc-flow-log',
        #         'Tags': [
        #             {
        #                 'Key': 'string',
        #                 'Value': 'string'
        #             },
        #         ]
        #     },
        # ]
        BlockDeviceMappings = [{"DeviceName": "/dev/xvda", "Ebs": {"VolumeSize": 10}}]
    )
    instance_ = response[0]
    instance_id_ = instance_.id
    return instance_
