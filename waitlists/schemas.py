from datetime import datetime
from ninja import Schema
from pydantic import EmailStr

class WaitListEntryCreateSchema(Schema):
    #Create -> Data
    #WaitlistEntryIn
    email: EmailStr

class WaitListEntryDetailSchema(Schema):
    #Get -> Data
    #WaitlistEntryOut
    email: str
    timestamp: EmailStr