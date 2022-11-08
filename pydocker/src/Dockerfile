FROM python:latest

RUN pip3 install "pymongo[srv]"

COPY ./mongoCnct.py .

CMD python3 ./mongoCnct.py