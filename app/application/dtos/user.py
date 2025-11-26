from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, eq=False)
class CreateUserDTO:
    tg_id: int


@dataclass(frozen=True, eq=False)
class UserDTO:
    id: UUID
    tg_id: int
