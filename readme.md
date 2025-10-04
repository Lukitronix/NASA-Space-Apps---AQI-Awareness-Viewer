# AQI Awareness Viewer 🌍

**Team:** Return (0)
**Challenge:** NASA Space Apps Challenge 2025 – AQI Edition
**Purpose:** Make air quality data accessible, understandable, and actionable for the general public.

---

## Project Summary

We developed the **AQI Awareness Viewer**, a web platform designed to make air quality data accessible and understandable to the general public, highlighting the tangible impacts of climate change.

- **Data Source:** Official NASA TEMPO satellite datasets hosted on AWS S3.
- **Core Feature:** Custom API that processes cloud-hosted data without downloads.
- **Predictive Capability:** Machine learning model trained on a decade of atmospheric data, providing a **48-hour AQI forecast**.
- **Goal:** Transform the platform from a simple viewer into a proactive tool, empowering users to make informed decisions about their health and environment.

---

## Project Structure

AQI-Awareness-Viewer/
│
├── ressources/
│   ├── presentation.pdf      # Slide presentation for the project.
│   └── explanation.pdf       # Detailed PDF explaining project workflow.
│
├── web/
│   └── react-app/            # Front-end React application.
│       └── README.md         # React-specific instructions.
│
├── api/
│   ├── app/           # Backend API to send NASA data to front end.
│   ├── prediction/             # Machine Learning model and training scripts.
│   └── README.md             # API usage instructions.
│
└── README.md                 # This file.

---

## How It Works: From Earth Data to Actionable Insights

### 1. Data Sourcing and Processing
- **Source:** NASA TEMPO Level-3 satellite data.
- **Processing:** AWS cloud-based processing avoids downloading massive datasets.
- **Efficiency:** Users access only processed, relevant AQI information in real-time.

### 2. Custom API
- Bridges NASA data and web front-end.
- Calculates AQI metrics and serves them through structured endpoints.

### 3. Predictive Machine Learning Model
- Built using **VARIMA (Vector Autoregressive Integrated Moving Average)**.
- Trained on **10+ years of atmospheric data**.
- Provides **48-hour AQI forecasts**.

### 4. User Interface (Front End)
- Clean, intuitive web viewer.
- Visualizations: Maps, charts, and forecasts.
- Designed for **ease of understanding** for non-experts.

---

## Benefits & Intended Impact

- **Accessibility:** One-stop platform for reliable AQI data.
- **Actionable Information:** Helps plan activities, reduce pollution exposure.
- **Educational Tool:** Raises awareness about air pollution and climate change.
- **Data Validity:** Uses official NASA datasets for scientific accuracy.

**Impact Goals:**
- Empower public with health information.
- Bridge gap between scientific data and general public.
- Encourage action against climate change.

---

## Technology & Tools

- **Cloud:** AWS (S3 for data storage, scalable computing for processing).
- **Data Source:** NASA TEMPO satellite mission.
- **Back End:** Python (xarray, netCDF4, scikit-learn/statsmodels), Flask/FastAPI.
- **Front End:** React, HTML, CSS, JavaScript.
- **Software Tools:** Jupyter Notebook, Git for version control.

---

## Creative Approach

- **Serverless Data Pipeline:** In-cloud processing avoids latency and duplication.
- **Visualization + Prediction:** Integrates forward-looking AQI predictions.
- **Human-Centered Design:** Intuitive interface for non-experts.

**Team Considerations:**
- Prioritized **user experience** and **data integrity**.
- Designed for **scalability** and efficient cloud processing.
- Focused on solving the **awareness gap** in air quality data.

---

## Challenges & Solutions

- **Data Size:** NASA datasets are huge (NetCDF/HDF5).
  - **Solution:** Cloud-native processing on AWS.
- **Model Accuracy:** Predicting AQI is complex.
  - **Solution:** VARIMA trained on 10 years of data.
- **User Experience:** Presenting complex data clearly.
  - **Solution:** Clear visual cues, color-coded AQI levels, interactive maps.

---

## Future Work

- Expand data sources (e.g., VIIRS, MODIS).
- Forecast additional pollutants (SO₂, CO, etc.).
- Extend prediction horizon (72h or 1 week).
- Real-time event detection (e.g., wildfire smoke).
- Mobile notifications and personalized alerts.
- Dashboard for policymakers and researchers.
- Citizen science integration for user-submitted data.

---

## License & Acknowledgements

- **License:** MIT License (or specify your preferred open-source license)
- **Credits:** Team Return (0)
- **NASA Space Apps Challenge 2025:** Participation for AQI Awareness challenge.
- **Data:** NASA TEMPO satellite mission.
- **Special Thanks:** Mentors, organizers, and everyone supporting the challenge.

---

**Note:** All files, scripts, and models include headers stating they were generated with the help of AI, in compliance with best practices for AI-assisted development.

---

**Enjoy exploring AQI Awareness Viewer! 🌱**