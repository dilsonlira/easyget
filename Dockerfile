FROM python:3.6-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ src/
COPY tests/ tests/
CMD ["python", "src/easyget.py"]
#CMD ["pytest", "./tests"]