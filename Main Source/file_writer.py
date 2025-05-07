import os
import datetime


def setup():
    if not os.path.exists("Reports"):
        os.mkdir("Reports")

def writeReport():
    date = datetime.datetime.now()
    filename = date.strftime("Reports/%m_%d_%Y_%H_%M_report.txt")
    with open(filename, "w") as file:
        file.write(f"Activity detected on motion sensor at {date.strftime('%H:%M:%S:%f')[:-3]} on {date.strftime('%m/%d/%Y')}")