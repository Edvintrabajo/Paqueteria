from wtforms import Form, StringField, SubmitField, validators

class RegistrationForm(Form):
    
    dni = StringField('dni', [validators.Length(min=9, max=9), validators.DataRequired()], render_kw={"placeholder": "DNI"})
    nombre = StringField('nombre', [validators.Length(min=4, max=20), validators.DataRequired()], render_kw={"placeholder": "Nombre"})
    apellido = StringField('apellido', [validators.Length(min=4, max=30), validators.DataRequired()], render_kw={"placeholder": "Apellido"})
    direccion = StringField('direccion', [validators.Length(min=4, max=50), validators.DataRequired()], render_kw={"placeholder": "Direccion"})
    save = SubmitField('Guardar')