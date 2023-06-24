import chromadb
from chromadb.config import Settings
from pprint import pprint as pp


persist_directory = "chromadb"
chroma_client = chromadb.Client(Settings(
    persist_directory=persist_directory, chroma_db_impl="duckdb+parquet",))
collection = chroma_client.get_or_create_collection(name="knowledge_base")


print('KB presently has %s entries' % collection.count())
print('\n\nBelow are the top 10 entries:')
results = collection.peek()
pp(results)

# delete ada7f455-8bfa-4448-b00c-de56595db57d
collection.delete(ids=["1e8c2fe3-9dee-4780-915e-7ce6e89c05eb"])
