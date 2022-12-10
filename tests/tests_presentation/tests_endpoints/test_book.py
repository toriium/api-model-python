import pytest
import httpx

from src.domain.book import Book
from src.domain.user import User


def test_get_route_book_with_valid_book_return_book(host: str, valid_token, created_book: Book):
    headers = {"Authorization": valid_token}
    response = httpx.get(url=f'{host}/book/{created_book.id}', headers=headers)

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


def test_post_route_book_with_valid_data_return_book(host: str, valid_token):
    headers = {"Authorization": valid_token}
    json = {
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil",
        "author": "Friedrich Wilhelm Nietzsche",
        "publisher": "Penguin Books",
        "release_date": "1886-01-01",
        "pages": 240,
        "description": "this is a description"
    }
    response = httpx.post(url=f'{host}/book', headers=headers, json=json)

    expected_response = {
        "isbn": "978-0140449235",
        "name": "Beyond Good and Evil",
        "author": "Friedrich Wilhelm Nietzsche",
        "publisher": "Penguin Books",
        "release_date": "1886-01-01",
        "pages": 240,
        "description": "this is a description"
    }

    assert response.status_code == 201
    assert response.json() == expected_response
