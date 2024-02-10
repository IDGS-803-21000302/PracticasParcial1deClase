from wtforms import Form
from wtforms import StringField, SelectField,RadioField,EmailField,IntegerField

class NumsFrom(Form):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')


class resistenciasForm(Form):
    primeraBanda = SelectField('primeraBanda',choices=[('negro', 'Negro'), ('cafe', 'Cafe'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])
    segundaBanda = SelectField('segundaBanda',choices=[('negro', 'Negro'), ('cafe', 'Cafe'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])
    terceraBanda = SelectField('terceraBanda',choices=[('negro', 'Negro'), ('cafe', 'Cafe'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])
    tolerancia = RadioField('tolerancia',choices=[('oro','Oro'),('plata','Plata')])