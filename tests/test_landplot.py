import pytest


@pytest.mark.parametrize(
    "invalid_cadastral_num",
    [
        "",
        "2345691",
        "lovechimichangasbutnunchakuisbetternunchakis4life",
        "23:54:CFE345:55:55",
        None,
    ],

)
def test_create_invalid_cadastral_num(superuser_client, invalid_cadastral_num):
    response = superuser_client.post(
        '/api/query/',
        json={
            "cadastral_number": invalid_cadastral_num,
            "lat": "23.123456",
            "long": '-23.123456',
        },
    )
    assert (
        response.status_code == 422
    ), "Кадастровый номер в запросе должен соответсвовать формату '00:00:0000000:00'."


@pytest.mark.parametrize(
    "invalid_lat_num",
    [
        "",
        "3459kg954vmkltihtht"
        "-23.45691",
        "145.123456",
        None,
    ],

)
def test_create_invalid_lat_num(superuser_client, invalid_lat_num):
    response = superuser_client.post(
        '/api/query/',
        json={
            "cadastral_number": "00:00:0000000:00",
            "lat": invalid_lat_num,
            "long": '-23.123456',
        },
    )
    assert (
        response.status_code == 422
    ), ("Создание запроса с пустой широтой или не соответсвующую формату от -90 до 90."
        "c 6 знаками после запятой должно быть запрещено."
        )


@pytest.mark.parametrize(
    "invalid_long_num",
    [
        "",
        "3459kg954vmkltihtht"
        "233.45691",
        None,
    ],
)
def test_create_invalid_long_num(superuser_client, invalid_long_num):
    response = superuser_client.post(
        '/api/query/',
        json={
            "cadastral_number": "00:00:0000000:00",
            "lat": '23.123456',
            "long": invalid_long_num,
        },
    )
    assert (
        response.status_code == 422
    ), "Создание запроса с пустой долгота или длиннее 11 символов должно быть запрещено."


@pytest.mark.parametrize('json', [
    {"cadastral_number": "00:00:0000000:00"},
    {"lat": "23.123456"},
    {"long": "-23.123456"},
    {"id": 3000},
    ]
)
def test_create_autofield(superuser_client, json):
    response = superuser_client.post(
        '/api/query/',
        json=json
    )
    assert (
        response.status_code == 422
    ), 'При попытке передать в запросе значения для автозаполняемых полей должна возвращаться ошибка 422.'


def test_create_landplot(superuser_client):
    response = superuser_client.post(
        '/api/query/',
        json={
            "cadastral_number": "00:00:0000000:00",
            "lat": '23.123456',
            "long": '-23.123456',
        },
    )
    assert (
        response.status_code == 200
    ), "При создании участка должен возвращаться статус-код 200."
    data = response.json()
    keys = sorted(
        [
            "cadastral_number",
            "lat",
            "long",
            "id",
        ]
    )
    assert (
        sorted(list(data.keys())) == keys
    ), f"При создании проекта в ответе API должны быть ключи `{keys}`."
    assert data == {
        "cadastral_number": "00:00:0000000:00",
        "lat": '23.123456',
        "long": '-23.123456',
        "id": 1,
    }, "При создании проекта тело ответа API отличается от ожидаемого."


@pytest.mark.parametrize(
    "json",
    [
        {
            "cadastral_number": "00:00:0000000:00",
            "lat": '23.1234',
            "long": '-23.3456',
        },
        {
            "cadastral_number": "00:00:0000000:00",
            "long": '-23.345644',
        },
        {
            "cadastral_number": "00:00:0000000:00",
            "lat": '23.123434',
        },
        {
            "lat": '23.123425',
            "long": '-23.345625',
        },
        {
            "cadastral_number": "00:00:0000000:00",
        },
        {},
    ],
)
def test_create_landplot_validation_error(json, superuser_client):
    response = superuser_client.post('/api/query/', json=json)
    assert response.status_code == 422, (
        "При некорректном создании участка должен возвращаться статус-код 422."
    )
    data = response.json()
    assert (
        "detail" in data.keys()
    ), "При некорректном создании участка в ответе API должен быть ключ `detail`."
