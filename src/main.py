from fastapi import FastAPI
from .modules.api_data_models import Message, CalcRequest, CalcResponse
from .schemas import Book
import logging

logging.basicConfig(
    format='[%(asctime)s][%(name)s] ~ %(message)s',
    level=logging.INFO
)

app = FastAPI()
logger = logging.getLogger()

@app.get('/')
def home():
    logger.info('home page')
    return {'key': 'hello'}

@app.get('/{pk}')
def get_item(pk: int, par: str = None): #first parameter obtain by url /{pk}, second parameter obtain by ?q=
    logger.info('get item {}'.format(pk))
    return {'key': pk, 'parameter': par}

@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str ):
    logger.info('get_user_item')
    return {'pk': pk, 'item': item}

@app.post('/book')
def create_book(item: Book):
    logger.info('book created')
    return item
