import random
import json

from faker import Faker

from conf import MODEL

faker = Faker()


def main():
    gen = view()
    m = [next(gen) for _ in range(100)]
    with open("output.txt", 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=4, ensure_ascii=False)


def model():
    return MODEL


def year():
    return random.randint(1940, 2021)


def pages():
    yield random.randint(100, 1000)


def isbn13():
    yield faker.isbn13()


def author():
    yield faker.name()


def title():
    with open('books.txt', 'r', encoding="utf-8") as f:
        for i in f:
            yield i.strip()


def rating():
    yield random.uniform(0, 5)


def price():
    yield random.uniform(0, 1000)


def view(pk=1):
    while True:
        func = {
            "model": model(),
            "pk": pk,
            "fields": {
                "title": next(title()),
                "year": (year()),
                "pages": next(pages()),
                "isbn13": next(isbn13()),
                "rating": next(rating()),
                "price": next(price()),
                "author": [
                    next(author()),
                    next(author())
                ]
            }
        }
        yield func
        pk += 1


if __name__ == '__main__':
    main()
