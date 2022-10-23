FROM ubuntu:focal

RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get -y install libseccomp-dev
RUN apt-get clean
RUN useradd -m user

ADD home/ /home/user/
ADD xinetd /etc/xinetd.d/user

RUN chown -R user:user /home/user
RUN chown root:root /home/user/flag.txt
RUN chown user:root /home/user/worldcup
RUN chmod 444 /home/user/flag.txt
RUN chmod +x /home/user/run.sh
RUN chmod +x /home/user/worldcup

USER user
WORKDIR /home/user

CMD ["/usr/sbin/xinetd", "-dontfork"]