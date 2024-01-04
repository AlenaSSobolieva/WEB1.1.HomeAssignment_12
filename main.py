# fastapi_contacts/
# ├── main.py
# ├── app/
# │   ├── __init__.py
# │   ├── models.py
# │   ├── crud.py  # New file for CRUD operations
# │   ├── authentication.py  # New file for authentication
# │   ├── database.py
# │   ├── dependencies.py  # New file for dependencies
# │   └── routes.py
# └── tests/
#     ├── __init__.py
#     ├── test_authentication.py
#     ├── test_contacts.py
#     ├── test_utilities.py
#     └── integration/
#         ├── __init__.py
#         ├── test_integration_auth.py
#         └── test_integration_contacts.py

# uvicorn fastapi_contacts.main:app --reload