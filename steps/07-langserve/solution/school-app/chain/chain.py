from langchain_google_vertexai import VertexAI

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable


def get_chain() -> Runnable:
    """Return a chain."""
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="""
            En cas de questionnement sur un concept. Il faudra y répondre selon le mode suivant. La description doit être construite en deux blocs.
            Le premier doit décrite de manière succinte mais précise le concept souhaité.
            Le second bloc doit donner les grands lignes du concept, pour ainsi donner les différents éléments qu'il serait intéressant d'écliricir pour mieux comprendre le concept
            """
            ),
            # Message humain à partir d'un template
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )
    llm = VertexAI(model_name="gemini-pro", temperature=0.1)
    output_parser = StrOutputParser()

    return prompt | llm | output_parser
