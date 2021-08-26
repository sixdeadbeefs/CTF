FROM kalilinux/kali-rolling:latest
MAINTAINER sixdeadbeefs <sixdeadbeefs@protonmail.com>

WORKDIR /root
CMD source /root/.bashrc

#~~~~ KALI-LINUX-DEFAULT METAPACKAGE INSTALLATION ~~~~ 
RUN apt-get install sudo -y
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-large -y

#~~~~~~~~~~~~~~~ PACKAGE INSTALLATIONS ~~~~~~~~~~~~~~~
RUN pip3 install pwntools

#~~~~~~ PACKAGE REPO UPDATES && PACKAGE UPGRADE ~~~~~~
RUN apt-get update -y && apt-get dist-upgrade -y

#~~~~~~~~~~~~~~~ ENVIRONMENT VARIABLES ~~~~~~~~~~~~~~~
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

#~~~~~~~~~~~~~~~~~~ EDITING .BAHSRC ~~~~~~~~~~~~~~~~~~
COPY aliases aliases
RUN cat aliases >> .bashrc
RUN rm aliases
