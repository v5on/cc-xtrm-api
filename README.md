# 💳 CC-XTRM Credit Card Generator Sub-API

A clean, simple sub-API frontend for securely accessing the main [CC Gen API](https://cc-gen-api-production.up.railway.app) through safe and formatted endpoints.

🔗 **Live Demo:** [https://cc-xtrm-api.vercel.app](https://cc-xtrm-api.vercel.app)

---

## 🌐 Endpoints

### 1️⃣ BIN Information Lookup

**Endpoint:**  
`GET /bin-info`

**Query Parameters:**

| Parameter | Type   | Required | Example             |
|-----------|--------|----------|---------------------|
| `bin`     | string | ✅ Yes   | `515462002115xxxx`  |

**Example Request:**  
```
https://cc-xtrm-api.vercel.app/bin-info?bin=515462002115xxxx
```

**Example Response:**
```json
{
  "bin": "515462",
  "bank": "THE BANCORP BANK NATIONAL ASSOCIATION",
  "country": "UNITED STATES",
  "country_code": "US",
  "flag": "🇺🇸",
  "scheme": "MASTERCARD",
  "type": "DEBIT",
  "prepaid": false,
  "tier": "PREPAID MASTERCARD GIFT CARD",
  "currency": "N/A"
}
```

---

### 2️⃣ Generate Card Details (JSON)

**Endpoint:**  
`GET /generate`

**Query Parameters:**

| Parameter | Type   | Required | Description                         |
|-----------|--------|----------|-------------------------------------|
| `bin`     | string | ✅ Yes   | BIN with optional X's               |
| `limit`   | int    | ❌ No    | Number of cards to generate         |
| `month`   | string | ❌ No    | Expiry month in MM (e.g. `12`)      |
| `year`    | string | ❌ No    | Expiry year in YY (e.g. `28`)       |
| `cvv`     | string | ❌ No    | CVV (e.g. `000`, `rnd`)             |

**Example Request:**  
```
https://cc-xtrm-api.vercel.app/generate?bin=515462002115xxxx&limit=10&month=12&year=28&cvv=000
```

**Example JSON Response:**
```json
{
  "cards": [
    {
      "number": "5154620021152085",
      "expiry": "12/28",
      "cvv": "000",
      "brand": "MASTERCARD",
      "type": "DEBIT"
    },
    ...
  ],
  "bin_info": {
    "bin": "515462",
    "bank": "THE BANCORP BANK NATIONAL ASSOCIATION",
    "country": "UNITED STATES",
    ...
  },
  "generated_at": "2025-07-08T15:18:33.789247"
}
```

---

### 3️⃣ Generate & Download as `.txt`

**Endpoint:**  
`GET /generate/view`

**Query Parameters:** *(same as `/generate`)*

**Example Request:**  
```
https://cc-xtrm-api.vercel.app/generate/view?bin=515462002115xxxx&limit=10&month=12&year=28&cvv=000
```

**Example Response:**
```
BIN: 515462
SCHEME: MASTERCARD
TYPE: DEBIT
TIER: PREPAID MASTERCARD GIFT CARD
PREPAID: False
BANK: THE BANCORP BANK NATIONAL ASSOCIATION
COUNTRY: UNITED STATES (US) 🇺🇸
CURRENCY: N/A
==============================
5154620021156789|12|28|000
...
```

---

## ✅ Features

- ✨ Clean and responsive frontend
- 🔒 Keeps main API hidden for security
- 📦 Returns both JSON and TXT formats
- ⚡ Vercel-deployable & super lightweight

---

## 🚀 Deployment

This app is ready to deploy on [Vercel](https://vercel.com/):

```bash
# Step 1: Clone this repo
git clone https://github.com/yourname/cc-xtrm-api.git
cd cc-xtrm-api

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Deploy to Vercel with vercel.json config
vercel
```

---

## 🧑‍💻 Powered by

- [FastAPI](https://fastapi.tiangolo.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Vercel](https://vercel.com/)
- [CC-Gen Main API](https://cc-gen-api-production.up.railway.app)

---

## 📩 Contact

Need help or want a custom API version?  
📧 [YourEmail@example.com]  
🌐 [Portfolio/Linktree](https://yourdomain.com)

---

> ⚠️ **Disclaimer:** This tool is for educational and testing purposes only. Do not use it for fraudulent activities.