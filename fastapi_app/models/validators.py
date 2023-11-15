import re
from datetime import datetime
from typing import Optional

from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException
from pydantic import BaseModel, field_validator

MSG_DATE_INVALID = "Invalid date format. Please use 'DD.MM.YYYY' or 'YYYY-MM-DD'"
MSG_PHONE_NUM_INVALID_CODE = "Phone number should start with '7' or '+7'"
MSG_PHONE_NUM_INVALID_LEN = "Phone number should contain 11 digits"
MSG_EMAIL_INVALID = "Invalid email"


class FormModel(BaseModel):
    date: Optional[str] = None
    phone_num: Optional[str] = None
    email: Optional[str] = None
    text: Optional[str] = None

    @field_validator('date')
    def validate_date(cls, date):
        if date:
            try:
                norm_date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                try:
                    norm_date = datetime.strptime(date, "%d.%m.%Y")
                except ValueError:
                    raise HTTPException(400, MSG_DATE_INVALID)

            return str(norm_date.date())

    @field_validator('phone_num')
    def validate_phone_num(cls, phone_num):
        """Remove leading '+' and get all digits from the phone number"""
        if phone_num:
            ru_code = '7'
            norm_number = "".join(re.findall(r"\d+", phone_num))

            if not norm_number.startswith(ru_code):
                raise HTTPException(400, MSG_PHONE_NUM_INVALID_CODE)
            if len(norm_number) != 11:
                raise HTTPException(400, MSG_PHONE_NUM_INVALID_LEN)

            return norm_number

    @field_validator('email')
    def validate_email(cls, email):
        if email:
            try:
                return validate_email(email, check_deliverability=False).normalized
            except EmailNotValidError:
                raise HTTPException(400, MSG_EMAIL_INVALID)


DEFAULT_RESPONSE = {key: str(value) for key, value in FormModel.__annotations__.items()}
