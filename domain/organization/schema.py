from typing import Optional

from pydantic import BaseModel


class OrganizationCreateRequest(BaseModel):
    name: str
    org_id: Optional[str] = None
