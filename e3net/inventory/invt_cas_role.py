#
#Copyright (c) 2018 Jie Zheng
#
from e3net.inventory.invt_base import get_inventory_base
from e3net.common.e3exception import e3_exception
from e3net.common.e3exception import E3_EXCEPTION_IN_USE
from e3net.common.e3exception import E3_EXCEPTION_NOT_FOUND
from e3net.common.e3exception import E3_EXCEPTION_INVALID_ARGUMENT
from e3net.common.e3exception import E3_EXCEPTION_OUT_OF_RESOURCE
from e3net.common.e3exception import E3_EXCEPTION_NOT_SUPPORT
from e3net.common.e3exception import E3_EXCEPTION_BE_PRESENT
'''
root_key is 'role'
while sub_key is the uuid of the role
'''

default_user_timeout=60
root_key='role'

def invt_register_cas_role(fields_create_dict,user_sync=False,user_timeout=default_user_timeout):
    assert('name' in fields_create_dict)
    base=get_inventory_base()
    assert(base)
    return base.register_object(root_key,fields_create_dict,user_sync=user_sync,user_timeout=user_timeout)

def invt_update_cas_role(role_uuid,fields_change_dict,user_sync=False,user_timeout=default_user_timeout):
    base=get_inventory_base()
    assert(base)
    sub_key=role_uuid
    base.update_object(root_key,sub_key,fields_change_dict,user_sync=user_sync,user_timeout=user_timeout)

def invt_unregister_cas_role(role_uuid,user_sync=False,user_timeout=default_user_timeout):
    sub_key=role_uuid
    base=get_inventory_base()
    assert(base)
    base.unregister_object(root_key,sub_key,user_sync=user_sync,user_timeout=user_timeout)

def invt_get_cas_role(role_uuid):
    sub_key=role_uuid
    base=get_inventory_base()
    assert(base)
    return base.get_object(root_key,sub_key)

def invt_list_cas_roles():
    base=get_inventory_base()
    assert(base)
    return base.list_objects(root_key)
