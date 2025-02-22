FROM ubuntu


WORKDIR /app

RUN apt update && apt install -y  python3 python3-pip 

COPY . . 

RUN pip install -r requirements.txt --break-system-packages

CMD ["python3" , "app.py"]
