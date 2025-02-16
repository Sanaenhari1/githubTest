from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    """Form for user registration with validation rules."""
    
    username = StringField(
        "Username",
        validators=[DataRequired(message="Username is required."), Length(min=3, max=20, message="Username must be between 3 and 20 characters.")]
    )
    
    email_address = StringField(
        "Email Address",
        validators=[DataRequired(message="Email is required."), Email(message="Enter a valid email address.")]
    )
    
    password1 = PasswordField(
        "Password",
        validators=[DataRequired(message="Password is required."), Length(min=6, message="Password must be at least 6 characters long.")]
    )
    
    password2 = PasswordField(
        "Confirm Password",
        validators=[DataRequired(message="Password confirmation is required."), EqualTo('password1', message="Passwords must match.")]
    )
    
    submit = SubmitField("Register")
