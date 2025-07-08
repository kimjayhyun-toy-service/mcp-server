from dependency_injector import containers, providers

from domain.organization.repositories.in_memory_implement import (
    InMemoryOrganizationRepository,
)
from domain.organization.services.implement import OrganizationService
from utils import setup_logger


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logger = providers.Singleton(setup_logger, logger_name=config.msaname)

    organization_repository = providers.Singleton(
        InMemoryOrganizationRepository, logger=logger
    )

    organization_service = providers.Singleton(
        OrganizationService, repository=organization_repository, logger=logger
    )
