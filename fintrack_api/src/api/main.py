from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import feature routers
from .routers.income import income_router
from .routers.expenses import expenses_router
from .routers.budget import budget_router
from .routers.reports import reports_router

# Initialize FastAPI app
app = FastAPI(
    title="FinTrack API",
    description=(
        "A comprehensive API to manage personal finance data including "
        "income, expenses, budgets, and reports."
    ),
    version="1.0.0"
)

# CORS Middleware for development ease (in production, adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PUBLIC_INTERFACE
@app.get("/")
def health_check():
    """Health check endpoint to verify API availability."""
    return {"message": "Healthy"}


# Include routers for each feature domain

app.include_router(income_router, prefix="/income", tags=["Income Management"])
app.include_router(expenses_router, prefix="/expenses", tags=["Expense Tracking"])
app.include_router(budget_router, prefix="/budgets", tags=["Budget Planning"])
app.include_router(reports_router, prefix="/reports", tags=["Reporting"])
