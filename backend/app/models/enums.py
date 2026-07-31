from enum import Enum


class UserRole(str, Enum):
    CITIZEN = "citizen"
    STAFF = "staff"
    MP = "mp"
    ADMIN = "admin"


class Language(str, Enum):
    ENGLISH = "english"
    SWAHILI = "swahili"