from app import create_celery_app

celery = create_celery_app()

@celery.task()
def init_etl_process(api_key, engine, series_id, table, schema, pos, load_type):
    from extensions.extract import ExtractAndLoad
    from sqlalchemy import create_engine
    etl = ExtractAndLoad(api_key, engine)
    start_date = None

    if load_type == 'append':
        pos, start_date = etl.get_connection_point(table, schema)
    
    data = etl.get_series(series_id, start_date)
    etl.load(data, pos, load_type, table, schema)
