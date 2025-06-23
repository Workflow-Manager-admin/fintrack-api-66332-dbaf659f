from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


income_router = APIRouter()


# PUBLIC_INTERFACE
class IncomeRecord(BaseModel):
    """Schema for income records."""
    id: int
    source: str
    amount: float
    date: str
    notes: str = ""


dummy_income_db = [
    IncomeRecord(id=1, source="Salary", amount=3000.0, date="2024-06-01"),
    IncomeRecord(id=2, source="Freelance", amount=450.0, date="2024-06-10"),
]


# PUBLIC_INTERFACE
@income_router.get("/", response_model=List[IncomeRecord])
def list_income():
    """List all income records"""
    return dummy_income_db


# PUBLIC_INTERFACE
@income_router.post("/", response_model=IncomeRecord)
def add_income(record: IncomeRecord):
    """Add a new income record"""
    dummy_income_db.append(record)
    return record
