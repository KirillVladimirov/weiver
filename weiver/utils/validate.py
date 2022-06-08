from dataclasses import dataclass
import datetime


@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None


def validate_user_on_server(user):
    pass


def check_username(user):
    pass


def check_birthday(user):
    pass


def validate_user(user: User):
    validate_user_on_server(user)
    check_username(user)
    check_birthday(user)


if __name__ == "__main__":
    user_id = 123
    validate_user(user_id)
