import conect_bd
from tkinter import messagebox

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

	def query_idMAX_DIAGNOSTICOS(self):
		rows=[]
		sql=f"""SELECT MAX(Id_Diagnostico) AS codigo FROM DIAGNOSTICOS"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def insert_DIAGNOSTICOS(self,id_DIAGNOSTICO,id_deta,datos):				
		sql=f"""INSERT INTO DIAGNOSTICOS VALUES({id_DIAGNOSTICO},'{datos[1]}','{datos[2]}','{datos[3]}','{datos[0]}',{id_deta})"""
		self.cursor.execute(sql)		
		self.cursor.commit()

	def exist_Paciente(self,codigo_cabe,dni):
		rows=[]
		sql=f"""SELECT HD.DNI_PAC FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON 
		HC.CODCABECERA=HD.CODCABECERA AND HC.CODCABECERA='{codigo_cabe}' AND HD.DNI_PAC='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	#comprobar la existencia de un paciente
	def existencia_pacienteBD(self,dni):
		rows=[]
		sql=f"""SELECT HD.DNI_PAC FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON 
		HC.CODCABECERA=HD.CODCABECERA AND HD.DNI_PAC='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def existencia_pacienteBDAnio(self,dni):
		rows=[]
		sql=f"""SELECT HD.DNI_PAC FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON HC.CODCABECERA=HD.CODCABECERA AND
		 HD.DNI_PAC='{dni}' AND YEAR(HC.FECHA)=YEAR(GETDATE())"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def existencia_pacienteBDServicio(self,dnipaciente,servicio):
		rows=[]
		sql=f"""SELECT YEAR(FECHA) AS fecha FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON HC.CODCABECERA=HD.CODCABECERA INNER JOIN MEDICO AS M 
		ON HC.DNI=M.DNI AND HD.DNI_PAC='{dnipaciente}' AND M.CODSERVICIO='{servicio}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def existencia_pacienteBDServicioAnio(self,dnipaciente,servicio):
		rows=[]
		sql=f"""SELECT YEAR(FECHA) AS fecha FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON HC.CODCABECERA=HD.CODCABECERA INNER JOIN MEDICO AS M 
		ON HC.DNI=M.DNI AND HD.DNI_PAC='{dnipaciente}' AND M.CODSERVICIO='{servicio}' AND YEAR(HC.FECHA)=YEAR(GETDATE())"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_DIAGNOSTICOS(self,iddeta):
		rows=[]
		sql=f"""SELECT * FROM DIAGNOSTICOS WHERE ID_DETA={iddeta}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def datos_Hoja(self,codigo):
		rows=[]
		sql=f"""SELECT * FROM HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON HC.CODCABECERA=HD.CODCABECERA AND HC.CODCABECERA='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def datos_HojaV2(self,codigo):
		rows=[]
		sql=f"""SELECT HC.CODCABECERA,HC.FECHA,HC.ESTABLECIMIENTO,HC.TURNO,HC.DNI,HD.ID_DETA,HD.DNI_PAC,HD.NOMBRE,HD.APELLIDOS,HD.HCL,
		        HD.FINACIAMIENTO,HD.ETNIA,HD.DISTRITOPRO,HD.EDAD,HD.SEXO,HD.PAB,HD.ESTABLEC,HD.SERVICIO,HD.Peso,
				HD.Talla,HD.Hb,HD.PC,M.DNI,M.NOMBRES,M.APELLIDOP,M.APELLIDOM,S.NOMBRE AS NOMBSERVICIO FROM 
				HIS_CAB AS HC INNER JOIN HIS_DETA AS HD ON HC.CODCABECERA=HD.CODCABECERA INNER JOIN MEDICO 
				AS M ON HC.DNI=M.DNI INNER JOIN SERVICIO AS S ON S.CODSERVICIO=M.CODSERVICIO  AND HC.CODCABECERA='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def delete_deta(self,iddeta):
		try:
			sql=f"""DELETE FROM HIS_DETA WHERE ID_DETA={iddeta}"""
			self.cursor.execute(sql)
			self.cursor.commit()
			return self.cursor.rowcount
		except Exception as e:
			messagebox.showerror("Notificacion",f"No pudo realizarse la operacion {e}")

	def Query_HisDeta(self,iddeta):
		try:
			rows=[]
			sql=f"""SELECT * FROM HIS_DETA WHERE ID_DETA={iddeta}"""
			self.cursor.execute(sql)
			rows=self.cursor.fetchall()
			return rows
		except Exception as e:
			raise e
		

	def delete_diagnostico(self,iddeta):
		try:
			sql=f"""DELETE FROM DIAGNOSTICOS WHERE ID_DETA={iddeta}"""
			self.cursor.execute(sql)
			self.cursor.commit()
			return self.cursor.rowcount
		except Exception as e:
			messagebox.showerror("Alerta",f"No pudo realizarse la operacion!! {e}")

	def Update_diagnostico(self,datos):
		
		try:
			sql=f"""UPDATE DIAGNOSTICOS SET Descripcion='{datos[1]}',TipDx='{datos[2]}',Lab='{datos[3]}',CODCIE='{datos[4]}' WHERE Id_Diagnostico={datos[0]}"""
			self.cursor.execute(sql)
			self.cursor.commit()
			
		except Exception as e:
			messagebox.showerror("Alerta",f"No pudo Ejecutarse D...! {e}")
	def Update_DetalleHis(self,codigo,pc,pab,peso,talla,hb):
		try:
			sql=f"""UPDATE HIS_DETA SET PC='{pc}',Hb='{hb}',Talla='{talla}',Peso='{peso}',PAB={pab} WHERE ID_DETA={codigo}"""
			self.cursor.execute(sql)
			self.cursor.commit()
			return self.cursor.rowcount			
		except Exception as e:
			messagebox.showerror("Alerta",f"No pudo Ejecutarse...! {e}")

	def Servicios(self):
		try:
			rows=[]
			sql=f"""SELECT * FROM SERVICIO"""
			self.cursor.execute(sql)
			rows=self.cursor.fetchall()
			return rows
		except Exception as e:
			messagebox.showerror("Alerta",f"{e}")

	def ServiciosVar(self,servicio,fecha):
		try:
			rows=[]
			sql=f"""SELECT * FROM HIS_CAB AS HC INNER JOIN MEDICO AS M ON HC.DNI=M.DNI AND HC.FECHA='{fecha}' AND CODSERVICIO='{servicio}'"""
			self.cursor.execute(sql)
			rows=self.cursor.fetchall()
			return rows
		except Exception as e:
			messagebox.showerror("Alerta",f"{e}")

		

	



