from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

app = FastAPI(
    title="GigHub API - C027-01-0848/2024",
    description="API for managing freelance gigs",
    version="1.0.0"
)
class Category(str, Enum):
    DEVELOPMENT = "Development"
    DESIGN = "Design"
    WRITING = "Writing"


class Status(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"
@app.get("/")
def root():
    return {"message": "Welcome to GigHub API"}   
   
class Gig(BaseModel):
    id: int
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=500)
    category: Category
    budget: float = Field(..., gt=0)
    currency: str
    status: Status
    client_name: str = Field(..., min_length=2, max_length=50)


class GigCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=500)
    category: Category
    budget: float = Field(..., gt=0)
    client_name: str = Field(..., min_length=2, max_length=50)


class GigUpdate(BaseModel):
    budget: Optional[float] = Field(None, gt=0)
    status: Optional[Status] = None

gigs_db = [
    {
        "id": 1,
        "title": "Build Portfolio Website",
        "description": "Create a responsive portfolio website using HTML, CSS and JavaScript.",
        "category": "Development",
        "budget": 18000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Alma Mutheu"
    },
    {
        "id": 2,
        "title": "Design Company Logo",
        "description": "Design a professional logo for a new startup with three revisions.",
        "category": "Design",
        "budget": 7000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Davis Maina"
    },
    {
        "id": 3,
        "title": "Write Blog Articles",
        "description": "Write five SEO-friendly blog articles about technology and innovation.",
        "category": "Writing",
        "budget": 9000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Marggie Wanja"
    }
]    
@app.get("/gigs")
def get_gigs(
    category: Optional[str] = None,
    min_budget: Optional[float] = None,
    max_budget: Optional[float] = None
):
    results = gigs_db

    if category:
        results = [
            gig for gig in results
            if gig["category"].lower() == category.lower()
        ]

    if min_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] >= min_budget
        ]

    if max_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] <= max_budget
        ]

    return results
    
@app.get("/gigs/search")
def search_gigs(q: str):
    results = []

    for gig in gigs_db:
        if q.lower() in gig["title"].lower():
            results.append(gig)

    if not results:
        return {
            "message": "No gigs found",
            "results": []
        }

    return {
        "results": results
    }
    
@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )
    
@app.post("/gigs")
def create_gig(gig: GigCreate):
    new_id = len(gigs_db) + 1

    new_gig = {
        "id": new_id,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": "KES",
        "status": "Open",
        "client_name": gig.client_name
    }

    gigs_db.append(new_gig)

    return {
        "message": "Gig created successfully",
        "gig": new_gig
    }
    
@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig_update: GigUpdate):

    for index, gig in enumerate(gigs_db):

        if gig["id"] == gig_id:

            if gig_update.budget is not None:
                gigs_db[index]["budget"] = gig_update.budget

            if gig_update.status is not None:
                gigs_db[index]["status"] = gig_update.status

            return {
                "message": "Gig updated successfully",
                "gig": gigs_db[index]
            }

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )
    
@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):

    for index, gig in enumerate(gigs_db):

        if gig["id"] == gig_id:

            deleted_gig = gigs_db.pop(index)

            return {
                "message": "Gig deleted successfully",
                "gig": deleted_gig
            }

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )