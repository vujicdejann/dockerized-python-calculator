FROM python:3.8-slim

WORKDIR /app

COPY calculator.py /app

CMD ["python", "calculator.py"]

ENTRYPOINT ["python", "calculator.py"]