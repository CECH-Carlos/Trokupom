FROM python:3.10


WORKDIR /Trokupom-Teste
COPY . .
RUN pip install -r requirements.txt


CMD python app.py