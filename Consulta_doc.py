import conect_bd

class Querys(object):

	def __init__(self):
		obj_conectar=conect_bd.Conexion()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	
		
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

	def Hojas_HIS(self):
		rows=[]
		sql=f"""SELECT * FROM HIS_CAB AS H INNER JOIN MEDICO AS M ON H.DNI=M.DNI INNER JOIN 
		SERVICIO AS S ON M.CODSERVICIO=S.CODSERVICIO AND H.FECHA=CONVERT(DATE,GETDATE(),102) AND S.CODSERVICIO='00001'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows


