from cmath import log
# import ollama
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

from langchain.chains import RetrievalQA


# client = ollama.Client()
ollama_model_name = "llama3.1:8b"
pdf_paths = [
    "./data/a.pdf",
    "./data/b.pdf",
]




class ModelLoader :
    def __init__(self, model_name="jhgan/ko-sbert-nli"):
        self.pdf_paths = pdf_paths
        self.model_name = model_name
        self.retriever = None
    def load(self):
        print("load 시작")
        loaders = [PyPDFLoader(path) for path in self.pdf_paths]
        docs = []
        for loader in loaders:
            docs.extend(loader.load_and_split())
        print(docs)
        print("loders 작업 끝")
        # print(docs[0])
            # 임베딩 생성
        encode_kwargs = {'normalize_embeddings': True}
        print("확인")
        ko_embedding = HuggingFaceEmbeddings(
            model_name=self.model_name,
            encode_kwargs=encode_kwargs,
            model_kwargs = {'device': 'cpu'}
        )
        print("임베딩 ㄱ종료")
        # Child 문서 분할기
        child_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=500)

        # 벡터 스토어와 parent doc store
        vectorstore = Chroma(
            collection_name="full_documents",
            embedding_function=ko_embedding
        )
        store = InMemoryStore()
        print("백터 스토어 작업 끝")
        # ParentDocumentRetriever 생성
        self.retriever = ParentDocumentRetriever(
            vectorstore=vectorstore,
            docstore=store,
            child_splitter=child_splitter
        )
        self.retriever.add_documents(docs,ids=None)
        sub_docs = vectorstore.similarity_search("인공지능 예산")
        print("글 길이: {}\n\n".format(len(sub_docs[0].page_content)))
        print(sub_docs[0].page_content)
    def run(self,query):
        if not self.retriever:
            raise ValueError("RAG not initialized")
        # docs = self.retriever.get_relevant_documents(query)
        print(query)
        llm = OllamaLLM(
            model=ollama_model_name,
        )
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff",retriever=self.retriever,return_source_documents = True)
        return qa.invoke({"query" : query})


# print(1)
# loader = ModelLoader()
# loader.load()
# print(loader.run("극저신용자 대출의 신용등급"))

