FROM python:3.6

ENV PYTHONPATH=/app

# Set the working directory to /app
WORKDIR /app

# Only install requirements.txt if requirements file has changed
ADD ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app
RUN pip uninstall .
RUN cd /usr/local/lib/python3.6/site-packages && python /app/setup.py develop

# Override this cmd with docker-compose depending on whether its worker or manage or shell or the application server
CMD ["/bin/bash"]