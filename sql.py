from sqlalchemy import create_engine, Column, Integer, String, select, MetaData
from sqlalchemy.engine.result import Result
from sqlalchemy.orm import registry, sessionmaker, declarative_base

# データベース設定
DATABASE = 'test_db'
USER = 'user'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = '3306'

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

Base = declarative_base()


class JourneySchema(Base):
    __tablename__ = "journey"
    id = Column(Integer, primary_key=True)
    journey_id = Column(String(36), unique=True, nullable=False)
    client_id = Column(Integer, nullable=False)


class Journey():
    def __init__(
        self,
        journey_id: str,
        client_id: int,
        number_of_users: int = 5,
    ):
        self.journey_id = journey_id
        self.client_id = client_id
        self.number_of_users = number_of_users


journey_table = JourneySchema.__table__


def get_by_id(journey_id: str) -> Journey | None:
    """Get Journey object by id."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    session = Session()
    statement = select(JourneySchema).where(
        journey_table.c.journey_id == journey_id)
    result: Result = session.execute(statement)
    journey_schema: JourneySchema | None = result.scalars().first()

    session.close()
    if journey_schema is not None:
        return Journey(
            journey_id=journey_schema.journey_id,
            client_id=journey_schema.client_id,
        )
    else:
        return None


def get_by_id_mapper(journey_id: str) -> Journey | None:
    # メタデータとレジストリの設定
    metadata = MetaData()
    mapper_registry = registry(metadata=metadata)

    # クラスとテーブルのマッピング
    mapper_registry.map_imperatively(Journey, journey_table)

    # エンジン、セッションファクトリの設定
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        statement = select(Journey).where(
            journey_table.c.journey_id == journey_id)
        result = session.execute(statement)
        journey = result.scalars().first()
        return journey


def main():
    journey1 = get_by_id('9fd3fa6c-01ca-485a-a73f-edc436bbddeb')
    print(f"get_by_JourneySchema {journey1.__dict__}")

    journey2 = get_by_id_mapper('9fd3fa6c-01ca-485a-a73f-edc436bbddeb')
    print(f"get_by_JourneyMapper {journey2.__dict__}")


if __name__ == "__main__":
    main()
