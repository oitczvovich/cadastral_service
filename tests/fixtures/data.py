import pytest


@pytest.fixture
def landplot(mixer):
    return mixer.blend(
        'app_cadastral.models.land_plot.LandPlot',
        cadastral_number='10:00:0100000:00',
        lat='29.123456',
        long='-54.123456',
    )


@pytest.fixture
def landplot_free(mixer):
    return mixer.blend(
        'app_cadastral.models.land_plot.LandPlot',
        cadastral_number='20:20:0000000:00',
        lat='23.123456',
        long='-23.123456',
        answer_server=True
    )


@pytest.fixture
def landplot_not_free(mixer):
    return mixer.blend(
        'app_cadastral.models.land_plot.LandPlot',
        cadastral_number='22:32:2000000:07',
        lat='55.654321',
        long='-123.654321',
        answer_server=False
    )