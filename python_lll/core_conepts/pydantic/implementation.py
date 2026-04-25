from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List, Optional


class Address(BaseModel):
    city: str
    zip_code: str = Field(pattern=r'^\d{5}$') # Must be exactly 5 digits




class UserProfile(BaseModel):
    user_id: int 
    username: str=Field(..., min_length=3, max_length=60)
    address: Optional[Address] = None 
    tags: List[str] = Field(default_factory=list)


    # Custom Validator
    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v:str) -> str:
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v.lower() 
    




## Execution

try:
    payload = {
        "user_id": "101",
        "username": "AdminUser",
        "address": {"city": "Seattle", "zip_code": "98101"}
    }

    user = UserProfile(**payload)
    print(user.model_dump())  # Export back to Dictionary

except ValidationError as e:
    print(e.json())
    




