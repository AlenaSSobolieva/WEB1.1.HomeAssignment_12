# fastapi_contacts/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_contacts.app.routes import router as contacts_router

from fastapi_contacts.app.database import create_tables, engine

app = FastAPI()

# Allow CORS for all origins in your development environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router for contacts
app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])

# Call create_tables to initialize the database tables
create_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)



