from base64 import b64encode
from io import BytesIO
from os import path

from flask import Flask
from flask import make_response
from flask import render_template
from flask_wtf import FlaskForm
from png import Writer
from wtforms import BooleanField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
with open(path.join(app.root_path, 'secret_key'), 'rb') as f:
    app.config['SECRET_KEY'] = f.read()


class IndexForm(FlaskForm):
    width = IntegerField(label='가로', validators=[DataRequired()])
    height = IntegerField(label='세로', validators=[DataRequired()])
    data_uri = BooleanField(label='data-uri')


def build_image(w, h):
    with BytesIO() as image:
        palette = [(0xFF, 0xFF, 0xFF, 0x00)]
        writer = Writer(w, h, palette=palette, bitdepth=1, compression=9)
        writer.write(image, [[0 for _ in range(w)] for _ in range(h)])
        image.seek(0)
        return image.read()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit():
        image = build_image(form.width.data, form.height.data)
        if form.data_uri.data:
            return 'data:image/png;base64,' + b64encode(image).decode()
        else:
            res = make_response(image)
            res.headers['Content-Type'] = 'image/png'
            res.headers['Content-Disposition'] = 'attachment; filename={}x{}.png'.format(form.width.data,
                                                                                         form.height.data)
            return res
    return render_template('index.html', form=form)
