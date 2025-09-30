# skills_features.py
from feast import Entity, FeatureView, Field
from feast.types import Float32, String

user = Entity(name="user", join_keys=["user_id"])

user_skills = FeatureView(
    name="user_skills",
    entities=[user],
    schema=[
        Field(name="technical_skills", dtype=String),
        Field(name="soft_skills", dtype=String),
        Field(name="skill_levels", dtype=String),
        Field(name="last_updated", dtype=String)
    ],
    online=True,
    source=skills_source
)