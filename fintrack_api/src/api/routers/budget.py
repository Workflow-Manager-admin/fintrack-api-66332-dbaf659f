from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


budget_router = APIRouter()


# PUBLIC_INTERFACE
class Budget(BaseModel):
    """Schema for a budget."""
    id: int
    category: str
    amount: float
    start_date: str
    end_date: str


dummy_budget_db = [
    Budget(
        id=1,
        category="Groceries",
        amount=400.0,
        start_date="2024-06-01",
        end_date="2024-06-30",
    ),
]


# PUBLIC_INTERFACE
@budget_router.get("/", response_model=List[Budget])
def list_budgets():
    """List all budgets"""
    return dummy_budget_db


# PUBLIC_INTERFACE
@budget_router.post("/", response_model=Budget)
def add_budget(budget: Budget):
    """Add a new budget"""
    dummy_budget_db.append(budget)
    return budget
