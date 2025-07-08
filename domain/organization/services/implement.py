import uuid
from typing import Optional

from fastapi import HTTPException

from domain.organization.repositories.interface import IOrganizationRepository

from .interface import IOrganizationService


class OrganizationService(IOrganizationService):
    def __init__(self, repository: IOrganizationRepository, logger):
        self.repository = repository
        self.logger = logger

    def create(self, name: str, org_id: Optional[str] = None):
        org_id = org_id or f"org_{uuid.uuid4().hex[:8]}"

        try:
            self.repository.create(name=name, org_id=org_id)
            return org_id

        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Organization with ID {org_id} already exists"
            )

    def read_all(self):
        return self.repository.read_all()

    def read_by_id(self, org_id: str):
        return self.repository.read_by_id(org_id=org_id)

    def update(self): ...

    def delete_by_id(self, org_id: str):
        self.repository.delete_by_id(org_id=org_id)
