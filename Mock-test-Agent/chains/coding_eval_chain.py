from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

class CodingEvalChain:
    def __init__(self, model_name="gemini-2.0-flash-lite"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

        self.prompt = ChatPromptTemplate.from_template("""
        You are a Senior Technical Interviewer evaluating a candidate's code submission.
        
        PROBLEM:
        Title: {title}
        Description: {description}
        
        CANDIDATE'S CODE ({language}):
        ```
        {user_code}
        ```

        Task:
        1. Analyze correctness (does it solve the problem and handle edge cases?).
        2. Analyze Time and Space complexity.
        3. Identify specific bugs or logical errors.
        4. Provide constructive feedback.

        Return output strictly as JSON in this format:
        {{
            "status": "Pass" or "Fail",
            "score": "Integer 0-10",
            "complexity": {{
                "time": "e.g., O(n)",
                "space": "e.g., O(1)"
            }},
            "feedback": "Overall summary of the approach...",
            "mistakes": ["List of specific bugs or logic errors found"],
            "improvements": ["Suggestion 1", "Suggestion 2"]
        }}
        """)

        self.chain = (
            self.prompt
            | self.llm
            | JsonOutputParser() 
        )

    def evaluate(self, title, description, user_code, language="python"):
        result = self.chain.invoke({
            "title": title,
            "description": description,
            "user_code": user_code,
            "language": language
        })
        return result