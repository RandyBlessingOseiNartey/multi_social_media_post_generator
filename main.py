from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel




load_dotenv()

# INITIAL STEP BEFORE THE ACTUAL PARALLEL PIPELINE
inputs=input("what is your content about: ")
 #model initialisation
model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1.0)

 #string parser
stringParser=StrOutputParser()

#DICTIONARY MAKER
def dict_maker(res):
    return {"res": res}
dict_maker_runnable=RunnableLambda(dict_maker)



def innitialStep(inputs:dict):
    
    #prompt
    prompt_template=ChatPromptTemplate.from_messages([("system", "you are a text summarizer"), ("human", "please summarize this content: {inputs}")])

    chain= prompt_template | model | stringParser
    
    res= chain.invoke({"inputs": inputs})
    return res 
    
#converting the nnormal python function into a runnable
movieSummaryRunnable= RunnableLambda(innitialStep)


#PARALLEL CHAIN 1

def linkedInPost(res:dict):
    res=res["res"]
    #prompt
    prompt_template=ChatPromptTemplate.from_messages([("system", "you are a linkedIn Post generator"), ("human", "Please genrate a post for this content: {res}")]) 
    
    chain= dict_maker_runnable | prompt_template | model | stringParser
    linkedIn_post=chain.invoke(res)
    return linkedIn_post

linkedInPostRunnable=RunnableLambda(linkedInPost)


#PARALLEL CHAIN 2
def instagramPost(res:dict):
    res=res["res"]
    #prompt
    prompt_template=ChatPromptTemplate.from_messages([("system", "you are an Instagram Post generator"), ("human", "Please genrate a post for this content: {res}")]) 
    
    chain= dict_maker_runnable | prompt_template | model | stringParser
    instagram_post=chain.invoke(res)
    return instagram_post

instagramPostRunnable=RunnableLambda(instagramPost)
    


final_post=(
    contentSummaryRunnable | dict_maker_runnable | RunnableParallel(branches={"LinkedIn Post: " : linkedInPostRunnable, "Instagram Post: " : instagramPostRunnable })
    
)

post=final_post.invoke(inputs)

post1=post["branches"]["LinkedIn Post: "]
post2=post["branches"]["Instagram Post: "]
print(post1)
print(post2)




















































