FROM python:3.9
COPY . /app
RUN pip install -r /app/requirements.txt
ENV FLASK_APP="app.py"
ENV FLASK_RUN_PORT=5000
CMD ["python", "/app/app.py"]
