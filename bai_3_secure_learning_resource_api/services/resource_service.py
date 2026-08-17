from fastapi import HTTPException, status

from models.data import resources


def visible_resources(user: dict):
    if user["role"] == "admin":
        return resources
    return [item for item in resources if item["is_published"]]


def get_resource(resource_id: int, user: dict):
    item = next((r for r in resources if r["id"] == resource_id), None)

    if item is None:
        raise HTTPException(status_code=404, detail="Resource not found")

    if user["role"] != "admin" and not item["is_published"]:
        raise HTTPException(status_code=404, detail="Resource not found")

    return item


def create_resource(data, username: str):
    new_id = max((r["id"] for r in resources), default=0) + 1
    item = {
        "id": new_id,
        "title": data.title,
        "description": data.description,
        "url": str(data.url),
        "is_published": False,
        "created_by": username,
    }
    resources.append(item)
    return item


def publish_resource(resource_id: int, published: bool):
    item = next((r for r in resources if r["id"] == resource_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    item["is_published"] = published
    return item


def delete_resource(resource_id: int):
    index = next(
        (i for i, r in enumerate(resources) if r["id"] == resource_id),
        None,
    )
    if index is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.pop(index)
