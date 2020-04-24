FROM python:3.7
RUN mkdir /code
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

WORKDIR /code
COPY . /code/
COPY ./entrypoint.sh /entrypoint
RUN ln -s /usr/local/bin/entrypoint.sh /
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools
RUN apt-get install -y gcc unixodbc-dev

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN pip install pyodbc --user
RUN pip install -e .

EXPOSE 5000
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]

