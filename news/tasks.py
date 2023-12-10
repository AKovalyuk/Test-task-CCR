from core.celery import app


@app.task(name='send_email')
def send_email():
    print('Hello world')
