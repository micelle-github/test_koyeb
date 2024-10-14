FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY .env .
COPY hello.py .
COPY test.py .
COPY text_send.py .

CMD ["python", "text_send.py"]
