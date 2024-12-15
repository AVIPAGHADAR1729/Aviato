from sqlalchemy import Column, Integer, String, ForeignKey, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

meta = MetaData()
Base = declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=True)
    mobile = Column(String, unique=True, nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=True)
    date_of_birth = Column(String, nullable=True)
    hashtag = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint("email", name="unique_email"),
        UniqueConstraint("mobile", name="unique_mobile"),
    )


DATABASE_URL = "sqlite:///./avi_test.db"
engine = create_engine(DATABASE_URL)
db_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
