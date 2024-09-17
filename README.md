# LLM-QA-Bot
This is an End-to-End LLM question-and-answer system using the langchain framework. 

## Concepts:
### LangChain
There is a big boom in the industry where every business wants to build their own LLM

**Why companies cannot directly use ChatGPT or use OpenAI API?**
- ChatGPT has no access to internal organization data
- Calling OpenAI API has higher cost (number of queries -> huge cost)
- ChatGPT has no access to internet / real time knowledge

**This is how Langchain comes into place. What is LangChain then?**
- LangChain is a framework that allows you to build applications based on LLM with external data sources, memory, and other utilities.

**What are the main properties of LangChain framework?**
- **Components**:  
  Components are modular building blocks that are ready and easy to use to build powerful applications. Including:  
  - LLM Wrappers: unified interface to interact with different LLMs)
  - Prompt Template: standardized input fed into the LLMs)
  - Indexes: structure large datasets or documents for quick search).

- **Chains**:  
  Chains refer to sequences of actions that the application will perform. Chains allow you to combine multiple components or tasks into a single workflow.

- **Agents**:  
  Agents use LLMs to make decisions about what actions to take. They interact with external tools (e.g., search engines, APIs, or databases) to fetch real-time or extended information.

- **Memory**:  
  Langchain allows applications to have memory, which means that the application can remember previous interactions and use that context for future conversations.

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

## Technical Architecture
<img width="847" alt="image" src="https://github.com/user-attachments/assets/6f50bd7d-fe30-4a09-bb8c-b4ea3ee5deb4">



