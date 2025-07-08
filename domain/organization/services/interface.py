from abc import ABC, abstractmethod
from typing import Optional


class IOrganizationService(ABC):
    @abstractmethod
    def create(self, name: str, org_id: Optional[str] = None):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_by_id(self, org_id: str):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete_by_id(self, org_id: str):
        pass
