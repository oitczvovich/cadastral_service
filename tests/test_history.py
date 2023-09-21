import pytest


def test_get_all_landplot(superuser_client, landplot_free, landplot_not_free):
    response = superuser_client.get("/api/history/")
    assert response.status_code == 200, (
        'Список запросов к земельным участкам должен быть доступен.'
    )
    data = response.json()
    print(data)
    assert data == {
        'results':
            [
                {
                    'lat': '23.123456',
                    'id': 1,
                    'long': '-23.123456',
                    'answer_server': True,
                    'cadastral_number': '20:20:0000000:00'
                },
                {
                    'lat': '55.654321',
                    'id': 2,
                    'long': '-123.654321',
                    'answer_server': False,
                    'cadastral_number': '22:32:2000000:07'
                }
            ],
        'total_count': 2,
        'page': 1,
        'size': 5,
        'next_url': None,
        'prev_url': None
    }
