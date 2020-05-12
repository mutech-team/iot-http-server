FROM ubuntu

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN apt install -y libpq-dev python-dev
RUN ln -sfn /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install pipenv
COPY Pipfile.lock .
COPY Pipfile .
RUN pipenv install --system --deploy --ignore-pipfile
ADD ./apache2.conf /etc/apache2/sites-available/000-default.conf
COPY ./mutech_iot_api /var/www/html
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]