from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

class CodingChain:
    def __init__(self, model_name="gemini-2.0-flash-lite"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

        self.prompt = ChatPromptTemplate.from_template("""
        You are an expert interviewer preparing coding for tech interviews in {company} for the role of {jrole}.
        Generate one {difficulty}-level coding question for the topic "{topic}". The question should be a previously asked in the company's interview. Which you can ask from leetcode or codechef like platforms.
        Return output strictly as JSON in this format:
        [
        {{
            "title": "...",
            "description": "...",
            "examples": [{{"input": "...", "output": "..."}}],
            "hidden_tests": [{{"input": "...", "output": "..."}}]
        }}
        ]
        """)

        self.chain = (
            self.prompt
            | self.llm
            | JsonOutputParser() 
        )

    def generate(self,company, jrole, topic, difficulty="medium"):
        result = self.chain.invoke({
            "company": company,
            "jrole": jrole,
            "topic": topic,
            "difficulty": difficulty  
        })
        return result
