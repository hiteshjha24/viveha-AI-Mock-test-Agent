import json
from chains.mcq_chain import MCQChain

class MCQAgent:
    def __init__(self):
        self.chain = MCQChain()

    def run(self, round_data):
        difficulty = round_data.get("difficulty", "medium")
        topics = round_data.get("topics", [])
        aggregated = []
        for topic in topics:
            print(f"Generating MCQs for topic: {topic} based on provided job role")
            raw = self.chain.generate(
                company=round_data["company"],
                jrole=round_data["jrole"],
                topic=topic,
                difficulty=difficulty,
                count=round_data["count"]
            )

            try:
                questions = json.loads(raw)
            except Exception:
                questions = {"raw": raw}
            aggregated.append({"topic": topic, "questions": questions})
        return {"type": "MCQ", "round_data": round_data, "generated": aggregated}
