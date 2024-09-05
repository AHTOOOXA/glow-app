import hashlib
import hmac
import logging
import time
from urllib.parse import parse_qsl, unquote

from aiogram import Bot

from app.config import db_config, tgbot_config
from app.infrastructure.database.repo.requests import RequestsRepo
from app.infrastructure.database.setup import (create_engine,
                                               create_session_pool)

engine = create_engine(db_config)
session_pool = create_session_pool(engine)
bot = Bot(tgbot_config.token)


async def get_repo():
    async with session_pool() as session:
        yield RequestsRepo(session)


def parse_init_data(init_data: str = None) -> dict:
    if not init_data:
        return {}

    parsed_data = dict(parse_qsl(init_data))
    return parsed_data


def validate_telegram_data(init_data: str) -> bool:
    parsed_data = parse_init_data(init_data)

    received_hash = parsed_data.pop("hash")
    # Constructing the data-check-string
    fields = sorted([(key, unquote(value)) for key, value in parsed_data.items() if key != "hash"])
    # Constructing the data-check-string using the sorted order
    data_check_string = "\n".join(f"{k}={v}" for k, v in fields)

    print(data_check_string)
    # Computing the secret key
    secret_key = hmac.new(b"WebAppData", tgbot_config.token.encode(), hashlib.sha256).digest()

    # Comparing received hash with computed hash
    computed_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    if computed_hash != received_hash:
        return False

    return True
