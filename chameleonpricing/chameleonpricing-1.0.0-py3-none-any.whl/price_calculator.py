def price_calculator(product_price, country):
    import pandas as pd
    df=pd.read_excel('/Users/mikel/Documents/Projects/chameleonpricing/chameleonpricing/DB.xlsx')
    find_ppp=df.ppp_spain[df.Country == country.lower()]
    return product_price * find_ppp.item()

def price_prediction(product_price, Country):
    import pandas as pd
    df=pd.read_excel('/Users/mikel/Documents/Projects/chameleonpricing/chameleonpricing/forecast.xlsx')
    df[Country]=df[Country] * product_price
    df1=df[['Year', Country]].tail(3)
    return df1