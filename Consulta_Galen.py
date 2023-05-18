import conect_bd

class QuerysG(object):

	def __init__(self):
		#Conexion a sisgalenplus.
		obj_conectargalen=conect_bd.ConexionGalen()
		obj_conectargalen.ejecutar_conn()
		self.cursor_galen=obj_conectargalen.get_cursor()

	def query_Paciente(self,dni):
		rows=[]
		sql=f"""SELECT P.NroDocumento,P.PrimerNombre,P.ApellidoPaterno,P.ApellidoMaterno,P.NroHistoriaClinica,CONVERT(DATE,P.FechaNacimiento,102) 
		AS FECHANACIMIENTO,TS.Descripcion,D.Nombre,D.IdDistrito,P.IdEtnia FROM Pacientes AS P INNER JOIN TiposSexo AS TS  ON TS.IdTipoSexo=P.IdTipoSexo INNER JOIN Distritos
		AS D ON P.IdDistritoProcedencia=D.IdDistrito AND P.NroDocumento='{dni}'"""
		self.cursor_galen.execute(sql)
		rows=self.cursor_galen.fetchall()
		return rows
#:::::::::::::::::consulta especialistas::::::::::::::::
	def Especialista(self,dni):
		rows=[]
		sql=f"""SELECT Nombres,ApellidoPaterno,ApellidoMaterno FROM Empleados WHERE DNI='{dni}'"""
		self.cursor_galen.execute(sql)
		rows=self.cursor_galen.fetchall()
		return rows

