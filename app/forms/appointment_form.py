from flask_wtf import FlaskForm
from wtforms.validators import Optional


from wtforms import (
    StringField,
    IntegerField,
    SelectField,
    DateField,
    TimeField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    NumberRange,
    Regexp,
    Optional
)

from datetime import date

from wtforms import ValidationError


class AppointmentForm(FlaskForm):

    # ---------------------------------------
    # Patient Details
    # ---------------------------------------

    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    age = IntegerField(
        "Age",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=120)
        ]
    )

    gender = SelectField(
        "Gender",
        choices=[
            ("", "Select Gender"),
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ],
        validators=[DataRequired()]
    )

    mobile = StringField(
        "Mobile Number",
        validators=[
            DataRequired(),
            Regexp(
                r'^[6-9]\d{9}$',
                message="Enter a valid 10-digit Indian mobile number."
            )
        ]
    )

    email = StringField(
    "Email Address (Optional)",
    validators=[
        Optional(),
        Email(message="Please enter a valid email address.")
    ]
)
    # ---------------------------------------
    # Appointment Details
    # ---------------------------------------

    appointment_type = SelectField(
        "Appointment Type",
        choices=[
            ("", "Select Appointment Type"),
            ("Consultation", "Consultation"),
            ("Follow-up", "Follow-up"),
            ("Home Visit", "Home Visit")
        ],
        default="Consultation",
        validators=[Optional()]
    )

    preferred_doctor = SelectField(
        "Preferred Doctor",
        choices=[
            ("", "Select Doctor"),
            ("Dr. J.Ashok kumar", "Dr. J.Ashok kumar"),
            ("Dr. Name","Dr. Name")
        ],
        default="Dr. J.Ashok kumar",
        validators=[Optional()]
    )

    preferred_date = DateField(
        "Preferred Date",
        format="%Y-%m-%d",
        validators=[DataRequired()]
    )

    # Hour (01–12)
    hour = SelectField(
        "Hour",
        choices=[
            (f"{i:02d}", f"{i:02d}")
            for i in range(0, 13)
        ],
        validators=[DataRequired()]
    )

    # Minute (00–59)
    minute = SelectField(
        "Minute",
        choices=[
            (f"{i:02d}", f"{i:02d}")
            for i in range(0, 60)
        ],
        validators=[DataRequired()]
    )

    # AM / PM
    period = SelectField(
        "AM/PM",
        choices=[
            ("AM", "AM"),
            ("PM", "PM")
        ],
        validators=[DataRequired()]
    )

    problem = TextAreaField(
        "Problem Description (optional)",
        validators=[
            Optional(), 
            Length(min=0, max=500)
        ]
    )

    submit = SubmitField("Book Appointment")

    # ---------------------------------------
    # Custom Validators
    # ---------------------------------------

    def validate_preferred_date(self, field):

        if field.data < date.today():

            raise ValidationError(
                "Appointment date cannot be in the past."
            )