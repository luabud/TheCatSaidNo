import pytest

@pytest.mark.parametrize("input, response_code", [("/", 200), ("/anythingelse", 404)])
def test_home(input, response_code, create_client):
    response = create_client.get(input)
    assert b'error' not in response.data
    assert response.status_code == response_code


