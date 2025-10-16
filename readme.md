# Symptom Checker

A simple web app that helps you understand what symptoms might mean. Uses Google's Gemini AI to provide educational health information.

**⚠️ DISCLAIMER:** This is for learning purposes only. Not real medical advice. Always see a doctor.

---

## What It Does

- Enter your symptoms
- Get general info about what they might indicate
- See when you should visit a doctor
- Simple, clean interface

---

## Tech Stack

- Python & Flask (backend)
- HTML/CSS/JavaScript (frontend)
- Google Gemini API (AI)

---

## Project Layout

```
healthcare-symptom-checker/
├── app.py                    # Main backend
├── requirements.txt          # Python packages
├── .env.example             # Template for API key
├── .gitignore              # What to ignore in git
├── README.md               # This file
├── templates/
│   └── index.html          # Website
└── static/
    └── style.css           # Styling
```

---

## Setup

### What You Need

- Python 3.8+
- pip
- Free Gemini API key

### Getting Started

**1. Clone this repo**
```bash
git clone https://github.com/yourusername/healthcare-symptom-checker.git
cd healthcare-symptom-checker
```

**2. Create virtual environment**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install packages**
```bash
pip install -r requirements.txt
```

**4. Get Gemini API key**

- Go to https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy the key

**5. Set up .env file**

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Open `.env` and add your key:
```
GEMINI_API_KEY=your_actual_key_here
```

**6. Run the app**
```bash
python app.py
```

**7. Open in browser**

Visit: http://localhost:5000

---

## How to Use

1. Type your symptoms (be specific)
2. Click "Check Symptoms"
3. Read the educational info
4. See when to visit a doctor
5. Click "Check Again" to try another

---

## API

### POST /api/check-symptoms

Send symptoms, get info back.

**Request:**
```json
{
  "symptoms": "sore throat and fever"
}
```

**Response:**
```json
{
  "success": true,
  "analysis": "Based on your symptoms...",
  "warning": "This is educational info only..."
}
```

---

## Important Notes

- **Educational only** - not a medical diagnosis tool
- Always see a real doctor for actual diagnosis
- App detects emergency symptoms and tells you to go to ER
- Your symptoms are not saved anywhere
- API key is kept private in .env

---

## Recording Demo Video

Show these things:

1. **Setup** - Show folder structure briefly
2. **Installation** - Run `pip install -r requirements.txt`
3. **Get API Key** - Show going to Gemini API website
4. **Config** - Show creating .env file
5. **Running** - `python app.py` and opening browser
6. **Test 1** - Enter "sore throat and fever for 2 days"
7. **Results** - Show the analysis output
8. **Test 2** - Try different symptoms like "persistent headache"
9. **Error Test** - Try empty input to show validation
10. **Code** - Quick walkthrough of app.py and index.html
11. **End** - Mention it can be deployed

Keep it 5-10 minutes, natural and relaxed.

---

## Deploying

Easy ways to host this:

**Render (Free):**
1. Push code to GitHub
2. Sign up at https://render.com
3. Create "New Web Service"
4. Connect your GitHub repo
5. Set `GEMINI_API_KEY` as environment variable
6. Deploy

**Railway (Free):**
1. Go to https://railway.app
2. Connect GitHub
3. Add environment variables
4. Deploy

---

## Troubleshooting

**Problem: "GEMINI_API_KEY not found"**
- Make sure .env file exists
- Check API key is in .env
- Restart Flask app

**Problem: Module not found**
- Run: `pip install -r requirements.txt`
- Make sure venv is activated

**Problem: Port 5000 in use**
- Edit app.py last line: `app.run(debug=True, port=5001)`

**Problem: API key not working**
- Get new key from https://makersuite.google.com/app/apikey
- Update .env

---

## What I Learned Building This

- Flask basics and routing
- Integrating with external APIs
- Prompt engineering for AI
- Building responsive UIs
- Environment variable handling
- Git and GitHub workflow

---

## Future Ideas

- Better UI design
- Multi-language support
- Mobile app version
- Save search history
- Integration with real medical data
- More detailed symptom questions

---

## License

MIT - feel free to use and modify

---
