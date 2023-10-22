FROM python:3.11-slim

RUN pip install pandas seaborn matplotlib

WORKDIR /test
COPY ["StressLevelDataset.csv", "./"]
ADD test.py .

CMD [ "python", "./test.py" ]