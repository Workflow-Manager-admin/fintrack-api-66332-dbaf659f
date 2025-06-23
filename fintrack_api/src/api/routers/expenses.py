from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


expenses_router = APIRouter()


# PUBLIC_INTERFACE
class ExpenseRecord(BaseModel):
    """Schema for expense records."""
    id: int
    category: str
    amount: float
    date: str
    notes: str = ""


dummy_expense_db = [
    ExpenseRecord(id=1, category="Groceries", amount=70.0, date="2024-06-03"),
    ExpenseRecord(id=2, category="Utilities", amount=120.5, date="2024-06-05"),
]


# PUBLIC_INTERFACE
@expenses_router.get("/", response_model=List[ExpenseRecord])
def list_expenses():
    """List all expense records"""
    return dummy_expense_db


# PUBLIC_INTERFACE
@expenses_router.post("/", response_model=ExpenseRecord)
def add_expense(record: ExpenseRecord):
    """Add a new expense record"""
    dummy_expense_db.append(record)
    return record
