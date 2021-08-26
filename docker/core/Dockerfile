FROM kalilinux/kali-rolling:latest
MAINTAINER sixdeadbeefs <sixdeadbeefs@protonmail.com>

WORKDIR /root
CMD source /root/.bashrc

#~~~~~ PACKAGE REPO UPDATE && DEPENDANCY INSTALL ~~~~~
RUN apt-get update -y
RUN apt-get install sudo -y

#~~~~ KALI-LINUX-DEFAULT METAPACKAGE INSTALLATION ~~~~ 
RUN DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-core -y
# NOTE: CHANGING ANYTHING BEFORE THE ABOVE LINE WILL RESULT IN BUILD
# TIME OF APPROX 20 MINS

#~~~~~ APT-GET PACKAGE UPGRADES && INSTALLATIONS ~~~~~
RUN apt-get dist-upgrade -y
RUN apt-get install python2.7 python-pip python-dev git -y
RUN pip3 install --upgrade pip 
RUN pip3 install --upgrade pwntools

#~~~~~~~~~~~~~~~ ENVIRONMENT VARIABLES ~~~~~~~~~~~~~~~
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

#~~~~~~~~~~~~~~~~~~ EDITING .BAHSRC ~~~~~~~~~~~~~~~~~~
COPY aliases aliases
RUN cat aliases >> .bashrc
RUN rm aliases
