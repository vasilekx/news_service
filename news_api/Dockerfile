FROM python:3.11.3-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
#CMD ["gunicorn", "news_api.wsgi:application", "--bind", "0:8000" ]

EXPOSE 8000
ENTRYPOINT ["sh", "./scripts/server-entrypoint.sh"]