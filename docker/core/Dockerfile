FROM kalilinux/kali-rolling:latest
MAINTAINER sixdeadbeefs <sixdeadbeefs@protonmail.com>

WORKDIR /root
CMD source /root/.bashrc

#~~~~~ PACKAGE REPO UPDATE && DEPENDANCY INSTALL ~~~~~
RUN apt-get update -y

#~~~~ KALI-LINUX-DEFAULT METAPACKAGE INSTALLATION ~~~~ 
RUN DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-core -y

#~~~~~ APT-GET PACKAGE UPGRADES && INSTALLATIONS ~~~~~
RUN apt-get install python3-pip\
	python-dev\
	git\
	sudo\
	vim\
	dirb\
	nmap\
	wordlists\
	libc6-i386\
	ltrace\
	strace\
	wget\
	curl\
	-y

RUN pip3 install --upgrade pip 
RUN pip3 install --upgrade pwntools
RUN sudo dpkg --add-architecture i386

#~~~~~~~~~~~~~~~~~ SETTING UP PWNDBG ~~~~~~~~~~~~~~~~~
RUN git clone https://github.com/pwndbg/pwndbg
RUN cd pwndbg && ./setup.sh

#~~~~~~~~~~~~~~~ ENVIRONMENT VARIABLES ~~~~~~~~~~~~~~~
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

#~~~~~~~~~~~~~~~~~~ SETTING UP TMUX ~~~~~~~~~~~~~~~~~~
COPY .tmux.conf .

#~~~~~~~~~~~~~~~~~~ EDITING .VIMRC ~~~~~~~~~~~~~~~~~~
ADD .vimrc .vimrc

#~~~~~~~~~~~~~~~~~~ EDITING .BAHSRC ~~~~~~~~~~~~~~~~~~
COPY aliases aliases
RUN cat aliases >> .bashrc
RUN rm aliases

#~~~~~~~~~~~~~~~ FINAL PACKAGE UGRADE ~~~~~~~~~~~~~~~
RUN apt-get upgrade -y
