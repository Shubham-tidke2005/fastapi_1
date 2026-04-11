#base image 
FROM python:3.9

#workdir
WORKDIR /app

#copy
COPY . .

#run 
RUN pip install -r req.txt

#port
EXPOSE 5000

#command
CMD ["python","app.py"]