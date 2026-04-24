FROM python:latest

RUN apt update && apt install -y openssh-server git neovim
RUN apt install -y net-tools iputils-ping tcpdump
RUN mkdir ~/git
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN git clone https://github.com/rinmeister/p3-cyber-waalstate_chatbot.git ~/git/p3-cyber-waalstate_chatbot
EXPOSE 4242
CMD ["python", "/root/git/p3-cyber-waalstate_chatbot/waalstate_chatbot.py"]

