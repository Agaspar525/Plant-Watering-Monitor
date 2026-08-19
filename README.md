# Plant Watering Monitor

A desktop GUI application that simulates a soil moisture sensor and helps track when plants need watering.

## Features
- Simulates a moisture sensor reading (0–100 scale)
- Automatically flags when a plant needs water (below 30% moisture)
- Lets the user "water" the plant with one click when needed
- Logs every watering event (plant name, moisture level, date) to a CSV file for history tracking

## Built With
- Python
- PyQt6 (GUI)
- CSV (data logging)

## How to Run
1. Install dependencies: `pip install PyQt6`
2. Run: `python main.py`
