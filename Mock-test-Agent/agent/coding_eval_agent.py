from chains.coding_eval_chain import CodingEvalChain

class CodingEvaluationAgent:
    def __init__(self):
        self.chain = CodingEvalChain()

    def evaluate(self, submission_data):
        """
        submission_data expected keys:
        - question_title
        - question_description
        - user_code
        - language (optional, default python)
        """
        print(f"Evaluating code for: {submission_data.get('question_title')}")
        
        result = self.chain.evaluate(
            title=submission_data["question_title"],
            description=submission_data["question_description"],
            user_code=submission_data["user_code"],
            language=submission_data.get("language", "python")
        )
        
        return result