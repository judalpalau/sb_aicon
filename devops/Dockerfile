FROM python:alpine3.14
RUN apk update \
    && apk add --update build-base git make nano curl \
    && apk add libffi-dev openssh tzdata \
    && apk add gcc libc-dev g++ libffi-dev libxml2 \
    && pip install --upgrade pip \
    && pip install gunicorn

### Build python requirements
RUN mkdir -p /app-run
WORKDIR /app-run

COPY devops/requirements.txt /app-run/
RUN pip install -r requirements.txt

### Expose Flask server
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

EXPOSE 8000

### Run with gunicorn
COPY entrypoint.sh /app-run/entrypoint.sh
COPY conf_gunicorn.py /app-run/conf_gunicorn.py
RUN chmod +x /app-run/entrypoint.sh
ENTRYPOINT ["/app-run/entrypoint.sh"]