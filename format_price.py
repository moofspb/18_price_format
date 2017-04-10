import argparse


def get_arguments():
    pass


def format_price(price):
    if price and ',' in price:
        price = price.replace(',', '.')
    try:
        if float(price) >= 0.0:
            return '{:,.0f}'.format(float(price)).replace(',', ' ')
        else:
            return '0'
    except ValueError:
        return '0'
    except TypeError:
        return '0'


if __name__ == '__main__':
    pass
