from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_base.conections import Base, engine
from api.route_scheme import router as api_router

#
#  Upon startup, verify storage and initialize physical tables if they do not exist
Base.metadata.create_all(bind=engine)

# inicialize core of the web server
app = FastAPI(title="User Management API", description="API for managing users", version="1.0.0")

# Add CORS middleware
# it blocks the access to the API from other domains, but we can configure it to allow access from specific domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routes
app.include_router(api_router)