FROM kalilinux/kali-rolling:latest
MAINTAINER sixdeadbeefs <sixdeadbeefs@protonmail.com>

WORKDIR /root
CMD source /root/.bashrc

#~~~~~ PACKAGE REPO UPDATE && DEPENDANCY INSTALL ~~~~~
RUN apt-get update -y
RUN apt-get install sudo -y

#~~~~ KALI-LINUX-DEFAULT METAPACKAGE INSTALLATION ~~~~ 
RUN DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-core -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install kali-linux-large -y
# NOTE: CHANGING ANYTHING BEFORE THE ABOVE 2 LINES WILL RESULT IN BUILD
# TIME OF APPROX 50 MINS
#~~~~~ APT-GET PACKAGE UPGRADES && INSTALLATIONS ~~~~~
RUN apt-get dist-upgrade -y
RUN pip3 install --upgrade pip 
RUN pip3 install --upgrade pwntools
RUN sudo dpkg --add-architecture i386
RUN sudo apt-get install libc6-i386 ltrace strace -y

#~~~~~~~~~~~~~~~~~ SETTING UP PWNDBG ~~~~~~~~~~~~~~~~~
RUN git clone https://github.com/pwndbg/pwndbg
RUN cd pwndbg && ./setup.sh

#~~~~~~~~~~~~~~~ ENVIRONMENT VARIABLES ~~~~~~~~~~~~~~~
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

#~~~~~~~~~~~~~~~~~~ SETTING UP TMUX ~~~~~~~~~~~~~~~~~~
COPY .tmux.conf .

#~~~~~~~~~~~~~~~~~~~ EDITING VIMRC ~~~~~~~~~~~~~~~~~~~
COPY .vimrc .vimrc

#~~~~~~~~~~~~~~~~~~ EDITING .BAHSRC ~~~~~~~~~~~~~~~~~~
COPY aliases aliases
RUN cat aliases >> .bashrc
RUN rm aliases

#~~~~~~~~~~~~~~~ FINAL PACKAGE UPGRADE ~~~~~~~~~~~~~~~
RUN apt-get upgrade -y
