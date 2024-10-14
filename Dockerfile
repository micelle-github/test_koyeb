FROM python:3.12

WORKDIR /usr/src/app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY .env .
COPY hello.py .
COPY test.py .
COPY text_send.py .

#RUN apt-get update && apt-get install -y bash
#RUN bash -c "source .env && export"


CMD ["python", "hello.py"]




