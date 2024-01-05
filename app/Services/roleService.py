from app.Contract.Response.getUserRoleResponse import Role,Pivot
from ..Configurations.constants import PSYCHOLOGIST_ROLE_LABEL,PSYCHOLOGIST_ROLE_NAME,PSYCHOLOGIST_ROLE_ID,CUSTOMER_ROLE_ID,CUSTOMER_ROLE_LABEL,CUSTOMER_ROLE_NAME

def getUserRole()-> Role:
    user = userService.getUser() #TODO cache se nikana he

    if user.roleId==PSYCHOLOGIST_ROLE_ID:
        pivot= Pivot(PSYCHOLOGIST_ROLE_ID,user.id)
        response = Role(user.create, user.id, PSYCHOLOGIST_ROLE_LABEL, PSYCHOLOGIST_ROLE_NAME, pivot, user.updated)
        return response
    else
        pivot = Pivot(CUSTOMER_ROLE_ID, user.id)
        response = Role(user.create, user.id, CUSTOMER_ROLE_LABEL, CUSTOMER_ROLE_NAME, pivot, user.updated)
        return response