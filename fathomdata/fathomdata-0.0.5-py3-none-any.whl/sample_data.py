import datetime
import random
import pandas as pd
import re
from urllib.request import urlopen

def get_sample_dataset():

    num_batches = 20
    cycle_time_days = 27

    titer_mu = 4.75
    titer_sigma = 1

    temperature_mu = 37
    temperature_sigma = .75

    titer_sample_data = _get_sample_dataframe("Titer", "g/L", num_batches, cycle_time_days, titer_mu, titer_sigma)
    temperature_sample_data = _get_sample_dataframe("Temperature", "°C", num_batches, cycle_time_days, temperature_mu, temperature_sigma)

    return {
        'Titer': titer_sample_data,
        'Temperature': temperature_sample_data
    }


def  _get_sample_dataframe(parameter_name, units, num_batches, cycle_time_days, mu, sigma):

    start_date = datetime.datetime.now() - datetime.timedelta(days=cycle_time_days * num_batches)

    return pd.DataFrame({parameter_name: [random.gauss(mu, 0.75 * sigma) + random.random() * 1.5 * sigma for x in range(num_batches)],
                         'units': units,
                         'batch_number': [f"2021-{x}" for x in range(num_batches)],
                         'batch_date': [(start_date + datetime.timedelta(days=cycle_time_days * x)).date() for x in range(num_batches)]})


def load_dataset(name, **kws):
    """Load an example dataset from the online repository (requires internet).
    This function provides quick access to a small number of example datasets
    that are useful for documenting or generating reproducible examples
    for bug reports. Requires an internet connection. 
    Use :func:`get_dataset_names` to see a list of available datasets.
    Parameters
    ----------
    name : str
        Name of the dataset (``{name}.csv`` on
        https://github.com/fathom-data/fathom-sample-data).
    kws : keys and values, optional
        Additional keyword arguments are passed to passed through to
        :func:`pandas.read_csv`.
    Returns
    -------
    df : :class:`pandas.DataFrame`
        Tabular data, possibly with some preprocessing applied.
    """

    if name not in get_dataset_names():
        raise ValueError(f"'{name}' is not one of the example datasets.")
    
    full_path = f"https://raw.githubusercontent.com/fathom-data/fathom-sample-data/main/{name}.csv"
    df = pd.read_csv(full_path,  encoding= 'unicode_escape', **kws)
    df = _detect_datetimes(df)

    if df.iloc[-1].isnull().all():
        df = df.iloc[:-1]

    return df

def get_dataset_names():
    """Report available example datasets, useful for reporting issues.
    Requires an internet connection.
    """
    url = "https://github.com/fathom-data/fathom-sample-data"
    with urlopen(url) as response:
        html = response.read()

    pattern = r"/fathom-data/fathom-sample-data/blob/main/(\w*).csv"
    datasets = re.findall(pattern, html.decode())
    return datasets

def _detect_datetimes(df):
    for col in df:
        if any(x in col for x in ["date", "expiry"]):
            try:
                df[col]=pd.to_datetime(df[col])
            except ValueError:
                pass
    return df
