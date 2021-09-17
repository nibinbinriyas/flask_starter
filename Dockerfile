FROM python:3.8-alpine
# define the present working directory
WORKDIR /nibz/app
# copy the contents into the working dir
COPY app.py /nibz/app
COPY ./templates/ /nibz/app/templates
COPY requirements.txt /nibz/app
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","app.py"]