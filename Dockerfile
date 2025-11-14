FROM python:3.12-slim

WORKDIR /app

COPY local_ip_app.py .

RUN pip install flask requests

EXPOSE 8080

CMD ["python", "local_ip_app.py"]
