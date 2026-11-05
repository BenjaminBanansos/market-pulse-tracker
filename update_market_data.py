#!/usr/bin/env python3
"""
PulseTrade Radar Data Updater
Updates data/market_data.json with latest price levels, momentum surges, and scalp signals.
"""

import json
import os
import sys
from datetime import datetime, timezone

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "market_data.json")

def update_data(payload):
    payload["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Successfully updated {DATA_PATH} at {payload['last_updated']}")

if __name__ == "__main__":
    target_path = sys.argv[1] if (len(sys.argv) > 1 and os.path.exists(sys.argv[1])) else DATA_PATH
    if os.path.exists(target_path):
        with open(target_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        update_data(data)
    else:
        print(f"Data file not found at {target_path}")
