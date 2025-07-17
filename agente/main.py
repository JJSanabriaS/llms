import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()




from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

os.environ["OPENAI_API_KEY"] = "
#print(os.environ.get("OPENAI_API_KEY")) #key should now be available


template = """ asiistente

historico de conversa
{history}

entrada
{input}"""

prompt = ChatPromptTemplate.from_messages([
   ("system",template),
   MessagesPlaceholder(variable_name="history"),
   ("human","(input)") 
])

llm=ChatOpenAI(temperature=0.7,model="gpt-4o-mini")
chain = prompt | llm

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
) 

def iniciar_Agente():
    print("bemviendo")
    while True:
        pregunta_usuario=input("Voce: ")
        if pregunta_usuario.lower() in ["sair","exit"]:
            print("asistente")
            break
        
        resposta = chain_with_history.invoke(
            {"input":pregunta_usuario},
            config={'configurable': {'session_id':'user123'}}
        )
        
        print('Assistente ', resposta.content)

if __name__ == "__main__":
    iniciar_Agente()

#https://www.youtube.com/watch?v=GCQl9RFns_0