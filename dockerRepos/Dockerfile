FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install git
RUN apt-get -y install python3-pip
RUN pip3 install flask
RUN mkdir gaDeployment
RUN cd gaDeployment
RUN git clone https://github.com/elusive666/ML_Deployment.git
#COPY dummy.txt gaDeployment/dummy.txt
#ENV JAVA_HOME /usr/local
WORKDIR ML_Deployment
RUN pip3 install -r requirements.txt

WORKDIR bin
CMD ["python3", "summaryService.py"]