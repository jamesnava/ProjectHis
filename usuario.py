import Consulta_doc
import GUI_User

class usuario(object):
	def __init__(self):
		self.obj_queryUser=Consulta_doc.querys()
		self.conectado=False
		self.obj_user=GUI_User.Usuario()
	def conectar(self,usuario,contra):		
		rows=self.obj_queryUser.query_User(usuario,contra)		
		identificador=-1
		user=""		
		estado=""
		servicio=""
		dni=""	
		if len(rows)!=0:
			identificador=1
			for val in rows:
				user=val.USUARIO				
				estado=val.ESTADO
				servicio=val.CODSERVICIO
				dni=val.DNI

		else:
			identificador=-1
		return identificador,user,estado,servicio,dni

