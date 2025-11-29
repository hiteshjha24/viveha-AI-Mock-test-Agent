import json
from chains.coding_chain import CodingChain

class CodingAgent:
    def __init__(self):
        self.chain = CodingChain()

    def run(self, round_data):
        difficulty = round_data.get("difficulty", "medium")
        topics = round_data.get("topics", [])
        aggregated = []
        for topic in topics:
            print(f"Generating coding question for topic: {topic}")
            raw = self.chain.generate(
             topic = topic, 
             difficulty=difficulty,
             company = round_data["company"],
             jrole = round_data["jrole"]
             )
            try:
                questions = json.loads(raw)
            except Exception:
                questions = {"raw": raw}
            aggregated.append({"topic": topic, "questions": questions})
        return {"type": "MCQ", "round_data": round_data, "generated": aggregated}
