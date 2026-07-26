FROM python:3
COPY app/ /app/
WORKDIR /app
RUN pip install flask flask_restful
EXPOSE 3333
CMD ["python", "app.py"]
