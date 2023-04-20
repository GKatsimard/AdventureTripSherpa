from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    SystemMessage,
    AIMessage,
    HumanMessage,
)
from apikeys import openai_api_key

OPENAI_API_KEY = openai_api_key
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Create System Agent Prompt
prompt=PromptTemplate(
    template="You are a travel agent specialized in {activity} excursions. Answer to questions providing only the requested information and nothing more.",
    input_variables=["activity"]
)
system_agent_prompt = SystemMessagePromptTemplate(prompt=prompt)

# Create Suggestions Prompt
prompt=PromptTemplate(
    template="I live in {user_location}. I love {activity} and I am {difficulty_level}. I would like to go for a {trip_duration} excursion which involves {activity}. Can you give me 10 suggestions in a list and describe each item in the list, along with an explanation why this suggestion matches my preferences?",
    input_variables=["user_location", "activity", "difficulty_level", "trip_duration"]
)
suggestions_prompt = HumanMessagePromptTemplate(prompt=prompt)

# Create ChatPromptTemplate: Combine System + Suggestions
chat_prompt = ChatPromptTemplate.from_messages([system_agent_prompt, suggestions_prompt])

def get_suggestions(activity, user_location, difficulty_level, trip_duration):

    chat_prompt_with_values=chat_prompt.format_prompt(
        activity=activity,
        user_location=user_location,
        difficulty_level=difficulty_level,
        trip_duration=trip_duration
    )
    response = chat(chat_prompt_with_values.to_messages())

    return response