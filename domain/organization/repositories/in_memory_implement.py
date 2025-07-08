from datetime import datetime

from .interface import IOrganizationRepository


class InMemoryOrganizationRepository(IOrganizationRepository):
    def __init__(self, logger):
        self._store = {}
        self.logger = logger

    def create(self, name: str, org_id: str):
        # Check if already exists
        if org_id in self._store:
            self.logger.error("error")
            raise

        self._store[org_id] = {"name": name, "created_at": datetime.now().isoformat()}

    def read_all(self):
        if not self._store:
            self.logger.warning("")
            return []

        organization_list = []

        for id, info in self._store.items():
            organization_info = {**info, "org_id": id}

            organization_list.append(organization_info)

        return organization_list

    def read_by_id(self, org_id: str):
        if not org_id in self._store:
            self.logger.error("error")
            raise

        return {"org_id": org_id, **self._store[org_id]}

    def update(self, id: str, data: dict):
        self._store[id] = data
        return data

    def delete_by_id(self, org_id: str):
        if not org_id in self._store:
            self.logger.error("error")
            raise

        del self._store[org_id]

        print(self._store)
