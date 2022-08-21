FROM python:3.9.12

WORKDIR /Users/muttulow/Desktop/03-Applications/containerized_webapp

COPY . .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","-m","src.algo_fastapi"]