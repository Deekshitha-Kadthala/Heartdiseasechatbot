from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_FOLDER, exist_ok=True)

def generate_report(prediction, confidence):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"report_{timestamp}.pdf"

    filepath = os.path.join(
        REPORT_FOLDER,
        filename
    )

    pdf = canvas.Canvas(
        filepath,
        pagesize=letter
    )

    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(
        120,
        750,
        "Heart Disease Detection Report"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        700,
        f"Prediction: {prediction}"
    )

    pdf.drawString(
        50,
        670,
        f"Confidence: {confidence}%"
    )

    pdf.drawString(
        50,
        640,
        f"Generated: {datetime.now()}"
    )

    pdf.save()

    return filepath