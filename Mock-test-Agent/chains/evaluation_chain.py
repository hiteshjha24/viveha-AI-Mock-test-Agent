from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

class EvaluationChain:
    def __init__(self, model_name="gemini-2.0-flash-lite"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

        self.prompt = ChatPromptTemplate.from_template("""
        You are a senior technical mentor. A student has just submitted a quiz.
        Here is their performance report:
        {report_data}

        Based on this data:
        1. Summarize their strong areas.
        2. Identify which topics they need to focus on for better enhancement.
        3. Provide 2 specific study tips for the weak topics.
        4. Motivate them with a positive note to keep improving.
        5. Try to write in a friendly and supportive manner and write as human way as possible "I mean donot include multiple ** or --"
        Keep the tone encouraging but professional. Keep it under 150 words.
        """)

        self.chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )

    def generate_feedback(self, report_data):
        return self.chain.invoke({"report_data": report_data})