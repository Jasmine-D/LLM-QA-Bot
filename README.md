# LLM-QA-Bot
This is an End-to-End LLM question-and-answer system using the langchain framework. 

## Concepts:
### LangChain
There is a big boom in the industry where every business wants to build their own LLM

**Why companies cannot directly use ChatGPT or use OpenAI API?**
- ChatGPT has no access to internal organization data
- Calling OpenAI API has higher cost (number of queries -> huge cost)
- ChatGPT has no access to internet / real time knowledge

### Vector Database
**How does Google search figure out the different meaning of "Apple" between "calories in Apple" and "employees in Apple"?**
- **Semantic search**:  
  Instead of keyword matching, it understands the intent of user query and use the context to perform the search
  
- **Embedding** (internal mechanism of semantic search):  
  Embedding is a numerical representation of text, which is a vector that contains values for several features.
  
- **Transformer architecture**:  
  One of the most popular word embedding techniques that chatGPT is using.

**How to store the embedding vectors?**
- **Traditional relational database**  
  We first store embeddings into database. Then for a user query:  
  generate an embedding -> linear search the database to calculate `cosine similarity` -> if value closes to 1 then put vector into result dataset
  
  Problem: too many computations and long delay, cannot handle millions of records

- **Vector database**  
  It uses `index` to help you search things faster. How does the database index works?
  It use a hashing function to create buckets of similar looking embeddings so that for the user query, we only need to linear search a small size of data in one bucket.  
  The Technique is called `LSH (Locality Sensitive Hashing)`

  Benefits: fast search & optimized storage




