FROM python
WORKDIR /app
RUN pip install flask redis
ADD app.py /app/app.py
EXPOSE 80
CMD ["python","app.py"]

