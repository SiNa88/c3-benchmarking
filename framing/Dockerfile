FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /work

RUN apt-get update && apt-get install -y python3 python3-pip python3-opencv wget
RUN pip3 install scikit-learn numpy opencv-python


#RUN wget -O  /usr/local/bin/kubetools https://github.com/kubemq-io/kubemqctl/releases/download/latest/kubemqctl_linux_386
#RUN chmod +x /usr/local/bin/kubetools

COPY  split.py /work
COPY 20-20000.mp4 /work
COPY run.sh /work
ENTRYPOINT ["/work/run.sh" , "20-20000.mp4" , "data-20-20000", "/out", "MQ1"]