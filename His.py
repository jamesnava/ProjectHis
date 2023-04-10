import Consulta_doc
from tkinter import messagebox
import random

class HIS(object):
	
	def __init__(self):
		self.obj_consultas=Consulta_doc.Querys()
		
	
	def medico_return(self,dni):
		try:
			rows=self.obj_consultas.query_Medico(dni)
			return rows
		except Exception as e:
			messagebox.showerror("Alerta","Datos no encontrados!!")

	def codigo_His_generar(self):		
		letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z','1','2','3','4','5','6','7','8','9','0']
		letra=''
		for i in range(0,5):
			letra+=letras[random.randint(0,len(letras)-1)]

		return letra

	def insertar_HISCAB(self,datos):
		rows=self.obj_consultas.consultar_Hoja('10126550')
		manana=0
		tarde=0
		for valor in rows:
			if valor.TURNO=="TARDE":
				tarde+=1
			elif valor.TURNO=="MAÑANA":
				manana+=1

		print(datos[3])
		if manana==0 and tarde==1:
			#nro=self.obj_consultas.insert_HISCABE(datos)
			#return nro
			pass
		elif tarde==0:
			pass

	def codigo_valido(self):
		codigo=""
		while True:
			cod=self.codigo_His_generar()
			rows=self.obj_consultas.row_codigoHISCABE(cod)
			if len(rows)==0:
				codigo=cod
				break
		return codigo

	def Hojas_HIS(self):
		rows=self.obj_consultas.Hojas_HIS()
		return rows

			

		
		
