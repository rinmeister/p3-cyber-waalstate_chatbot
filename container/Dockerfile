FROM python:latest

RUN apt update && apt install -y openssh-server git neovim
RUN apt install -y net-tools iputils-ping tcpdump
RUN mkdir ~/git
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN git clone https://rinmeister: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@github.com/AIM-Propedeuse/p3-cyber-chatbot.git ~/git/p3-cyber-chatbot
EXPOSE 6666
CMD ["python", "/root/git/p3-cyber-chatbot/chatbot.py"]

