import pytest


def test_get_landplot_result(superuser_client, landplot_free, landplot_not_free):
    response = superuser_client.get('/api/result/1')
    print('response', response.json())
    assert (
        response.status_code == 200
    ), "При GET-запросе к эндпоинту `/api/result/obj_id' должен возвращаться статус-код 200."
    assert isinstance(
        response.json(), dict
    ), "При GET-запросе к эндпоинту `/api/result/obj_id' должен возвращаться объект типа `list`."
    data = response.json()
    keys = sorted(
        {
            "cadastral_number",
            "lat",
            "long",
            "answer_server",
            "id",
        }
    )
    assert (
        sorted(list(data.keys())) == keys
    ), f"При GET-запросе к эндпоинту `/api/result/obj_id' в ответе API должны быть ключи `{keys}`."
    assert response.json() == {
            'cadastral_number': '20:20:0000000:00',
            'lat': '23.123456',
            'long': '-23.123456',
            'answer_server': True,
            "id": 1,
        }, "При GET-запросе к эндпоинту `/api/result/obj_id` тело ответа API отличается от ожидаемого."