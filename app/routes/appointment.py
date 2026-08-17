from flask import Blueprint, render_template, redirect
from urllib.parse import quote

from app.forms.appointment_form import AppointmentForm

appointment = Blueprint("appointment", __name__)

# ----------------------------------------------------
# CHANGE THIS TO YOUR CLINIC'S WHATSAPP NUMBER
# Format: CountryCode + Number (No +, No spaces)
# Example: 919876543210
# ----------------------------------------------------

WHATSAPP_NUMBER = "918056209884"


@appointment.route("/appointment", methods=["GET", "POST"])
def book_appointment():

    form = AppointmentForm()

    if form.validate_on_submit():

        email = form.email.data.strip() if form.email.data else "Not Provided"

        preferred_time = (
            f"{form.hour.data}:"
            f"{form.minute.data} "
            f"{form.period.data}"
        )

        message = f"""
Hello Ashok,

I would like to book an appointment.

Name: {form.full_name.data}
Age: {form.age.data}
Gender: {form.gender.data}
Phone: {form.mobile.data}
Email: {email}

Appointment Type: {form.appointment_type.data}
Preferred Doctor: {form.preferred_doctor.data}
Preferred Date: {form.preferred_date.data.strftime('%d-%m-%Y')}
Preferred Time: {preferred_time}

Problem:
{form.problem.data if form.problem.data else "Not Provided"}

Please confirm my appointment.

Thank you.
"""

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
        )

        return redirect(whatsapp_url)

    return render_template(
        "appointment/appointment.html",
        form=form
    )