## MarketAI Suite

MarketAI Suite is a Flask web app that generates marketing campaigns, sales pitches, and lead scores using the Groq API. It provides a clean UI with three tools backed by simple JSON endpoints.

## Features

- Campaign generator for product, audience, and platform
- Sales pitch generator tailored to a customer persona
- Lead scoring with JSON output (score, reasoning, probability)

## Tech Stack

- Python + Flask
- Groq API client
- HTML/CSS/JS frontend

## Setup

1) Create and activate a Python environment (optional but recommended).
2) Install dependencies:

```
pip install -r hackathon/requirements.txt
```

3) Set your Groq API key:

Windows (PowerShell):

```
$env:GROQ_API_KEY="your_api_key_here"
```

Windows (Command Prompt):

```
set GROQ_API_KEY=your_api_key_here
```

## Run

From the repository root:

```
python hackathon/app.py
```

Open the app in your browser:

```
http://127.0.0.1:5000
```

## API Endpoints

All endpoints accept JSON and return JSON.

### POST /api/campaign

Request body:

```
{
	"product": "Eco-friendly bamboo water bottle",
	"audience": "Gen Z outdoor enthusiasts",
	"platform": "Instagram"
}
```

### POST /api/pitch

Request body:

```
{
	"product": "Enterprise CRM Software",
	"persona": "CTO of a mid-sized fintech company"
}
```

### POST /api/score

Request body:

```
{
	"lead_name": "John Doe",
	"budget": "$5,000 - $10,000",
	"need": "Automate workflow",
	"urgency": "High"
}
```

Response example:

```
{
	"result": {
		"score": 82,
		"reasoning": "Strong budget fit and urgent timeline",
		"conversion_probability": "68%"
	}
}
```

## Troubleshooting

- If the app exits immediately, make sure `GROQ_API_KEY` is set in your environment.
- If port 5000 is busy, stop the conflicting process or change the port in `app.py`.
