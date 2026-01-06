# Viveha AI Mock Test Agent

Viveha AI Mock Test Agent is an AI-powered agent designed to conduct mock tests and assessments, helping users practice and evaluate their skills in an automated, interactive way.[web:2]

## Features

- AI-driven question generation for mock tests.
- Automated evaluation and scoring of user responses.
- Configurable difficulty levels and test lengths.
- Extensible architecture to plug in new domains or question banks.
- Integration with GitHub for version-controlled test workflows (planned).[web:2]

## Tech Stack

- Backend: Python / FastAPI (or preferred web framework)
- AI/LLM: OpenAI / other LLM provider (via API)
- Orchestration: LangChain / custom agent framework
- Data: JSON/DB-backed question and result store
- Tooling: Git, GitHub Actions for CI/CD (optional)[web:2]

Update this section with the exact stack and libraries used in this repo.

## Project Structure

viveha-AI-Mock-test-Agent/
├── src/ # Core agent and business logic
├── tests/ # Unit and integration tests
├── configs/ # Configuration files (YAML/JSON)
├── scripts/ # Helper scripts for setup and maintenance
├── requirements.txt # Python dependencies
└── README.md # Project documentation


Adjust this tree according to the actual folders in your repository.[web:2]

## Getting Started

### Prerequisites

- Python 3.10+ installed
- Git installed
- (Optional) Virtual environment tool such as `venv` or `conda`
- API key for your LLM provider (e.g., OpenAI), stored as an environment variable `LLM_API_KEY`[web:2]

### Installation

Clone the repository
git clone https://github.com/hiteshjha24/viveha-AI-Mock-test-Agent.git
cd viveha-AI-Mock-test-Agent

Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

Install dependencies

pip install -r requirements.txt


### Running the Agent

Set environment variables
export LLM_API_KEY="your_api_key_here"

Run the main app (replace with actual entrypoint)
python -m src.main


After starting, the agent can be accessed via CLI, REST API, or a UI (update this line according to your implementation).[web:2]

## Usage

Typical use cases:

- Run a full mock test session for a chosen topic.
- Generate a quick quiz with N questions.
- Analyze historical performance across multiple mock tests.

## Configuration

- `configs/agent.yaml`: Core agent configuration (LLM model, temperature, max tokens).
- `configs/tests.yaml`: Test templates, difficulty levels, domain configuration.
- `.env` (optional): Local environment variables such as `LLM_API_KEY`.[web:2]

