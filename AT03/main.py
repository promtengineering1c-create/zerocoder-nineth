import requests

def get_cats(breed: str):

    url = f"https://api.thecatapi.com/v1/images/search"
    params = {
    'limit': 1,          # Количество изображений (от 1 до 100, по умолчанию 1)
    'size': 'small',       # Размер изображений: 'full', 'med', 'small'
    'mime_types': 'jpg', # Формат: 'jpg,png', 'gif'
    'breed_ids': f'{breed}'  # ID конкретной породы (например, бенгальская)
}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

print(get_cats("бенгальская"))