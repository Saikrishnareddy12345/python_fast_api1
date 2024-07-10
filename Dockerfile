FROM python:alpine3.20
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "uvicorn sample:app --reload --host 0.0.0.0 --port 80" ]