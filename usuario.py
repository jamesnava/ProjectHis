import Consulta_doc


class usuario(object):
	def __init__(self):
		self.obj_queryUser=Consulta_doc.Querys()
		self.conectado=False
		
	def conectar(self,usuario,contra):		
		rows=self.obj_queryUser.query_User(usuario,contra)		
		identificador=-1
		user=""		
		estado=""
		servicio=""
		dni=""
		rol=""	
		if len(rows)!=0:
			identificador=1
			for val in rows:
				estado=val.ESTADO
				user=val.USUARIO				
				servicio=val.CODSERVICIO
				dni=val.DNI
				rol=val.ROL
		else:
			identificador=-1
		return identificador,user,estado,servicio,dni,rol

