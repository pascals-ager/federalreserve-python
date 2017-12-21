CREATE SCHEMA IF NOT EXISTS fred AUTHORIZATION scott;


CREATE TABLE IF NOT EXISTS fred.gdp_data_stg(
index serial primary key,
period timestamp not null,
data double precision
);

CREATE TABLE IF NOT EXISTS fred.sentiment_idx_stg(
index serial primary key,
period timestamp not null,
data double precision
);

CREATE TABLE IF NOT EXISTS fred.unemployment_rate_stg(
index serial primary key,
period timestamp not null,
data double precision
);