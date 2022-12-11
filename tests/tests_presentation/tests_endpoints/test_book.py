import pytest
import httpx

from src.domain.book import Book
from src.infrastructure.db_raw.db_utils import DBUtils


def test_get_route_book_with_valid_book_return_book(host: str, valid_headers: dict, created_book: Book):
    url = f'{host}/book/{created_book.id}'
    headers = valid_headers
    response = httpx.get(url=url, headers=headers)

    expected_response = {
        "id": 1,
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil",
        "author": "Friedrich Wilhelm Nietzsche",
        "publisher": "Penguin Books",
        "release_date": "1886-01-01",
        "pages": 240,
        "description": "this is a description"
    }

    assert response.status_code == 200
    assert response.json() == expected_response


def test_post_route_book_with_valid_data_return_book(host: str, valid_headers: dict):
    url = f'{host}/book'
    headers = valid_headers
    json = {
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil",
        "author": "Friedrich Wilhelm Nietzsche",
        "publisher": "Penguin Books",
        "release_date": "1886-01-01",
        "pages": 240,
        "description": "this is a description"
    }
    response = httpx.post(url=url, headers=headers, json=json)

    expected_response = {
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil",
        "author": "Friedrich Wilhelm Nietzsche",
        "publisher": "Penguin Books",
        "release_date": "1886-01-01",
        "pages": 240,
        "description": "this is a description"
    }

    DBUtils.execute(query="delete from tbl_books where isbn = '978-0140449235' ")

    assert response.status_code == 201
    assert response.json() == expected_response


def test_put_route_book_with_valid_data_return_200(host: str, valid_headers: dict, created_book: Book):
    url = f'{host}/book'
    headers = valid_headers
    json = {
        "id": created_book.id,
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil 2",
        "author": "Friedrich Wilhelm Nietzsche 2",
        "publisher": "Penguin Books 2",
        "release_date": "1886-01-02",
        "pages": 242,
        "description": "this is a description 2"

    }
    response = httpx.put(url=url, headers=headers, json=json)

    expected_response = {
        "id": created_book.id,
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil 2",
        "author": "Friedrich Wilhelm Nietzsche 2",
        "publisher": "Penguin Books 2",
        "release_date": "1886-01-02",
        "pages": 242,
        "description": "this is a description 2"
    }

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
