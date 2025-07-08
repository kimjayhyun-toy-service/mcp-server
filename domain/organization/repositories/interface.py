# repositories/user_repository.py
from abc import ABC, abstractmethod


class IOrganizationRepository(ABC):
    @abstractmethod
    def create(self, name: str, org_id: str):
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
