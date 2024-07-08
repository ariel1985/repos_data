#  pydeantic models for data validation

from pydantic import BaseModel

class RepoCreate(BaseModel):
    name: str

class Repo(BaseModel):
    id: str
    name: str
    stars: int
    owner: str
    description: str
    forks: int
    languages: list[str]
    topics: list[str]
