import requests
import json

from bs4 import BeautifulSoup


def parse_request(request: requests):
    rq = request.text
    soup = BeautifulSoup(rq, 'lxml')
    products = soup.find_all('div', class_='card-column')
    parse_products = []
    main_src = 'https://www.labirint.ru'
    for i in range(10):
        try:
            product = products[i]
        except:
            break
        else:
            author = product.find('div', class_='product-author')
            author_text = " " if not author else author.text
            other_info = product.find('div', class_="product need-watch")
            title = other_info['data-name']
            disc_price = other_info['data-discount-price']
            price = disc_price if disc_price else other_info['data-price']
            ahref = main_src + other_info.find('a')['href']
            parse_products.append((title, author_text, price, ahref))
    return parse_products


def parse_result(products: list):
    text = "Вот что найдено по вашему запросу:\n"
    for i in range(len(products)):
        value = products[i]
        title = value[0]
        author_text = value[1].strip()
        price = value[2]
        ahref = value[3]
        text += f'{i + 1}.\n{title}\nАвтор:{author_text}\nЦена:{price}\n{ahref}\n\n'
    return text


def main():
    pass


if __name__ == '__main__':
    main()
