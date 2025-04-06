# Moustache Escapes Nearby Property Finder API

This Flask-based backend API helps Moustache Escapes' tele-calling team quickly find hotel properties located within a 50km radius of a customer-specified location. It is designed to work in real-time with minimal latency and provides smart location matching even with minor spelling mistakes.

---

## Features

- **Fuzzy Search**: Handles minor spelling errors in city/area names (e.g., `delih` → `Delhi`)
- **Location-Based Search**: Uses latitude and longitude to calculate real distances using the Haversine formula.
- **Dynamic Property Loading**: Loads property data from a `.txt` file.
- **Fast Response**: Optimized for <2 second API response time.

---

## Tech Stack

- Python
- Flask
- Geopy (for geocoding)
- FuzzyWuzzy (for typo correction)
- Haversine Formula (for distance calculation)

---

---

## 📄 Property List Format

`property_list.txt` should be formatted as:
Property Name,Latitude,Longitude

**Example:**
Moustache Jaipur,27.29124839,75.89630143
Moustache Delhi,28.61257139,77.28423582

---

# Run Tests

pytest test_api.py -v

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
    bash
    git clone https://github.com/your-username/moustache-api.git
    cd moustache-api
```

### 2. Create a Virtual Environment

```
    python3 -m venv venv
    source venv/bin/activate
```

### 3. Install Dependencies

```
    pip3 install -r requirements.txt
```

### 3. Run the Server

```
    python3 app.py
```

### Answers of the questions asked in mail :
'''
    https://docs.google.com/document/d/1Lu__agjYk6R0Y3kRyZkRzlegUaPCmIGiCBr6VfYYqdU/edit?usp=sharing
'''
