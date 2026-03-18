from fastapi import APIRouter
from services.opendota import get_hero_stats_last_days, get_hero_role_rows_last_days

router = APIRouter()

@router.get("/meta/heroes")
def meta_heroes(days: int = 8):
    rows = get_hero_stats_last_days(days)
    return {"days": days, "rows": rows}

@router.get("/meta/roles")
def meta_roles(days: int = 8):
    rows = get_hero_role_rows_last_days(days)
    return {"days": days, "rows": rows}
