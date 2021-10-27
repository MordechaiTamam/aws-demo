sudo yum install docker -y
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
sudo su $USER
docker run hello-world
docker run -d --name docker-nginx  -p 80:80 nginx