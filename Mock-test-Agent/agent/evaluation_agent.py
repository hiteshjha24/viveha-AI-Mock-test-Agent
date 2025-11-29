from chains.evaluation_chain import EvaluationChain

class EvaluationAgent:
    def __init__(self):
        self.chain = EvaluationChain()

    def evaluate(self, user_submission):
        """
        user_submission structure expected:
        [
            {
                "topic": "Python",
                "question": "...",
                "user_answer": "A",
                "correct_answer": "A"
            },
            ...
        ]
        """
        topic_performance = {}
        total_correct = 0
        total_questions = 0
        for item in user_submission:
            topic = item['topic']
            is_correct = item['user_answer'].strip().upper() == item['correct_answer'].strip().upper()
            
            if topic not in topic_performance:
                topic_performance[topic] = {"correct": 0, "total": 0}
            
            topic_performance[topic]["total"] += 1
            total_questions += 1
            if is_correct:
                topic_performance[topic]["correct"] += 1
                total_correct += 1
        report_summary = ""
        for topic, stats in topic_performance.items():
            percentage = (stats['correct'] / stats['total']) * 100
            report_summary += f"- Topic: {topic}: {stats['correct']}/{stats['total']} correct ({percentage:.1f}%)\n"

        ai_feedback = self.chain.generate_feedback(report_summary)

        return {
            "total_score": f"{total_correct}/{total_questions}",
            "topic_breakdown": topic_performance,
            "ai_feedback": ai_feedback
        }