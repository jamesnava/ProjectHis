import conect_bd

class Querys(object):

	def __init__(self):
		obj_conectar=conect_bd.Conexion()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()

		#Conexion a sisgalenplus.
		obj_conectargalen=conect_bd.ConexionGalen()
		obj_conectargalen.ejecutar_conn()
		self.cursor_galen=obj_conectargalen.get_cursor()

	def query_User(self,user,password):
		rows=[]
		sql=f"""SELECT * FROM USUARIO AS U INNER JOIN MEDICO AS M ON M.DNI=U.DNI AND U.USUARIO='{user}' AND U.CONTRASENIA='{password}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows	
		
	def query_Medico(self,dni):		
		rows=[]
		sql=f"""SELECT * FROM MEDICO INNER JOIN SERVICIO ON MEDICO.CODSERVICIO=SERVICIO.CODSERVICIO AND DNI='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def insert_HISCABE(self,datos):
		sql=f"""INSERT INTO HIS_CAB VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
		return self.cursor.rowcount

	def consultar_Hoja(self,dni):
		rows=[]
		sql=f"""SELECT * FROM HIS_CAB WHERE FECHA=CONVERT(DATE,GETDATE(),102) AND DNI='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def row_codigoHISCABE(self,codigo):
		rows=[]
		sql=f"""SELECT * FROM HIS_CAB WHERE CODCABECERA='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def Hojas_HIS(self,dni,servicio):
		rows=[]
		sql=f"""SELECT * FROM HIS_CAB AS H INNER JOIN MEDICO AS M ON H.DNI=M.DNI INNER JOIN 
		SERVICIO AS S ON M.CODSERVICIO=S.CODSERVICIO AND H.FECHA=CONVERT(DATE,GETDATE(),102) AND S.CODSERVICIO='{servicio}' AND H.DNI='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_cie10(self,descrip):
		rows=[]
		sql=f"""SELECT * FROM CIE WHERE NOMBRE LIKE '%{descrip}%'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_cie10Param(self,codigo):
		rows=[]
		sql=f"""SELECT * FROM CIE WHERE CODCIE='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_idMAXHIS_DETA(self):
		rows=[]
		sql=f"""SELECT MAX(ID_DETA) AS codigo FROM HIS_DETA"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def insert_HISDETA(self,id_deta,datos):				
		sql=f"""INSERT INTO HIS_DETA VALUES({id_deta},'{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}','{datos[5]}','{datos[6]}','{datos[7]}',
		'{datos[8]}','{datos[9]}','{datos[10]}','{datos[11]}','{datos[12]}','{datos[13]}','{datos[14]}','{datos[15]}','{datos[16]}','{datos[17]}')"""
		self.cursor.execute(sql)		
		self.cursor.commit()
		

	



