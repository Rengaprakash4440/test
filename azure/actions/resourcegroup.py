from pydantic import BaseModel
from typing import Optional, List, Dict
from . import actionstore
from azure.identity import ClientSecretCredential
class resourcegroup(BaseModel):
      pass
@actionstore.kubiya_action()
def resourcegroup(_: resourcegroup) -> str:
    credential = ClientSecretCredential(tenant_id=actionstore.secrets.get("AZURE_TENANT_ID"),client_id=actionstore.secrets.get("AZURE_CLIENT_ID"),client_secret=actionstore.secrets.get("AZURE_CLIENT_SECRET"),subscription_id="3d36e840-3f7b-4ea1-ba7b-a690c0f3cc36")
    resource_groups = credential.resource_groups.list()
    for resource_group in resource_groups:
        a = resource_group
    return f"Resource Group Name: {a}"