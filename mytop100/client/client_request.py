import requests

endpoint_get = "http://127.0.0.1:8000/api/movies/"
endpoint_get_generic = "http://127.0.0.1:8000/api/generic/movies/"
endpoint_get_one =  "http://127.0.0.1:8000/api/movie/5"
endpoint_get_one_generic =  "http://127.0.0.1:8000/api/generic/movie/999"



endpoint_post = "http://127.0.0.1:8000/api/create-movie/"
movie_data = {
    "title": "Meu Filme",
    "director": "Nome do Diretor",
    "description": "Uma descrição interessante do filme"
}


try:
    response = requests.get(endpoint_get_one_generic)
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.json()}")
except Exception as e:
    print(f"An error occurred: {e}")
