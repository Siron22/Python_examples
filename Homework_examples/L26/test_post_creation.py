import random

import pytest
import requests


GO_REST_ACCESS_TOKEN = "0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"
header = {"Accept": "application/json",
          "Content-Type": "application/json",
          "Authorization": f"Bearer {GO_REST_ACCESS_TOKEN}"
          }
url_users = 'https://gorest.co.in/public/v2/users'


@pytest.fixture()
def new_user():
    user_data = {'email': f'name.surname{random.randint(10000, 1000000000000)}@test.com',
                 'gender': 'female',
                 'name': 'Anna Ivanova',
                 'status': 'active'}

    response = requests.post(url_users, json=user_data, headers=header)
    print(response.status_code)
    print(response.text)
    if response.status_code != 201:
        raise Exception("Can't create user!")
    id_ = response.json()['id']
    yield id_
    requests.delete(f"{url_users}/{id_}", headers=header)


def test_post_creation(new_user):
    id_ = new_user
    url_posts = f"https://gorest.co.in/public/v2/users/{id_}/posts"
    post_data = {'title': 'WQQQ', 'body': 'fvdddfvd'}
    post_response = requests.post(url_posts, headers=header, json=post_data)
    assert post_response.status_code == 201
    assert post_response.json()['user_id'] == id_
    assert post_response.json()['title'] == post_data['title']
    assert post_response.json()['body'] == post_data['body']
