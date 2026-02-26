# 📍 Geocode Automation Tool

A simple Python tool for batch geocoding addresses using Google Geocoding API.

This program reads addresses from Excel, converts them to latitude & longitude, validates Dumai area boundaries, and saves the results into a new Excel file.

## ⚙️ Requirements

- Python 3.10+
- Google Geocoding API Key
- Internet

---

## 🚀 Installation

### 1. Clone repository
```bash
git clone https://github.com/USERNAME/geocoding-dumai.git
cd geocoding-dumai
```
### 2. Create virtual environment
```bash
python -m venv .venv
```
# Windows
```bash
.venv\Scripts\activate
```
# Mac/Linux
```bash
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
🔑 Setup Google API Key

Go to Google Cloud Console: https://console.cloud.google.com/
<br>Enable Geocoding API
<br>Create an API key
<br>Create .env file in project root: GOOGLE_API_KEY=YOUR_API_KEY

▶️ Run the program
```bash
python main.py
```
