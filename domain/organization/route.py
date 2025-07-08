from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from container import Container

from .schema import OrganizationCreateRequest

router = APIRouter(prefix="/organization", tags=["Organization"])


@router.post("/")
@inject
def create_organization(
    request: OrganizationCreateRequest,
    organization_service=Depends(Provide[Container.organization_service]),
):
    name = request.name
    org_id = request.org_id

    created_org_id = organization_service.create(name=name, org_id=org_id)

    return JSONResponse(
        status_code=201,
        content={"message": f"Organization '{name}' created", "org_id": created_org_id},
    )


@router.get("/")
@inject
def get_all_organizations(
    organization_service=Depends(Provide[Container.organization_service]),
):
    list_organization = organization_service.read_all()
    return JSONResponse(status_code=200, content=list_organization)


@router.get("/{org_id}")
@inject
def get_organization_by_id(
    org_id: str = Path(..., description="Organization ID"),
    organization_service=Depends(Provide[Container.organization_service]),
):
    organization = organization_service.read_by_id(org_id=org_id)
    return JSONResponse(status_code=200, content=organization)


@router.delete("/{org_id}")
@inject
def delete_organization_by_id(
    org_id: str = Path(..., description="Organization ID"),
    organization_service=Depends(Provide[Container.organization_service]),
):
    try:
        organization_service.delete_by_id(org_id=org_id)
    except:
        raise HTTPException(
            status_code=404, detail=f"Organization with ID {org_id} not found"
        )
    return JSONResponse(status_code=202, content={"message": "Organization deleted"})
