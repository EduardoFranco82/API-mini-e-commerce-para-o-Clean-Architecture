from fastapi import APIRouter
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.supplier_route import router as supplier_router
from src.presentation.fastapi.routes.categorie_route import router as categorie_router
from src.presentation.fastapi.routes.payment_methods_router import router as payment_method_router
from src.presentation.fastapi.routes.coupons_route import router as coupon_router
from src.presentation.fastapi.routes.customer_route import router as customer_router
from src.presentation.fastapi.routes.address_route import router as address_router


router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(supplier_router, prefix='/suppliers', tags=['supplier'])
router.include_router(categorie_router, prefix='/categorie', tags=['categorie'])
router.include_router(payment_method_router,prefix='/payment_method', tags=['payment_method'])
router.include_router(coupon_router,prefix='/coupon', tags=['coupon'])
router.include_router(customer_router, prefix='/customer', tags=['customer'])
router.include_router(address_router, prefix='/address', tags=['address'])