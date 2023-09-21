from tests.conftest import BASE_DIR

try:
    from app_cadastral.models.land_plot import LandPlot
except (NameError, ImportError):
    class LandPlot:
        pass

try:
    from app_cadastral.core.config import Settings
except (NameError, ImportError):
    raise AssertionError(
        'Не обнаружен объект настроек приложения `Settings`.'
        'Проверьте и поправьте: он должен быть доступен в модуле `app.core.config`.',
    )


def test_check_migration_file_exist():
    APP_DIR = BASE_DIR / 'app_cadastral'
    app_dirs = [d.name for d in APP_DIR.iterdir()]
    assert 'alembic' in app_dirs, (
        'В корневой директории не обнаружена папка `alembic`.'
    )
    ALEMBIC_DIR = BASE_DIR / 'app_cadastral' / 'alembic'
    version_dir = [d.name for d in ALEMBIC_DIR.iterdir()]
    assert 'versions' in version_dir, (
        'В папке `alembic` не обнаружена папка `versions`'
    )
    VERSIONS_DIR = ALEMBIC_DIR / 'versions'
    files_in_version_dir = [f.name for f in VERSIONS_DIR.iterdir() if f.is_file() and 'init' not in f.name]
    assert len(files_in_version_dir) > 0, (
        'В папке `alembic.versions` не обнаружены файлы миграций'
    )


def test_check_db_url():
    for attr_name, attr_value in Settings.schema()['properties'].items():
        if 'db' in attr_name or 'database' in attr_name:
            assert 'sqlite+aiosqlite' in attr_value['default'], (
                'Укажите значение по умолчанию для подключения базы данных sqlite '
            )
