from datetime import datetime
from ninja import Schema
from pydantic import EmailStr

class WaitListEntryCreateSchema(Schema):
    #Create -> Data
    #WaitlistEntryIn
    email: EmailStr

class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    # updated: datetime
    # timestamp: datetime
    # description: Optional[str] = ""

class WaitListEntryDetailSchema(Schema):
    #Get -> Data
    #WaitlistEntryOut
    email: EmailStr
    timestamp: datetime
    updated: datetime