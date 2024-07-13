from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class RepoModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
    repo_id: str
    name: str
    stars: int
    owner: str
    description: str
    forks: int
    languages: list[str]
    topics: list[str]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


if __name__ == "__main__":
    repo = RepoModel(
        repo_id="234",
        name="test-repo",
        stars=100,
        owner="test-owner",
        description="test-description",
        forks=10,
        languages=["Python", "JavaScript"],
        topics=["test-topic1", "test-topic2"],
    )
    
    print('repo type:', type(repo))
    print(repo)
