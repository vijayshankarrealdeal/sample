from fastapi import APIRouter
from routes.user_auth import user_router
from routes.learn import learn_router

router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(learn_router, prefix="/learn", tags=["learn"])