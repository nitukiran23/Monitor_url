FROM python:3.9.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY url_monitor.py url_monitor.py
CMD [ "python3", "url_monitor.py", "--host=0.0.0.0"]
