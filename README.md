# federalreserve-python
Flask application to read federal reserve data and incrementally persist to a postgresql database

Application details
-------------------
1. Docker Container for the Flask App 
2. Docker Container for Postgres Persistence
3. Application runs on gunicorn server @8000 and is mapped to host 8000.
4. Application exposes two apis @http://localhost:8000/api/#/default via a Swagger-ui
5. The apis are documented and can be accessed using the Ui.
6. /load/{series_id} endpoint accesses the fred service and loads the series data afresh to the respective staging tables as mapped:
    gdp_data_stg = 'GDPC1'
    sentiment_idx_stg = 'UMCSENT'
    unemployment_rate_stg = 'UNRATE'
7. /increment/{series_id} loads only those values that are not present in the tables, using the latest available date as the connection point to access Fred service
8. The postgresql service runs @5432 and is mapped to host 5432. The data is persisted in a local host volume at ./postgresql/data

####Added#####
9. Docker container for Celery and Redis (@6379:6379)
10. The ETL process is put on the celery task queue and asynchronously carried out by the workers

To run
-------
1. Clone the repository, navigate to ./federal_reserve_app
2. docker-compose up (first run may take a while as images are layered)
3. Once containers are up & running(ignore FATAL:  role "root" does not exist, this is a docker bug that is caused because of enforced dependencies in docker-compose, it can be solved by using systemd unit files for services dependency management)
    http://localhost:8000/api/#/default 
4. Click on the default namespace to use the swagger-ui and enter the relevant series_id for load/increment apis
5. Interact with docker postgres container to check the load:
    sudo docker exec -i -t federalreserveapp_postgres_1 /bin/bash
    psql fundingcircle scott
    select * from fred.gdp_data_stg;
    select * from fred.sentiment_idx_stg;
    select * from fred.unmeployment_rate_stg;
6. run ./average_unemployment.sql to get the average unemployment rate from 1980 upto 2015
8. ./postgresql/init_schema.sql is the schema definition script
ENV POSTGRES_DB fundingcircle
ENV POSTGRES_USER scott
ENV POSTGRES_PASSWORD tiger
in Dockerfile creates the database, user with encrypted password before init_schema is executed.
