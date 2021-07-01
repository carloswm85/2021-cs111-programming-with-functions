import csv
from datetime import datetime


def main():
    products_file = "E:/GitHub/2021-cs111-programming-with-functions/w10-handling-exceptions/prove-handling-exceptions/products.csv"
    products = read_products(products_file)

    print('>>> Inkom Emporium <<<')

    # print('Products:')
    # for number, product in products.items(): # This loop is going to print a dictionary
    # 	print(number, product)

    requests_file = "E:/GitHub/2021-cs111-programming-with-functions/w10-handling-exceptions/prove-handling-exceptions/request.csv"
    process_request(requests_file, products_file)


def read_products(file):
    """
            Reads file into a dictionary.
    """
    print()
    products = {}

    try:
        with open(file, "rt") as infile:
            reader = csv.reader(infile)
            next(reader)
            for line in reader:
                product_number = line[0]
                product_name = line[1]
                product_price = line[2]
                products[product_number] = [product_name, product_price]
    except KeyError as key_err:
        print(
            f"Error: line {reader.line_num} of {file.name} is formatted incorrectly.")
        # If we write code that attempts to find a key in a dictionary and that key doesn't exist in the dictionary.
        print(key_err)
    except FileNotFoundError as file_not_found_err:
        print(f"Error: cannot open {file} because it doesn't exist.")
        print(file_not_found_err)
        exit()
    except PermissionError as perm_err:
        print(
            f"Error: cannot read from {file} because you don't have permission.")
        print(perm_err)
        exit()
    return products


def process_request(requests_file, products_file):
    product_dic = read_products(products_file)
    current_date = datetime.now()
    with open(requests_file, "rt") as infile:
        reader = csv.reader(infile)
        next(reader)
        print('Requested items:')

        number_items = 0
        total = 0
        sub_total = 0
        sales_tax_rate = 0.06

        for line in reader:
            product_number = line[0]
            product_quantity = line[1]
            quantity = int(product_quantity)
            if product_number in product_dic.keys():
                product = product_dic[product_number]
                name = product[0]
                price = float(product[1])
                print(f'{name}: {product_quantity} @ {price}')

                sub_total = sub_total + quantity * price
            number_items = number_items + quantity

        print(f'\nNumber of Items: {number_items}')
        print(f'Subtotal: {sub_total}')
        sales_tax = sales_tax_rate * sub_total
        print(f'Sales Tax: {sales_tax:.2f}')
        total = sub_total + sales_tax
        print(f'Total: {total:.2f}')

        print('\nThank you for shopping at the Inkom Emporium')
        # Formatting date and time https://stackoverflow.com/a/63061189/7389293
        print(f'{current_date:%A %d, %Y, %I:%M %p}')


if __name__ == "__main__":
    main()
