from typing import Optional

from fastapi import Query

from app import router
from app.common import (
    USER_ACCOUNT_CREATE_API,
    GET_USERS_API,
    DELETE_USER_API,
    UPDATE_USER_API,
    send_invite_email,
    SEND_INVITES,
)
from app.common.schema import (
    UserCreateEmail,
    UserCreateMobileDOB,
    UserCreateMobileHashtag,
    UserGet,
    UserDelete,
)
from app.service import AccountCreateService


@router.post(USER_ACCOUNT_CREATE_API, tags=["create_user"])
async def create_user(
    user: UserCreateEmail | UserCreateMobileDOB | UserCreateMobileHashtag,
):
    return await AccountCreateService(dto=user).create_user()


@router.get(GET_USERS_API, tags=["get_users"])
async def get_users(user_ids: Optional[list[str]] = Query(None)):
    return await AccountCreateService(dto=UserGet(user_ids=user_ids)).get_users()


@router.put(UPDATE_USER_API, tags=["update_user"])
async def update_user(
    user_id: str, user: UserCreateEmail | UserCreateMobileDOB | UserCreateMobileHashtag
):
    return await AccountCreateService(dto=user).update_user(user_id)


@router.delete(DELETE_USER_API, tags=["delete_user"])
async def delete_user(user_id: str):
    return await AccountCreateService(dto=UserDelete(user_id=user_id)).delete_user()


@router.get(SEND_INVITES)
async def send_invite():
    recipients = [
        "dhwanil@aviato.consulting",
        "pooja@aviato.consulting",
        "prijesh@aviato.consulting",
    ]
    response = send_invite_email(
        recipients, REDOC_LINK, FIRESTORE_SCREENSHOT, GITHUB_LINK
    )
    return {"status": response, "message": "Invitation emails sent."}
