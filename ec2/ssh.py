import boto3

import botocore

import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Connect/ssh to an instance

def set_machine(address):
    client.connect(address, username='ec2-user')
    try:

        # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
        # Execute a command(cmd) after connecting/ssh to an instance
        stdin, stdout, stderr = client.exec_command("sudo yum install docker -y")
        print(stdout.read())
        stdin, stdout, stderr = client.exec_command("sudo systemctl start docker")
        print(stdout.read())
        stdin, stdout, stderr = client.exec_command("sudo docker run -d --name docker-nginx  -p 80:80 nginx")
        print(stdout.read())
        # close the client connection once the job is done
    finally:
        try:
            client.close()
        except BaseException as ex:
            print(ex)