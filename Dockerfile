FROM python:3.9

WORKDIR /reverseip

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
RUN apt update && apt install pkg-config -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
