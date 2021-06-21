def price_calculator(product_price, country):
    import pandas as pd
    df=pd.read_excel('/Users/mikel/Documents/Projects/chameleonpricing/chameleonpricing/DB.xlsx')
    find_ppp=df.ppp_spain[df.Country == country.lower()]
    return product_price * find_ppp.item()