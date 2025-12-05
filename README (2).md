# Kasparro — Agentic Facebook Performance Analyst

python -V  # >= Python 3.10 recommended
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py "Write 3 Facebook ad copies for Christmas sale"
python run.py "Analyze CTR drop and suggest improvements"


## Data
Default CSV: data/sample_ads.csv

To use your own dataset:

Replace sample file inside /data/

Or configure path in data_agent.py

Data fields expected include (loose schema support):

spend, clicks, revenue, ctr, roas, etc.

Schema validation warnings will be logged but system will continue.

## Config
Edit `config/config.yaml`:
```yaml
python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: true
```
(Currently minimal but modular — will expand soon)

Inside code:

Keyword-based task classification (Creative vs Analytics)

Creative themes: 🎄 Christmas / ⚡ Black Friday / Generic fallback

Product detection: Shoes (expandable)

## Repo Map
kasparroagenticfbanalystvinit/
│
├── run.py
├── README.md
│
├── data/
│   └── sample_ads.csv
│
└── src/
    ├── agents/
    │   ├── planner.py
    │   ├── data_agent.py
    │   ├── insight_agent.py
    │   ├── creative_agent.py
    │   └── evaluator_agent.py
    │
    ├── orchestrator/
    │   └── orchestrator.py
    │
    └── utils/
        └── logger.py


## Run
python run.py "Analyze CTR drop and suggest improvements"
python run.py "Black Friday Ad for Shoes"


## Outputs
Creative tasks produce:

3+ ad variations with:

✨ Headline

📝 Body text

🎬 Format suggestion (image / carousel / video)

Analytics tasks produce:

KPIs: CTR, ROAS, Spend, Revenue

Insights + recommendations

Best variant suggestion (from evaluator)

Logs printed to console + via logger.py

## Observability
Planned upcoming improvements:

JSON agent traces (input → output)

Creative scoring breakdown

Option to save output into:

/reports/insights.json

/reports/creatives.json

Option to integrate Langfuse later

Goal: “Team-ready” debugging & collaboration

## Release
- Tag: `v1.0` and paste link here.

## Self-Review
To be added in PR:

How Planner routes tasks intelligently

Why CreativeAgent has theme/product fallback

Design tradeoffs (fast dev vs modular scalability)

👏 Project Status
Task Type	Result
Creative generation	✔ Working
Analytics insights	✔ Working
Theme + product detection	✔ Working
Error handling	✔ Stable
Team observability	🔜 Enhancing

