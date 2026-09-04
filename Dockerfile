# ux-compose product ASGI image
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "uvicorn[standard]" fastapi ux-compose ux-dom ux-behavior

COPY . .

# CSS: run `uxcompose build` before `docker build` so output.css is in COPY.
# Or compile in the image (uncomment):
# RUN pip install --no-cache-dir pytailwindcss \
#  && uxcompose build --skip-import

EXPOSE 8080
CMD ["sh", "-c", "uvicorn app:asgi --host 0.0.0.0 --port ${PORT:-8080}"]
