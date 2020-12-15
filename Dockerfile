from python:3.6

# create workdir
WORKDIR /app

# Install required dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt 

# Build app from source code
COPY src /app

EXPOSE 8090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]
