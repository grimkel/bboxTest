FROM python:3.12.7

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "bbox:app", "--host", "0.0.0.0" ]