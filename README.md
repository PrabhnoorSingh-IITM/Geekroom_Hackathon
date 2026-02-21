# InsightForge

Hey, welcome to InsightForge. I built this e-commerce intelligence research agent to help teams make sense of fragmented data—catalogs, reviews, pricing, and competitor listings—and turn them into actionable business decisions.

Instead of staring at basic up-and-down charts, you can give InsightForge a brief, upload your data (or use the provided samples), and get a structured, strategic report. Quick mode gives you fast answers in seconds, while deep mode takes a bit longer to provide a comprehensive strategy.

## Features

- Quick mode for fast answers and Deep mode for strategy
- Actionable recommendations based on hard evidence
- Data completeness checks to flag noise
- Persistent memory so it learns over time
- Fully functioning API built with FastAPI
- Web dashboard for easy interaction

## Project Structure

- `src/research_agent.py`: The core research engine
- `api/`: FastAPI backend with rate limiting, logging, and validation
- `webapp/`: The frontend UI dashboard
- `data/domain_memory.json`: Where the agent's memory is stored
- `datasets/`: Processed datasets for sample runs

## How to Run It

### 1. Set up the API

First, install the dependencies:

```bash
pip install -r requirements.txt
```

Then start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

You can check out the API docs at `http://127.0.0.1:8000/docs`.

### 2. Run the Web Dashboard

Open a new terminal window, navigate to the webapp folder, and start a local server:

```bash
cd webapp
python3 -m http.server 5500
```

Open your browser to `http://127.0.0.1:5500` to use the interface.

### Running via CLI

If you prefer the command line, you can run the agent directly:

Quick report:

```bash
python3 src/research_agent.py --brief examples/brief_quick_underperforming.json --output out/quick_report.md --update-memory
```

Deep report:

```bash
python3 src/research_agent.py --brief examples/brief_deep_gap_analysis.json --output out/deep_report.md --update-memory
```

## Datasets

I've included processed JSON datasets in `datasets/processed/` that work out of the box. If you want to use the raw CSV files, you'll need Git LFS:

```bash
git lfs install
git lfs pull
```

## Production Details

The API has a built-in rate limiter (30 requests per minute) and structured logging. You can also enable API key authentication by setting the `ECOM_AGENT_API_KEY` environment variable.

## License

MIT
