from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

# Define a GraphQL schema using dataclasses
@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, id: int) -> User:
        return User(id=id, name="sarthak Doe", email="sarthsak@example.com")

# Create a FastAPI app with GraphQL
schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# Run server: uvicorn filename:app --reload
