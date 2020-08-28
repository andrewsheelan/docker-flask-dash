FROM python:3.8.5

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

COPY  . .

CMD ./run
