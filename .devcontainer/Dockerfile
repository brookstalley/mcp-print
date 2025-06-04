FROM python:3.12-slim

WORKDIR /app
COPY . .

# Build the Printful SDK and install deps
RUN pip install --upgrade pip 
RUN pip install ./printful-client

RUN pip install -r requirements.txt

CMD ["python", "server.py"]