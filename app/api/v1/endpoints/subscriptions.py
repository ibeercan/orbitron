from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.auth.deps import get_current_active_user
from app.models.user import User, SubscriptionType

router = APIRouter()


@router.get("/me")
async def get_subscription(
    *,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's subscription info.
    """
    return {
        "subscription_type": current_user.subscription_type,
        "subscription_end": current_user.subscription_end.isoformat() if current_user.subscription_end else None,
    }


@router.post("/upgrade")
async def upgrade_subscription(
    *,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
    plan: str = "monthly",  # monthly, quarterly, yearly
) -> Any:
    """
    Upgrade user subscription (placeholder - payment integration needed).
    """
    # TODO: Integrate payment gateway (Stripe, etc.)
    # For now, just update in DB
    from datetime import datetime, timedelta

    if plan == "monthly":
        days = 30
    elif plan == "quarterly":
        days = 90
    elif plan == "yearly":
        days = 365
    else:
        raise ValueError("Invalid plan")

    current_user.subscription_type = SubscriptionType.PREMIUM
    current_user.subscription_end = datetime.utcnow() + timedelta(days=days)
    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)

    return {"message": f"Subscription upgraded to {plan} plan"}