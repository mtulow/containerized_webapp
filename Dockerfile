FROM python:3.8.5
WORKDIR /usr/src/app
COPY . .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","-m","src.algo_fastapi"]
