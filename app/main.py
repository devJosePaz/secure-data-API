from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.transaction_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/", tags=["Root"])
async def root():
    return JSONResponse(
        content={
            "mensagem": "🔐 API de Transações Criptografadas com RSA",
            "sobre": "Este projeto é voltado para práticas de segurança e desenvolvimento com FastAPI.",
            "documentação": "Acesse /docs para explorar os endpoints interativos.",
            "endpoints_úteis": {
                "Listar transações": "/transaction/transactions/",
                "Buscar transação por ID": "/transaction/transaction/{id}",
                "Criar nova transação": "/transaction/transactions/",
            },
            "atenção": "Alterações e exclusões estão bloqueadas por se tratar de dados sensíveis."
        }
    )
