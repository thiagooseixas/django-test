# Container base: Python 2.7.15-stretch Linux
FROM python:2.7.15-stretch

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /code

# Define o diretório de trabalho
WORKDIR /code

# "Copia" arquivo requirements.txt para o diretorio code
ADD requirements.txt /code/

# Executa o pip
RUN pip install -r requirements.txt

# "Copia" os arquivos locais para o diretorio code no container 
ADD . /code/        
