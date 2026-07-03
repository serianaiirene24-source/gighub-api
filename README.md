 GigHub API
Admission Number: C027-01-0848/2024

 Project Overview
This project is an API built using FastAPI for a  platform called GigHub. The API helps manage freelance job listings by allowing users 
to add, view, update, search, and delete gigs.

 Project Features
The API performs this functions:
* Display all available gigs.
* Filter gigs by category or budget.
* Search for gigs by title.
* View a specific gig using its ID.
* Create a new gig.
* Update the budget or status of an existing gig.
* Delete a gig that is no longer available.

 Gig Information
Each gig record contains the following information:

.ID
.Title
. Description
. Category
. Budget
. Currency
. Status
. Client Name

For this project, the categories used are:

* Development
* Design
* Writing

The currency used is (KES), based on my admission number.

 Technologies Used
. Python
. FastAPI
. Pydantic
. Uvicorn

 API Endpoints

| Method | Endpoint       | Purpose                                  |
| ------ | -------------- | ---------------------------------------- |
| GET    | /              | Displays a welcome message               |
| GET    | /gigs          | Returns all gigs with optional filtering |
| GET    | /gigs/search   | Searches gigs by title                   |
| GET    | /gigs/{gig_id} | Returns one gig using its ID             |
| POST   | /gigs          | Creates a new gig                        |
| PUT    | /gigs/{gig_id} | Updates a gig's budget or status         |
| DELETE | /gigs/{gig_id} | Removes a gig from the list              |

 Validation

The API checks user input before saving a new gig. The title and description must meet the required length, 
the budget must be greater than zero, the category must be one of the allowed categories, 
and the client name must also meet the required length. The status field only accepts Open, In Progress, or Closed.

Running the Project
1. Open the project folder.
2. Run the following command:
   uv run uvicorn main:app --reload
3. Open the following address in your browser:
   http://127.0.0.1:8000/docs
4. Use the Swagger interface to test all the available endpoints.

 Conclusion
This project demonstrates how FastAPI can be used to build a simple REST API with validation and CRUD functionality. 
It also shows how endpoints can be used to manage  gig records efficiently.


