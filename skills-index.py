import pinecone

pinecone.init(api_key="YOUR_API_KEY", environment="us-east1-gcp")

# Create index for skills embedding
pinecone.create_index(
    name="skills-index",
    dimension=768,
    metric="cosine"
)

index = pinecone.Index("skills-index")