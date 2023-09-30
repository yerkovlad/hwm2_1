FROM python:3.8
RUN apt-get update && apt-get install -y \
WORKDIR /app
COPY . /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
CMD ["python", "personal_assistant.py"]
