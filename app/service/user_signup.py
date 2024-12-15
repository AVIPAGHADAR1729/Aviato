from fastapi import HTTPException
from google.cloud.firestore_v1.field_path import FieldPath

from app import app


class AccountCreateService:
    __slots__ = ("dto",)

    def __init__(self, dto):
        self.dto = dto
        self.dto.users_ref = app.firestore.collection("users")

    async def create_user(self):

        if hasattr(self.dto, "email"):
            email_query = self.dto.users_ref.where(
                "email", "==", self.dto.email
            ).stream()
            if any(email_query):
                raise HTTPException(status_code=400, detail="Email already exists.")

        if hasattr(self.dto, "mobile"):
            mobile_query = self.dto.users_ref.where(
                "mobile", "==", self.dto.mobile
            ).stream()
            if any(mobile_query):
                raise HTTPException(
                    status_code=400, detail="Mobile number already exists."
                )

        if not hasattr(self.dto, "email") or not hasattr(self.dto, "mobile"):
            raise HTTPException(status_code=400, detail="Invalid request payload!")

        doc_ref = self.dto.users_ref.add(self.dto.dict())
        user_id = doc_ref[1].id

        return {
            **self.dto.dict(),
            "user_id": user_id,
            "message": "User created successfully",
        }

    async def update_user(self, user_id: str):
        user_doc = self.dto.users_ref.document(user_id)

        if not user_doc.get().exists:
            return {"message": "User not found", "user_id": user_id}

        user_data = self.dto.dict(exclude_none=True)

        # Update the Firestore document with the provided data
        user_doc.update(user_data)

        return {
            "ok": True,
            "message": "User updated successfully",
            "user_id": user_id,
            "updated_data": user_data,
        }

    async def delete_user(self):
        user_doc = self.dto.users_ref.document(self.dto.user_id)

        if not user_doc.get().exists:
            return {"message": "User not found", "user_id": self.dto.user_id}

        user_doc.delete()

        return {
            "ok": True,
            "message": "User deleted successfully",
            "user_id": self.dto.user_id,
        }

    async def get_users(self):
        query = self.dto.users_ref.where(
            FieldPath.document_id(), "in", self.dto.user_id
        )
        results = query.stream()

        users = [doc.to_dict() for doc in results]

        return {"ok": True, "users": users}
