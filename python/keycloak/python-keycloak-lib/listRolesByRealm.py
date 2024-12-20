# List all roles in JSON by the realm you pass in
# to run:  python3 listRolesByRealm.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

import sys
import json
from prettytable import PrettyTable, ALL
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        realm_name=sys.argv[2],
                        client_id=sys.argv[3],
                        client_secret_key=sys.argv[4],
                        verify=True)

print("debug: getting the admin connection set")
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

# set the headers
roleTable = PrettyTable(["ID", "Name", "Description", "ContainerID"], align='l', max_width=40)
roleTable.hrules=ALL

realm_roles = keycloak_admin.get_realm_roles()

# Get Realms
realm_roles = str(realm_roles).replace("'", '"')
realm_roles = str(realm_roles).replace("True", 'true')
realm_roles = str(realm_roles).replace("False", 'false')
role_json_object = json.loads(realm_roles)
#print(json.dumps(json_object, indent=1))

for item in role_json_object:
    roleTable.add_row([item["id"],item["name"],item["description"],item["containerId"]])
# print the table out
print(roleTable)