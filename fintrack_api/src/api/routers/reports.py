from fastapi import APIRouter


reports_router = APIRouter()


# PUBLIC_INTERFACE
@reports_router.get("/summary")
def get_summary():
    """Return a simple financial summary for demonstration."""
    # In a real implementation, calculations would reference actual DB or services.
    return {
        "total_income": 3450.0,
        "total_expenses": 190.5,
        "net_savings": 3259.5
    }
