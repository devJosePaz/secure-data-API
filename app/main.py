from app.database import engine, Base
from app.models.models import Transaction

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("tabela criada com sucesso")
