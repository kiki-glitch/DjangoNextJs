from typing import List

from ninja_jwt.authentication import JWTAuth

from django.shortcuts import get_object_or_404
from ninja import Router
import helpers 

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema, WaitListEntryDetailSchema, WaitListEntryCreateSchema

router = Router()


@router.get("", response=List[WaitlistEntryListSchema], auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.post("", response=WaitListEntryDetailSchema, auth=helpers.api_auth_user_or_annon)
def create_waitlist_entries(request, data:WaitListEntryCreateSchema):
    obj = WaitlistEntry(**data.dict())
    print(request.user)
    obj.save()
    return obj

@router.get("{entry_id}", response=WaitListEntryDetailSchema, auth=helpers.api_auth_user_required)
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj