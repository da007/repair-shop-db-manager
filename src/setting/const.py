import os
from dotenv import load_dotenv

# Загружаем секреты из .env файла
load_dotenv()

AVAILABLE_TABLES = {
    "Administrator": ["clients", "devices", "device_types", "employees", "order_spare_parts", "order_services", "statuses", "spare_parts", "services", "orders"],
    "Operator": ["clients", "order_spare_parts", "order_services", "statuses", "orders"],
    "Master": ["devices", "statuses", "spare_parts", "services", "orders"],
    "Storage": ["order_spare_parts", "spare_parts"],
    "Guest": [],
}

AVAILABLE_ROUTES = {
    "Administrator": ["/", "/setting", "/loggin", "/tables/clients", "/tables/devices", "/tables/device_types", "/tables/employees", "/tables/order_spare_parts", "/tables/order_services", "/tables/statuses", "/tables/spare_parts", "/tables/services", "/tables/orders"],
    "Operator": ["/", "/setting", "/loggin", "/tables/clients", "/tables/order_spare_parts", "/tables/order_services", "/tables/statuses", "/tables/orders"],
    "Master": ["/", "/setting", "/loggin", "/tables/devices", "/tables/statuses", "/tables/spare_parts", "/tables/services", "/tables/orders"],
    "Storage": ["/", "/setting", "/loggin", "/tables/order_spare_parts", "/tables/spare_parts"],
    "Guest": ["/", "/setting", "/loggin"],
}

# Ключ теперь берется из окружения, а не из кода!
CRYPT_KEY = os.getenv("CRYPT_KEY", "-KlO432jG5Vm5G24X3gb-2oRX2jsVODPMjW1fu8idzw=")
SETTING_FILE = "setting.crypt"

SETTING_DEFAULT = {
    "app": {
        "theme_mode": "Темная стандартная",
        "theme_color": "Индиго"
    },
    "db": {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "User"), 
        "password": os.getenv("DB_PASSWORD", "1pq0"), 
        "database": os.getenv("DB_NAME", "repair_shop")
    }
}
