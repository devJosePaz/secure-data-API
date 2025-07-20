from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
import schemas, models
from databse import get_db

router = APIRouter(prefix="/transaction", tags=["transactions"])

@router.get("/transactions/", response_model=list[schemas.TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions


@router.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    if transaction.value <= 0:
        raise HTTPException(status_code=400, detail="error the value must be greater than or equal to 0")

    new_transaction = Transaction(
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
        raise HTTPException(status_code=500, detail="error creating transaction")
