FROM ubuntu:20.04
RUN apt update -y
RUN apt install ssh -y
RUN apt install python3
RUN apt install -y python3-pip
RUN apt install -y dnsutils git
RUN pip3 install awscli

RUN git clone https://github.com/awslabs/awscli-aliases.git
RUN mkdir -p ~/.aws/cli
RUN cp awscli-aliases/alias ~/.aws/cli/alias