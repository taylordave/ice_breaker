from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    given the LinkedIn information {information} about the person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model='mistral')

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        mock=True
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
