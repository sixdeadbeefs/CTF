FROM kalilinux/kali-rolling:latest
MAINTAINER sixdeadbeefs <sixdeadbeefs@protonmail.com>

WORKDIR /root
CMD source /root/.bashrc

#Update apt-get repos, and upgrade all outdated packages.
RUN apt-get update && apt-get dist-upgrade -y

#Install kali-linux-large meta-package with with DEBIAN_FRONTEND set
#to noninteractive, otherwise the installation will prompt for user
#input and the docker build command will fail. 
RUN apt-get install sudo -y
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-large -y

RUN sudo apt-get update -y
RUN pip3 install pwntools
RUN sudo apt-get upgrade -y

#Setting JAVA home
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

#Copying over .bashrc file because it has some useful aliases
COPY aliases aliases
RUN cat aliases >> .bashrc
RUN rm aliases
