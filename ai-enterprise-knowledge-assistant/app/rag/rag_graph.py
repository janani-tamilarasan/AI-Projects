from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate

from app.rag.retriever import retriever
from app.rag.llm import get_llm


class RAGState(TypedDict):

    question: str
    documents: list
    answer: str


# -----------------------------
# 1. RETRIEVE
# -----------------------------

def retrieve(state: RAGState):

    question = state["question"]

    documents = retriever.invoke(
        question
    )

    return {
        "documents": documents
    }


# -----------------------------
# 2. GENERATE
# -----------------------------

def generate(state: RAGState):

    question = state["question"]

    documents = state["documents"]

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert technical recruiter.

        Analyze the candidate information provided in the context
        and answer the user's question.

        Use ONLY the information provided in the context.

        If the information is not available in the context,
        clearly say that the information is not available.

        Context:
        {context}

        Question:
        {question}

        Provide a clear and concise answer.
        """
    )

    messages = prompt.format_messages(
        context=context,
        question=question
    )
    llm = get_llm()
    response = llm.invoke(
        messages
    )

    return {
        "answer": response.content
    }


# -----------------------------
# 3. BUILD GRAPH
# -----------------------------

def build_graph():

    graph = StateGraph(
        RAGState
    )

    # Nodes

    graph.add_node(
        "retrieve",
        retrieve
    )

    graph.add_node(
        "generate",
        generate
    )

    # Edges

    graph.add_edge(
        START,
        "retrieve"
    )

    graph.add_edge(
        "retrieve",
        "generate"
    )

    graph.add_edge(
        "generate",
        END
    )

    return graph.compile()