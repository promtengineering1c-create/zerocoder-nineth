from unittest.mock import Mock
from main import get_cats

def test_get_cats_status_code_200(mocker):
    url = "https://cdn2.thecatapi.com/images/3kn.jpg"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "id": "3kn",
        "url": url,
        "width": 500,
        "height": 377
    }]
    
    mocker.patch('main.requests.get', return_value=mock_response)


    data = get_cats("бенгальская")

    assert data[0]['url'] == "https://cdn2.thecatapi.com/images/3kn.jpg"

def test_get_cats_status_code_500(mocker):
    url = "https://cdn2.thecatapi.com/images/3kn.jpg"
    mock_response = Mock()
    mock_response.status_code = 500
    
    mocker.patch('main.requests.get', return_value=mock_response)


    data = get_cats("бенгальская")

    assert data == None     