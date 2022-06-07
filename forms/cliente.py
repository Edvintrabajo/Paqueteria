from wtforms import Form, StringField, SubmitField, validators

class RegistrationForm(Form):
    
    dni = StringField('DNI', [validators.Length(9)], default='Introduce el DNI')
    nombre = StringField('Nombre', [validators.Length(min=4, max=20)], default='Introduce el Nombre')
    apellido = StringField('Apellido', [validators.Length(min=4, max=30)], default='Introduce el Apellido')
    direccion = StringField('Direccion', [validators.Length(min=4, max=50)], default='Introduce el Direccion')
    save = SubmitField('Guardar')
    cancel = SubmitField('Cancelar')