def calculate_tax(price):
    '''
    calculate the tax of a product
    '''
    taxed_price = price * 1.19
    return round(taxed_price, 2)