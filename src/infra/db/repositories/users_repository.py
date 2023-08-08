from src.infra.db.settings.connetion import DBConnetionHandler
from src.infra.db.entities.users import Users as UsersEntity


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnetionHandler() as database:
            try:
                new_registy = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                database.session.add(new_registy)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
