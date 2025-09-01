from importlib.metadata import metadata
from tkinter.messagebox import NO
from PIL import Image
from sentence_transformers import SentenceTransformer,util
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from langchain.chains import RetrievalQA



model = SentenceTransformer("clip-ViT-B-32")
text_model = SentenceTransformer('sentence-transformers/clip-ViT-B-32-multilingual-v1')
embedding_fn = HuggingFaceEmbeddings(model_name="sentence-transformers/clip-ViT-B-32") # 나중에 텍스트 질의를 받을 때 필요한 임베딩 함수를 위해 필요함

paths = ["one.jpeg","two.jpeg","three.jpeg","four.jpeg","five.jpeg","six.jpeg","seven.jpeg","eight.jpeg","nine.jpeg","ten.jpeg","eleven.jpeg"]
image_descriptions = {
    "one.jpeg": "Raccoon photo",
"two.jpeg": "Panda photo",
"three.jpeg": "Tiger photo",
"four.jpeg": "Dog photo, puppy",
"five.jpeg": "Hedgehog photo",
"six.jpeg": "Black cat photo, black kitty photo",
"seven.jpeg": "Grape photo",
"eight.jpeg": "Fluffy cat, pretty kitty",
"nine.jpeg": "Monkey photo",
"ten.jpeg": "Jaguar photo",
"eleven.jpeg" : "Bicycle photo"
}



# collection_metadata를 추가해서 코사인 유사도로 변경해주기
vectordb = Chroma(collection_name="images",collection_metadata={"hnsw:space": "cosine"},embedding_function=embedding_fn)
docs = []
vectors = []
idxs = []
a = model.encode(Image.open(f"./images/one.jpeg"))
# print(a) 
for i, path in enumerate(paths):
  emb = model.encode(Image.open(f"./images/{path}"))

    # Document 형태로 변환
  doc = Document(
        page_content=image_descriptions[f"{path}"],  # 문자열 필수
        # page_content=f"이미지 이름 :{path}",
        metadata={"path": path}             # 메타데이터는 dict 가능
    )

  docs.append(doc)
  vectors.append(emb)
  idxs.append(f"img_{i}")

print("벡터 저장")
vectordb._collection.add(
    ids=idxs,
    embeddings=vectors,
    documents = [d.page_content for d in docs], # page_content가 없으면 none이라는 에러가 나오므로 선언해줘야 한다
    metadatas=[d.metadata for d in docs],
)
print("벡터 저장 종료")







# text_emb = model.encode(Image.open(f"./images/test3.jpeg"))
# text_emb = text_model.encode("monkey")

# score = util.cos_sim([text_emb],vectors)
# print(score)
# results = vectordb._collection.query(
#     query_embeddings=[text_emb],  # 리스트 형태
#     n_results=3
# )

# print(results)


template  = """
You will now take on the role of finding images when requested. 
When an image is found, you should provide a simple description of it, 
for example: 'This is a cute puppy image.' 
Do not show the image name to the user, only return it.
Always respond in Korean.
The phrase that the user will enter is as follows
{question}

Here is the retrieved context:
{context}
"""


prompt = PromptTemplate(
    input_variables=["question","context"],
    template=template
)

retriever = vectordb.as_retriever(search_kwargs={"k":1})

ollama_model_name = "llama3.1:8b"
query ="puppy image"
llm = OllamaLLM(model=ollama_model_name, temperature=0.0)
qa =RetrievalQA.from_chain_type(llm=llm, 
chain_type="stuff",
retriever=retriever,
chain_type_kwargs={"prompt": prompt},
return_source_documents = True)
print(query)
result = qa.invoke({"query": query })
print(result)


