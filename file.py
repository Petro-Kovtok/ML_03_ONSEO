from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
import logging

logging.basicConfig(
    format='[%(asctime)s][%(name)s] ~ %(message)s',
    level=logging.INFO
)

# class
class User(BaseModel):
    id: int # field: valid values
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

# this data we will input in user's as arguments
external_data = {
    'id': '322',
    'signup_ts': '2022-05-17 13:15',
    'friends': [1, 2, '3']
}

# create instance of User
user = User(**external_data)

# print(user.id)
# print(repr(user.signup_ts))
# print(user.friends)
# print(user.dict())

User(id=6, signup_ts='1999-09-09 19:24', friends=[1, 2, 4, 'not'])


