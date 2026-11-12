# ✈️ TravelMate

TravelMate is an AI-powered travel planner that turns a simple prompt like “Plan a 5-day trip to Japan under a $2000 budget” into a structured travel plan with flight suggestions, hotel recommendations, and a day-by-day itinerary.

It combines a FastAPI web app, a LangGraph multi-agent workflow, and live travel data sources to generate practical trip suggestions.

## Highlights

- AI-generated travel itineraries
- Flight search via Aviationstack integration
- Hotel discovery via Tavily search
- Multi-agent workflow for flight, hotel, and itinerary generation
- PostgreSQL-backed conversation and state persistence
- FastAPI frontend with a stylish web UI
- Health check and production-ready API structure

## Tech Stack

- Python 3.11
- FastAPI
- LangGraph
- LangChain + Groq LLM
- PostgreSQL
- Tavily search
- Aviationstack flight API
- Jinja2 + static frontend assets

## Project Structure

```text
TravelMate/
├── app.py                  # FastAPI entry point
├── backend.py              # LangGraph travel orchestration
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container setup
├── .env.example            # Environment variable template (if added)
├── static/                 # Frontend static assets
├── templates/              # Jinja templates
├── tools/
│   ├── flight_tool.py      # Flight parsing and search logic
│   ├── tavily_tool.py      # Hotel search helper
│   └── __init__.py
├── test.py                 # sample usage test
├── README.md               # project docs
└── .gitignore
```

## Features

### Travel planning workflow

The backend creates a multi-step graph that:

1. Searches for relevant flights
2. Finds hotel opportunities using web search
3. Builds a practical itinerary
4. Produces a final polished travel response

### API flow

- `GET /` serves the app frontend
- `POST /api/travel` accepts a travel request and returns structured results
- `GET /health` checks if the server is running

## Environment Setup

Create a `.env` file in the project root with the values below:

```env
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_key
DEFAULT_ORIGIN_IATA=DEL
DATABASE_URL=your_postgres_connection_string
```

Optional AI observability values:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_PROJECT=travel-mate
```

## Installation

### 1) Clone the repository

```bash
git clone https://github.com/Manunkumbar/TravelMate.git
cd TravelMate
```

### 2) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

```text
http://127.0.0.1:8000/
```

## Docker

You can also run the app in a container:

```bash
docker build -t travelmate .
docker run -p 8000:8000 travelmate
```

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Plan a 5-day trip to Japan with a moderate budget",
    "thread_id": "demo-thread"
  }'
```

## Notes

- The app expects valid API keys and a reachable PostgreSQL database for state storage.
- Flight and hotel data may vary depending on live third-party APIs and rate limits.
- Some travel queries may need a default origin airport like `DEL` when only a destination is mentioned.

## License

This project is currently distributed without a formal license file. If you are publishing or sharing it publicly, consider adding an appropriate open-source license.

## Contributing

Contributions are welcome. If you want to improve the planner, add support for more travel sources, or improve the frontend, feel free to open a pull request.
