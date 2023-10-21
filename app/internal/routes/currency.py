from fastapi import APIRouter
from app.package.redis_tools.tools import RedisTools

router = APIRouter(
    prefix='/api/v1/currency'
)


@router.get('/{pair}')
def currency_pair(pair: str):
    if pair not in [s.decode('utf-8') for s in RedisTools.get_keys()]:
        return {'error': 'This pair does not exists'}

    return {
        'pair': pair,
        'price': RedisTools.get_pair(pair)
    }


