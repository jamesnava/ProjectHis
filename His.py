import Consulta_doc
from tkinter import messagebox
from tkinter import *
import random
from tkinter import ttk

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

	def insertar_HISCAB(self,datos,dni,servicio):
		rows=self.obj_consultas.consultar_Hoja(dni)
		if datos[4]==dni:
			aux=True
			turnos=[val.TURNO for val in rows]
			if datos[3] in turnos:
				aux=False
			if aux:
				nro=self.obj_consultas.insert_HISCABE(datos)
				return nro
			else:
				messagebox.showinfo("Alerta","Superó la Cantidad de Hojas permitidas")
		else:
			messagebox.showerror("Alerta","Datos no corresponden")

	def codigo_valido(self):
		codigo=""
		while True:
			cod=self.codigo_His_generar()
			rows=self.obj_consultas.row_codigoHISCABE(cod)
			if len(rows)==0:
				codigo=cod
				break
		return codigo

	def Hojas_HIS(self,dni,servicio):
		rows=self.obj_consultas.Hojas_HIS(dni,servicio)
		return rows
	def Top_InsertarData(self,ventana,codigo):
		font1=('Comic Sans MS',12,'bold')
		self.TopInsert=Toplevel(ventana)
		self.TopInsert.geometry("800x700")
		self.TopInsert.title("Ingresar Pacientes")
		self.TopInsert.grab_set()
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")

		etiqueta=Label(self.TopInsert,text="DNI PACIENTE :",font=font1)
		etiqueta.grid(row=1,column=0)	

		self.entry_DniPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_DniPaciente.grid(row=1,column=2,columnspan=2,pady=5)
		
		etiqueta=Label(self.TopInsert,text="NOMBRES :",font=font1)
		etiqueta.grid(row=1,column=4)	

		self.entry_NombrePaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_NombrePaciente.grid(row=1,column=5,columnspan=2,pady=5)
	
		etiqueta=Label(self.TopInsert,text="APELLIDOS :",font=font1)
		etiqueta.grid(row=2,column=0)	

		self.entry_ApellidosPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_ApellidosPaciente.grid(row=2,column=2,columnspan=2,pady=5)	

		etiqueta=Label(self.TopInsert,text="HISTORIA CL. :",font=font1)
		etiqueta.grid(row=2,column=4)	

		self.entry_HistoriaPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_HistoriaPaciente.grid(row=2,column=5,columnspan=2,pady=5)

		etiqueta=Label(self.TopInsert,text="FINANCIAMIENTO :",font=font1)
		etiqueta.grid(row=3,column=0)
		self.combo_financiamiento=ttk.Combobox(self.TopInsert,width=30,style="MyEntry.TEntry",values=['SIS','PARTICULAR','SALUDPOL','OTRO'],state='readonly')
		self.combo_financiamiento.current(0)
		self.combo_financiamiento.grid(row=3,column=2,columnspan=2,pady=5)	

		etiqueta=Label(self.TopInsert,text="ETNIA:",font=font1)
		etiqueta.grid(row=3,column=4)
		self.entry_EtniaPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_EtniaPaciente.grid(row=3,column=5,columnspan=2,pady=5)

		etiqueta=Label(self.TopInsert,text="GENERO :",font=font1)
		etiqueta.grid(row=4,column=0)
		self.entry_GENERO=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_GENERO.grid(row=4,column=1,columnspan=2,pady=5)
		
