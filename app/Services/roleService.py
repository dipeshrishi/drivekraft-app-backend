import logging

from app.Contract.Response.getUserRoleResponse import Role,Pivot
from ..Configurations.constants import PSYCHOLOGIST_ROLE_LABEL,PSYCHOLOGIST_ROLE_NAME,PSYCHOLOGIST_ROLE_ID,CUSTOMER_ROLE_ID,CUSTOMER_ROLE_LABEL,CUSTOMER_ROLE_NAME
from ..Services import userService
from flask import jsonify

def getUserRole()-> Role:
    user = userService.getUserDetails()

    if user.roleId==PSYCHOLOGIST_ROLE_ID:
        pivot= Pivot(PSYCHOLOGIST_ROLE_ID,user.id)
        response = Role(user.created, user.id, PSYCHOLOGIST_ROLE_LABEL, PSYCHOLOGIST_ROLE_NAME, pivot, user.updated)
    else :
        pivot = Pivot(CUSTOMER_ROLE_ID, user.id)
        response = Role(user.created, user.id, CUSTOMER_ROLE_LABEL, CUSTOMER_ROLE_NAME, pivot, user.updated)
    return response