FROM python:3.9-slim
WORKDIR /home/app1
COPY app.py /home/app1
COPY requirements.txt /home/app1
RUN pip install -r requirements.txt
CMD ["python", "app.py"]