import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.src.schemas.schema import Query

schema = strawberry.Schema(query=Query)

app = FastAPI(title="FastAPI + Strawberry GraphQL Example")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def root():
    return {"message": "Hello! Go to /graphql for GraphQL Playground"}
