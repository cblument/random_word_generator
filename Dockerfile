FROM python:3.12.2-slim

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY generate_random_words.py /

