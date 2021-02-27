from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    image = FileField('Image Upload', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Invalid file type, please try again'])
    ])
