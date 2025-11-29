from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

class MCQChain:
    def __init__(self, model_name="gemini-2.0-flash-lite"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

        self.prompt = ChatPromptTemplate.from_template("""
        You are an expert interviewer preparing MCQs for tech interviews. The interview is based on {company} of {jrole}
        Generate {count} {difficulty}-level MCQs for the topic "{topic}".   
        Return output strictly as JSON in this format:
        [
            {{
                "question": "Question text here", 
                "options": ["A) Option 1","B) Option 2","C) Option 3","D) Option 4"], 
                "correct_answer": "A", 
                "explanation": "Brief reason why A is correct"
            }}
        ]
        """)

        self.chain = (
            self.prompt
            | self.llm
            | JsonOutputParser() 
        )

    def generate(self,company,jrole, topic, difficulty="medium", count=5):
        result = self.chain.invoke({
            "company": company,
            "jrole": jrole, 
            "topic": topic,
            "difficulty": difficulty,
            "count": count
        })
        return result
