FROM python:latest

RUN pip3 install "pymongo[srv]"

COPY ./mongoCnct.py .
COPY ./vitaldata.csv .

CMD python3 ./mongoCnct.py