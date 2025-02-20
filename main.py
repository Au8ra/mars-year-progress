from fastapi import FastAPI
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

app = FastAPI()

MARS_YEAR_DAYS = 687
START_DATE = datetime(2024, 12, 26)

def get_mars_progress():
    today = datetime.utcnow()
    elapsed_days = (today - START_DATE).days % MARS_YEAR_DAYS
    progress = (elapsed_days / MARS_YEAR_DAYS) * 100
    return round(progress, 2), elapsed_days

def generate_progress_bar(progress, elapsed_days):
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.barh(0, progress, color='red', height=0.4)
    ax.set_xlim(0, 100)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.text(50, 0, f"Mars Year 37 is {progress}% complete", ha="center", va="center", color="white", fontsize=14)
    filename = "progress.png"
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.1, dpi=100, facecolor="black")
    plt.close()
    return filename

@app.get("/mars/progress")
def get_progress():
    progress, elapsed_days = get_mars_progress()
    filename = generate_progress_bar(progress, elapsed_days)
    return {"progress": f"{progress}%", "elapsed_days": elapsed_days, "image": filename}
