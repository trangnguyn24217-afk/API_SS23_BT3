from fastapi import APIRouter, Depends, status

from dependencies.authentication import get_current_user
from dependencies.authorization import require_admin
from schemas.schemas import PublishRequest, ResourceCreate
from services.resource_service import (
    create_resource,
    delete_resource,
    get_resource,
    publish_resource,
    visible_resources,
)

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("")
def list_resources(current_user: dict = Depends(get_current_user)):
    return {"items": visible_resources(current_user)}


@router.get("/{resource_id}")
def read_resource(
    resource_id: int,
    current_user: dict = Depends(get_current_user),
):
    return get_resource(resource_id, current_user)


@router.post("", status_code=status.HTTP_201_CREATED)
def add_resource(
    data: ResourceCreate,
    current_user: dict = Depends(require_admin),
):
    return create_resource(data, current_user["username"])


@router.patch("/{resource_id}/publish")
def update_publish(
    resource_id: int,
    data: PublishRequest,
    current_user: dict = Depends(require_admin),
):
    return publish_resource(resource_id, data.is_published)


@router.delete("/{resource_id}")
def remove_resource(
    resource_id: int,
    current_user: dict = Depends(require_admin),
):
    return delete_resource(resource_id)
