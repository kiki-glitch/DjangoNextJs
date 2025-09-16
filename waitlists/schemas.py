from datetime import datetime
from ninja import Schema
from pydantic import EmailStr
from typing import List

class WaitlistEntryCreateSchema(Schema):
    #Create -> Data
    #WaitlistEntryIn
    email: EmailStr

class ErrorWaitlistEntryCreateSchema(Schema):
    #Create -> Data
    #WaitlistEntryIn
    email: List[dict]
    # non_field_errors: List[str] = []

class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    # updated: datetime
    # timestamp: datetime
    # description: Optional[str] = ""

class WaitlistEntryDetailSchema(Schema):
    #Get -> Data
    #WaitlistEntryOut
    email: EmailStr
    timestamp: datetime
    updated: datetime