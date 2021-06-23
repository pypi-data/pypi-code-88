import holidays
from datetime import date, datetime, timedelta
import pyodbc
from typing import Tuple, Union
from typing_extensions import Literal       # Literal is added in Python 3.8 in 'typing' library ~ https://stackoverflow.com/a/67193166/15657263

# Custom imports
from config.config_credentials_reader import ConfigCredentialsReader


def get_samedaycustomers(retry=0):
    temp_sameday = []
    conn = get_conn()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT [customer_id] FROM [BlueCrest].[dbo].[SameDayClients]""")
            [temp_sameday.append(x.customer_id) for x in cursor.fetchall()]
            cursor.close()
            close_conn(conn)
            return temp_sameday
        except Exception as ex:
            print("Exception gettings samedayclients: " + str(ex))
            close_conn(conn)
            if retry < 3:
                return get_samedaycustomers(retry=retry+1)
            return temp_sameday

def close_conn(conn):
    try:
        conn.close()
    except Exception as ex:
        print(ex)

def get_conn(retry = 0):
    """
    Returns the BlueCrest pyodbc connector.

    Returns:
    ----
    - If connection can be successfully made: returns pyodbc connector
    - Else: returns False
    """
    # database connection
    try:
        connection_string = get_bluecrest_connection_string()
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as ex:
        print("No Connection: " + str(ex))
        if retry < 3:
            return get_conn(retry=retry+1)
        return False

def get_bluecrest_connection_string() -> str:
    """ Reads BlueCrest 10.10.10.30 connectionstring from credentials """
    config_reader = ConfigCredentialsReader()
    connection_object = config_reader.config_data.bluecrest_10_10_10_30_connection
    return connection_object.to_sql_connection_string()

def generate_dates(inputdate: Union[str,datetime,None] = None, customer_id: Union[int,str,None]=None, retry: int = 0) -> Union[Tuple[datetime,datetime], Tuple[Literal[False],Literal[False]]]:
    """
    Returns start and end of facturation date as datetimes or False, False if failed

    params:
    ----
    inputdate: 
        Represents the invoice date.\n
        If {datetime}: uses param as invoice date\n
        If {str}: first parses param to invoice date using one of following datetime formats "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"\n
        If {None}: uses current timestamp as invoice date\n
    customer_id:
        Represents the DBFact customerID (AKA ClientNumber)

    Returns:
    ----
    * If succeeds: returns (start_invoice_datetime, end_invoice_dateime)
    * If fails: return tuple (False, False)
    """
    # database connection
    conn = get_conn()
    if conn:
        # string to datetime
        if not isinstance(inputdate,datetime):
            if inputdate:
                try:
                    inputdate = datetime.strptime(inputdate,"%Y-%m-%d %H:%M:%S.%f")
                except ValueError:
                    pass
                except TypeError:
                    pass
                try:
                    inputdate = datetime.strptime(inputdate,"%Y-%m-%d %H:%M:%S")
                except ValueError:
                    pass
                except TypeError:
                    pass
                try:
                    inputdate = datetime.strptime(inputdate,"%Y-%m-%d %H:%M")
                except ValueError:
                    pass
                except TypeError:
                    pass
                try:
                    inputdate = datetime.strptime(inputdate,"%Y-%m-%d")
                except ValueError:
                    pass
                except TypeError:
                    pass
                if not isinstance(inputdate,datetime):
                    inputdate = datetime.now()
            else:
                inputdate = datetime.now()
        
        if not isinstance(customer_id,int):
            try:
                customer_id = int(customer_id)
            except Exception as ex:
                customer_id = 0
        sameday = (customer_id in get_samedaycustomers())

        try:
            holidays_be = holidays.Belgium(years= inputdate.year)
            cutoff = datetime.strptime('00:00:00.000','%H:%M:%S.%f')
            if not sameday:
                cursor = conn.cursor()
                cursor.execute("""SELECT * FROM ProductionDay""")
                cutoff = datetime.strptime(cursor.fetchone()[0],'%H:%M:%S.%f')
                cursor.close()
            
            fact_date = datetime.combine(inputdate.date(), cutoff.time())
            # 1 time calculate time before or after cutoff (after do nothing, before substract one)
            if inputdate.time() < cutoff.time():
                fact_date -= timedelta(days=1)
            # 2 go back until actual working day (no holiday and no weekend)
            while (fact_date.weekday() > 4 or any(fact_date.date() == h for h in holidays_be)):
                fact_date -= timedelta(days=1)
            end = datetime.combine(inputdate.date(), (cutoff - timedelta(seconds=1)).time())
            # 3 time calculate time before or after cutoff (after add one, before do nothing)
            if not inputdate.time() < cutoff.time() and not sameday:
                end += timedelta(days=1)
            # 4 go forward until actual working day (no holiday and no weekend)
            while (end.weekday() > 4 or any(end.date() == h for h in holidays_be)):
                end += timedelta(days=1)
            close_conn(conn)
            return fact_date, end
        except Exception as ex:
                print(ex)
                close_conn(conn)
                if retry < 3:
                    return generate_dates(inputdate=inputdate,retry=retry+1)
                return False, False
    else:
        return False, False

        

if __name__ == "__main__":
    input_date = datetime(2021, 5, 21, hour=14)
    dates = generate_dates(inputdate=input_date, customer_id=7255)
    print(f"Invoice date start and end for date '{input_date}'")
    print("-> Start invoice datetime:", dates[0])
    print("-> End invoice datetime:", dates[1])