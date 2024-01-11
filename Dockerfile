FROM python:3.10.1

WORKDIR /FAST_API

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /FAST_API

CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port=8000"]

EXPOSE 8000