from role import Role, RolePermission

import asyncio

async def initialize():
  roles = await Role.find({'$or': [{'name': 'OWNER'}, {'name': 'MANAGER'}, {'name': 'WAITER'}]}).to_list()
  
  if len(roles) != 3:
    owner = Role(name='OWNER', permission=[RolePermission(name='__all__', permission=3)])
    manager = Role(name='MANAGER', permission=[RolePermission(name='__all__', permission=3)])
    waiter = Role(name='WAITER', permission=[RolePermission(name='__all__', permission=3)])
    
    await asyncio.gather(owner.save(), manager.save(), waiter.save())