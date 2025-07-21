from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models
from app.database import get_db

router = APIRouter(prefix="/transaction", tags=["transactions"])

@router.get("/transactions/", response_model=list[schemas.TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions

@router.get("/transaction/{transaction_id}", response_model=schemas.TransactionResponse)
def list_transaction_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="error, transaction not found")
    return transaction


@router.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    if transaction.value <= 0:
        raise HTTPException(status_code=400, detail="error the value must be greater than or equal to 0")

    new_transaction = models.Transaction(
            user_document=transaction.user_document,
            credit_card_token=transaction.credit_card_token,
            value=transaction.value
        )

    try:
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return  new_transaction

    except Exception as e:
        print("error", e)
        return{"error": str(e)}


@router.put("/transaction/{transacton_id}")
def update_transaction():
    raise HTTPException(status_code=403, detail="no fields can be changed, all data is sensitive")
    

@router.delete("/transaction/{transaction_id}")
def delete_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    pass

    
    
