import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Script format input price from 3245.000000 to 3 245')
    parser.add_argument('price', help='Price to format')
    return parser.parse_args()


def format_price(price):
    if price and ',' in price:
        price = price.replace(',', '.')
    try:
        if float(price) >= 0.0:
            return '{:,.0f}'.format(float(price)).replace(',', ' ')
        else:
            return 'Negative price!'
    except ValueError:
        return 'Incorrect value!'
    except TypeError:
        return 'Incorrect type!'


def print_price(raw_price):
    print('Formatted price: {}'.format(format_price(raw_price)))


if __name__ == '__main__':
    args = get_arguments()
    print_price(args.price)
