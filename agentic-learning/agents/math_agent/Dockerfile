FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV PYTHONPATH=/app
ENV PORT=8081
EXPOSE 8081
CMD ["uvicorn", "agents.math_agent.server:http_app", "--host", "0.0.0.0", "--port", "8081"]
