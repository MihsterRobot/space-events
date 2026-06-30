import httpx

from app.core.config import settings

BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed'


def fetch_asteroids(start_date: str, end_date: str) -> dict:
    '''Fetch asteroid close approach data from NASA NeoWs.

    Args:
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.

    Returns:
        Raw JSON response from the NeoWs API.
    '''
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': settings.nasa_api_key,
    }

    with httpx.Client() as client:
        response = client.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
