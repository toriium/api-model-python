import json

import httpx
from faker import Faker

from src.domain.book import Book
from src.infrastructure.db_raw.db_utils import DBUtils


def test_get_route_book_with_valid_book_return_book(host: str, valid_headers: dict, created_book: Book):
    url = f'{host}/book/{created_book.id}'
    headers = valid_headers
    response = httpx.get(url=url, headers=headers)

    expected_response = json.loads(created_book.json())

    assert response.status_code == 200
    assert response.json() == expected_response


def test_post_route_book_with_valid_data_return_book(host: str, valid_headers: dict):
    url = f'{host}/book'
    headers = valid_headers

    fake = Faker()
    json_data = {
        "isbn": fake.isbn13(),
        "name": fake.name(),
        "author": fake.name(),
        "publisher": fake.company(),
        "release_date": fake.date(),
        "pages": fake.random_int(),
        "description": fake.text(),
    }
    response = httpx.post(url=url, headers=headers, json=json_data)

    expected_response = json_data

    DBUtils.execute(query=f"delete from tbl_books where isbn = '{json_data['isbn']}' ")

    assert response.status_code == 201
    assert response.json() == expected_response


def test_put_route_book_with_valid_data_return_200(host: str, valid_headers: dict, created_book: Book):
    url = f'{host}/book'
    headers = valid_headers

    fake = Faker()
    json_data = {
        "id": created_book.id,
        "isbn": fake.isbn13(),
        "name": fake.name(),
        "author": fake.name(),
        "publisher": fake.company(),
        "release_date": fake.date(),
        "pages": fake.random_int(),
        "description": fake.text(),
    }
    response = httpx.put(url=url, headers=headers, json=json_data)

    expected_response = json_data

    assert response.status_code == 200
    assert response.json() == expected_response


def test_delete_route_book_with_valid_book_id_return_200(host: str, valid_headers: dict, created_book: Book):
    url = f'{host}/book'
    headers = valid_headers
    params = {"book_id": created_book.id}

    response = httpx.delete(url=url, headers=headers, params=params)

    expected_response = {"message": "Book deleted"}

    assert response.status_code == 200
    assert response.json() == expected_response
