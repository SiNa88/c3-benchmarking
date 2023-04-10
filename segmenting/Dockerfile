FROM ubuntu

RUN apt-get update && apt-get install -y ffmpeg python3 python3-pip
RUN pip3 install  ffmpeg-python

# Add scirpts and video files
ADD . /work
# Set the working directory
WORKDIR /work

RUN chmod 777 /work/*

#RUN wget -O  /usr/local/bin/kubetools https://github.com/kubemq-io/kubemqctl/releases/download/latest/kubemqctl_linux_386
#RUN chmod +x /usr/local/bin/kubetools

ENTRYPOINT ["python3", "split.py"]
