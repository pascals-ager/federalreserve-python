import os
import sys
import xml.etree.ElementTree as ET
import urllib.request as url_request
import urllib.parse as url_parse
import urllib.error as url_error
import pandas as pd
urlopen = url_request.urlopen
quote_plus = url_parse.quote_plus
urlencode = url_parse.urlencode
HTTPError = url_error.HTTPError

'''
Access DATABASE_URI and API_KEY from settings file. How do i did?
'''
###########


###########



class ExtractAndLoad(object):
    earliest_realtime_start = '1776-07-04'
    latest_realtime_end = '9999-12-31'
    nan_char = '.'
    max_results_per_request = 1000
    root_url = 'https://api.stlouisfed.org/fred'

    def __init__(self,
                 api_key=None,
                 engine=None):
        self.api_key = api_key
        self.engine = engine


    def __fetch_data(self, url):
        """
        helper function for fetching data given a request URL
        """
        url += '&api_key=' + self.api_key
        try:
            response = urlopen(url)
            root = ET.fromstring(response.read())
        except HTTPError as exc:
            root = ET.fromstring(exc.read())
            raise ValueError(root.get('message'))
        return root

    def _parse(self, date_str, format='%Y-%m-%d'):
        """
        helper function for parsing FRED date string into datetime
        """
        rv = pd.to_datetime(date_str, format=format)
        if hasattr(rv, 'to_pydatetime'):
            rv = rv.to_pydatetime()
        return rv

    def get_series(self, series_id, observation_start=None, observation_end=None, **kwargs):
        """
        Get data for a Fred series id. This fetches the latest known data, and is equivalent to get_series_latest_release()
        Parameters
        ----------
        series_id : str
            Fred series id such as 'CPIAUCSL'
        observation_start : datetime or datetime-like str such as '7/1/2014', optional
            earliest observation date
        observation_end : datetime or datetime-like str such as '7/1/2014', optional
            latest observation date
        kwargs : additional parameters
            Any additional parameters supported by FRED. You can see https://api.stlouisfed.org/docs/fred/series_observations.html for the full list
        Returns
        -------
        data : Series
            a Series where each index is the observation date and the value is the data for the Fred series
        """
        url = "%s/series/observations?series_id=%s" % (self.root_url, series_id)
        if observation_start is not None:
            observation_start = pd.to_datetime(observation_start,
                                               errors='raise')
            url += '&observation_start=' + observation_start.strftime('%Y-%m-%d')
        if observation_end is not None:
            observation_end = pd.to_datetime(observation_end, errors='raise')
            url += '&observation_end=' + observation_end.strftime('%Y-%m-%d')
        if kwargs.keys():
            url += '&' + urlencode(kwargs)
        root = self.__fetch_data(url)
        if root is None:
            raise ValueError('No data exists for series id: ' + series_id)
        data = {}
        for child in root.getchildren():
            val = child.get('value')
            if val == self.nan_char:
                val = float('NaN')
            else:
                val = float(val)
            data[self._parse(child.get('date'))] = val

        return data



    def get_connection_point(self, table, schema):
        statement = "select index, period from "+ schema+"."+table+" order by period desc limit 1"
        try:
            connection_point = pd.read_sql_query(statement, self.engine)
        except Exception as e:
            raise
        if not connection_point.empty:  
            load_date =  connectionPoint.iloc[0][1].to_pydatetime()
            load_pos = connectionPoint.iloc[0][0]
            return load_pos, load_date
        else:
            return 1, None


    def load(self, data, pos, load_type, table, schema):
        df = pd.DataFrame(list(data.items()),columns=['period','data'])
        df['period'] = pd.to_datetime(df['period'])
        if pos > 1:
            df = df[1:]
        df.index += pos        
        try:
            df.to_sql(table, self.engine, if_exists=load_type, schema=schema, index=True)            
        except:            
            raise

        return