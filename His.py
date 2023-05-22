import Consulta_doc
from tkinter import messagebox
from tkinter import *
import random
from tkinter import ttk
from datetime import date
import Consulta_Galen
import Operaciones

class HIS(object):
	
	def __init__(self):
		self.obj_consultas=Consulta_doc.Querys()
		self.obj_consultaGalen=Consulta_Galen.QuerysG()
		self.obj_operaciones=Operaciones.operaciones()		
	
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
	def Top_InsertarData(self,ventana,codigo,servicio):
		self.codigo_HISCABE=codigo
		self.codigo_servicio=servicio
		font1=('Comic Sans MS',12,'bold')
		self.TopInsert=Toplevel(ventana)
		self.TopInsert.geometry("950x700")
		self.TopInsert.title("Ingresar Pacientes")
		self.TopInsert.iconbitmap("image/paciente.ico")
		self.TopInsert.resizable(0,0)
		self.TopInsert.grab_set()
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")

		etiqueta=Label(self.TopInsert,text="DNI PACIENTE :",font=font1)
		etiqueta.grid(row=1,column=0)
		self.dni_p=StringVar()	

		self.entry_DniPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry",textvariable=self.dni_p)
		self.entry_DniPaciente.grid(row=1,column=1,columnspan=3,pady=5)
		self.entry_DniPaciente.bind("<Return>",lambda event:self.event_searchPaciente(event))
		
		etiqueta=Label(self.TopInsert,text="NOMBRES :",font=font1)
		etiqueta.grid(row=1,column=4)	

		self.entry_NombrePaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_NombrePaciente.grid(row=1,column=5,columnspan=3,pady=5)
	
		etiqueta=Label(self.TopInsert,text="APELLIDOS :",font=font1)
		etiqueta.grid(row=2,column=0)	

		self.entry_ApellidosPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_ApellidosPaciente.grid(row=2,column=1,columnspan=3,pady=5)	

		etiqueta=Label(self.TopInsert,text="HISTORIA CL. :",font=font1)
		etiqueta.grid(row=2,column=4)	

		self.entry_HistoriaPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_HistoriaPaciente.grid(row=2,column=5,columnspan=3,pady=5)

		etiqueta=Label(self.TopInsert,text="FINANCIAMIENTO :",font=font1)
		etiqueta.grid(row=3,column=0)
		self.combo_financiamiento=ttk.Combobox(self.TopInsert,width=30,style="MyEntry.TEntry",values=['SIS','PARTICULAR','SALUDPOL','OTRO'],state='readonly')
		self.combo_financiamiento.current(0)
		self.combo_financiamiento.grid(row=3,column=1,columnspan=3,pady=5)	

		etiqueta=Label(self.TopInsert,text="ETNIA:",font=font1)
		etiqueta.grid(row=3,column=4)
		self.entry_EtniaPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_EtniaPaciente.grid(row=3,column=5,columnspan=3,pady=5)

		etiqueta=Label(self.TopInsert,text="GENERO :",font=font1)
		etiqueta.grid(row=4,column=0)
		self.entry_GENERO=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_GENERO.grid(row=4,column=1,columnspan=3,pady=5)

		etiqueta=Label(self.TopInsert,text="EDAD:",font=font1)
		etiqueta.grid(row=4,column=4)
		self.entry_EdadPaciente=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_EdadPaciente.grid(row=4,column=5,columnspan=3,pady=5)

		etiqueta=Label(self.TopInsert,text="Distrito Proc.:",font=font1)
		etiqueta.grid(row=5,column=0)
		self.entry_DistritoProcedencia=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_DistritoProcedencia.grid(row=5,column=1,columnspan=3,pady=5)

		etiqueta=Label(self.TopInsert,text="CT. POBLADO:",font=font1)
		etiqueta.grid(row=5,column=4)
		self.entry_CentroPoblado=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry")
		self.entry_CentroPoblado.grid(row=5,column=5,columnspan=3,pady=5)

		marco_perimetro=LabelFrame(self.TopInsert,text="Perimetro y cefálico abdominal",font=("Helvetica",11,"italic"))
		marco_perimetro.grid(row=6,column=0,columnspan=5,padx=5)

		etiqueta=Label(marco_perimetro,text="PC:",font=font1)
		etiqueta.grid(row=1,column=1)
		self.entry_PC=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_PC.grid(row=1,column=2,columnspan=2,pady=5)

		etiqueta=Label(marco_perimetro,text="Pab:",font=font1)
		etiqueta.grid(row=1,column=4)
		self.entry_Pab=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_Pab.grid(row=1,column=5,columnspan=2,pady=5)


		marco_perimetro=LabelFrame(self.TopInsert,text="Evaluacion Antrometrica Hemoglobina",font=("Helvetica",11,"italic"))
		marco_perimetro.grid(row=7,column=0,columnspan=9,padx=5)

		etiqueta=Label(marco_perimetro,text="Peso:",font=font1)
		etiqueta.grid(row=1,column=1)
		self.entry_peso=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_peso.grid(row=1,column=2,columnspan=2,pady=5)

		etiqueta=Label(marco_perimetro,text="Talla:",font=font1)
		etiqueta.grid(row=1,column=4)
		self.entry_talla=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_talla.grid(row=1,column=5,columnspan=2,pady=5)

		etiqueta=Label(marco_perimetro,text="Hb:",font=font1)
		etiqueta.grid(row=1,column=7)
		self.entry_Hb=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_Hb.grid(row=1,column=8,columnspan=2,pady=5)

		etiqueta=Label(self.TopInsert,text="Establecimiento:",font=font1)
		etiqueta.grid(row=8,column=0)
		self.entry_Establecimiento=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry",state="readonly")		
		self.entry_Establecimiento.grid(row=8,column=1,columnspan=2,pady=5)

		etiqueta=Label(self.TopInsert,text="Servicio:",font=font1)
		etiqueta.grid(row=8,column=4)
		self.entry_Servicio=ttk.Entry(self.TopInsert,width=30,style="MyEntry.TEntry",state="readonly")		
		self.entry_Servicio.grid(row=8,column=5,columnspan=2,pady=5)

		marco_perimetro=LabelFrame(self.TopInsert,text="Diagnosticos",font=("Helvetica",11,"italic"))
		marco_perimetro.grid(row=9,column=0,columnspan=12,padx=5)

		etiqueta=Label(marco_perimetro,text="CIE:",font=font1)
		etiqueta.grid(row=1,column=1)
		self.entry_CIE=ttk.Entry(marco_perimetro,width=20,style="MyEntry.TEntry")
		self.entry_CIE.bind("<Return>",self.fill_DX)
		self.entry_CIE.grid(row=1,column=2,columnspan=2,pady=5)

		etiqueta=Label(marco_perimetro,text="Descripcion:",font=font1)
		etiqueta.grid(row=1,column=4)
		self.entry_Descripcion=ttk.Entry(marco_perimetro,width=30,style="MyEntry.TEntry")
		self.entry_Descripcion.grid(row=1,column=5,columnspan=2,pady=5)
		self.entry_Descripcion.bind("<Return>",self.Top_searchCie)

		etiqueta=Label(marco_perimetro,text="Tipo Dx:",font=font1)
		etiqueta.grid(row=1,column=7)
		self.entry_tipoDX=ttk.Combobox(marco_perimetro,width=10,values=["P","D","R"],state="readonly")
		self.entry_tipoDX.current(0)
		self.entry_tipoDX.grid(row=1,column=8,columnspan=2,pady=5)

		etiqueta=Label(marco_perimetro,text="LAB:",font=font1)
		etiqueta.grid(row=1,column=10)
		self.entry_LAB=ttk.Entry(marco_perimetro,width=10,style="MyEntry.TEntry")
		self.entry_LAB.grid(row=1,column=11,columnspan=2,pady=5)

		btn_addDX=ttk.Button(marco_perimetro,width=15,text="Agregar")
		btn_addDX['command']=self.Insertar_diagnosticos
		btn_addDX.grid(row=2,column=4)

		btn_quitDX=ttk.Button(marco_perimetro,width=15,text="Quitar")
		btn_quitDX["command"]=self.delete_tableSelected
		btn_quitDX.grid(row=2,column=6)


		self.table_datos=ttk.Treeview(marco_perimetro,height=5,columns=('#1','#2','#3','#4'),show='headings')	

		self.table_datos.heading("#1",text="CIE10")
		self.table_datos.column("#1",width=100,anchor="w",stretch='NO')	
		self.table_datos.heading("#2",text="DESCRIPCION")
		self.table_datos.column("#2",width=300,anchor="w",stretch='NO')
		self.table_datos.heading("#3",text="TIPO DX")
		self.table_datos.column("#3",width=200,anchor="w",stretch='NO')
		self.table_datos.heading("#4",text="LAB")
		self.table_datos.column("#4",width=100,anchor="w",stretch='NO')				
		self.table_datos.grid(row=3,column=0,columnspan=20) 
		self.table_datos.configure(height=5)

		btn_addDatos=ttk.Button(marco_perimetro,width=15,text="Agregar")
		btn_addDatos["command"]=self.insertData
		btn_addDatos.grid(row=5,column=4)
		btn_cancleDatos=ttk.Button(marco_perimetro,width=15,text="Cancelar")		
		btn_cancleDatos.grid(row=5,column=6)

	def delete_tableSelected(self):
		try:
			selected_item = self.table_datos.selection()[0]
			self.table_datos.delete(selected_item)	
		except Exception as e:
			messagebox.showinfo("Alerta","Seleccione un Item")		

	def event_searchPaciente(self,event):
		dni=self.entry_DniPaciente.get()
		today = date.today()
		rows=self.obj_consultaGalen.query_Paciente(dni)				
		if len(dni)>0:
			try:
				self.delete_Entrys()
				rows=self.obj_consultaGalen.query_Paciente(dni)								
				self.entry_NombrePaciente.insert(0,rows[0].PrimerNombre)
				self.entry_ApellidosPaciente.insert(0,rows[0].ApellidoPaterno+" "+rows[0].ApellidoMaterno)
				self.entry_HistoriaPaciente.insert(0,rows[0].NroHistoriaClinica)
				self.entry_GENERO.insert(0,rows[0].Descripcion)
				self.entry_EtniaPaciente.insert(0,rows[0].IdEtnia)
				self.entry_DistritoProcedencia.insert(0,rows[0].Nombre)
				fechanacimiento=rows[0].FECHANACIMIENTO				
				edad=int(today.year)-int(fechanacimiento[:4])
				self.entry_EdadPaciente.insert(0,edad)
				establecimiento,servicio=self.obj_operaciones.VEstablecimiento(dni,self.codigo_servicio)
				
				self.entry_Establecimiento.insert(0,establecimiento)
				self.entry_Establecimiento["state"]="readonly"

				
				self.entry_Servicio.insert(0,servicio)
				self.entry_Servicio["state"]="readonly"
			except Exception as e:
				messagebox.showerror("Alerta",f"error {e}")
		else:
			messagebox.showinfo("Alerta","Ingrese el DNI")
	def delete_Entrys(self):
		self.entry_NombrePaciente["state"]="normal"
		self.entry_NombrePaciente.delete(0,"end")
		self.entry_ApellidosPaciente["state"]="normal"
		self.entry_ApellidosPaciente.delete(0,"end")
		self.entry_HistoriaPaciente["state"]="normal"
		self.entry_HistoriaPaciente.delete(0,"end")
		self.entry_GENERO["state"]="normal"
		self.entry_GENERO.delete(0,"end")
		self.entry_EtniaPaciente["state"]="normal"
		self.entry_EtniaPaciente.delete(0,"end")
		self.entry_DistritoProcedencia["state"]="normal"
		self.entry_DistritoProcedencia.delete(0,"end")
		self.entry_Establecimiento["state"]="normal"
		self.entry_Establecimiento.delete(0,"end")
		self.entry_Servicio["state"]="normal"
		self.entry_Servicio.delete(0,"end")
		self.entry_EdadPaciente["state"]="normal"
		self.entry_EdadPaciente.delete(0,"end")

	def Top_searchCie(self,event):
		self.TopCIE=Toplevel(self.TopInsert)
		self.TopCIE.title('Diagnosticos')		
		self.TopCIE.geometry("720x400+350+50")
		self.TopCIE.focus_set()	
		self.TopCIE.grab_set()
		self.TopCIE.resizable(0,0)	
		self.TopCIE.iconbitmap('image/diagnostico.ico')

		label_title=Label(self.TopCIE,text='Buscar')
		label_title.place(x=20,y=20)
		self.Entry_buscar_General=ttk.Entry(self.TopCIE,width=30)
		self.Entry_buscar_General.focus()
		self.Entry_buscar_General.place(x=80,y=20)
		self.Entry_buscar_General.bind('<Key>',self.buscar_cie)		

		#tabla...
		self.table_CIE=ttk.Treeview(self.TopCIE,columns=('#1','#2'),show='headings')		
		self.table_CIE.heading("#1",text="CODIGO")
		self.table_CIE.column("#1",width=80,anchor="center")
		self.table_CIE.heading("#2",text="CIE")
		self.table_CIE.column("#2",width=200,anchor="center")										
		self.table_CIE.place(x=10,y=70,width=700,height=290)
		self.table_CIE.bind('<<TreeviewSelect>>',self.itemTable_selected)
	def buscar_cie(self,event):
		self.borrar_tabla()
		parametro=''		
		if len(self.Entry_buscar_General.get())!=0:
			parametro=parametro+self.Entry_buscar_General.get()
			rows=self.obj_consultas.query_cie10(parametro)
			for valores in rows:
				self.table_CIE.insert('','end',values=(valores.CODCIE,valores.NOMBRE))	

	def borrar_tabla(self):
		for item in self.table_CIE.get_children():
			self.table_CIE.delete(item)
	def itemTable_selected(self,event):
		if len(self.table_CIE.focus())!=0:
			self.entry_CIE.delete(0,'end')
			self.entry_CIE.insert(0,self.table_CIE.item(self.table_CIE.selection()[0],option='values')[0])
			self.entry_Descripcion.delete(0,'end')
			self.entry_Descripcion.insert(0,self.table_CIE.item(self.table_CIE.selection()[0],option='values')[1])
			self.entry_LAB.delete(0,"end")
		self.TopCIE.destroy()

	def fill_DX(self,event):
		param=self.entry_CIE.get()
		rows=self.obj_consultas.query_cie10Param(param)
		if len(rows)>0:
			self.entry_Descripcion.delete(0,'end')
			self.entry_Descripcion.insert(0,rows[0].NOMBRE)
		else:
			messagebox.showerror("Alerta","Datos no Encontrados")
			self.entry_CIE.delete(0,'end')
			self.entry_Descripcion.delete(0,'end')
	def Insertar_diagnosticos(self):
		codigo_cie=self.entry_CIE.get()
		descripcion=self.entry_Descripcion.get()
		tipo=self.entry_tipoDX.get()
		lab=self.entry_LAB.get()
		tabladatos=self.diagnosticos_data()
		aux=False
		if len(tabladatos)>0:			
			for i in range(len(tabladatos)):
				if tabladatos[i][0]==codigo_cie:
					aux=True
					break

		if not aux:
			self.table_datos.insert("",'end',values=(codigo_cie,descripcion,tipo,lab))
		else:
			messagebox.showerror("Alerta","el diagnostico ya existe!!")

	def insertData(self):
		#recuperando valores
		dni_p=self.entry_DniPaciente.get()
		nombre_p=self.entry_NombrePaciente.get()
		apellidos_p=self.entry_ApellidosPaciente.get()
		hcl_p=self.entry_HistoriaPaciente.get()
		financiamiento_p=self.combo_financiamiento.get()
		Etnia_p=self.entry_EtniaPaciente.get()
		distritopro_p=self.entry_DistritoProcedencia.get()
		centrop_p=self.entry_CentroPoblado.get()
		edad_p=self.entry_EdadPaciente.get()
		sexo_p=self.entry_GENERO.get()
		pab_p=self.entry_Pab.get()
		Establecimiento_p=self.entry_Establecimiento.get()
		servicio_p=self.entry_Servicio.get()
		codcabecera_p=self.codigo_HISCABE
		peso_p=self.entry_peso.get()
		talla_p=self.entry_talla.get()
		hb_p=self.entry_Hb.get()
		pc_p=self.entry_PC.get()
		datos=[dni_p,nombre_p,apellidos_p,hcl_p,financiamiento_p,Etnia_p,distritopro_p,centrop_p,edad_p,sexo_p,pab_p,Establecimiento_p,servicio_p,codcabecera_p,peso_p,talla_p,hb_p,pc_p]
		idrows=self.obj_consultas.query_idMAXHIS_DETA()
		id_deta=0
		if idrows[0].codigo!=None:
			id_deta=idrows[0].codigo+1
		else:
			id_deta=1		
		try:
			#comprobar la existencia
			existencia_paciente=self.obj_consultas.exist_Paciente(self.codigo_HISCABE,dni_p)	
			if len(existencia_paciente)==0:				
				rows_diagnosticos=self.diagnosticos_data()
				if len(rows_diagnosticos)>0:
					nro=self.obj_consultas.insert_HISDETA(id_deta,datos)
					for i in range(len(rows_diagnosticos)):				
						rows_DIAGNOSTICO=self.obj_consultas.query_idMAX_DIAGNOSTICOS()
						if rows_DIAGNOSTICO[0].codigo!=None:
							id_diag=rows_DIAGNOSTICO[0].codigo+1
						else:
							id_diag=1			
						self.obj_consultas.insert_DIAGNOSTICOS(id_diag,id_deta,rows_diagnosticos[i])
						self.TopInsert.destroy()					
					messagebox.showinfo("Alerta","Se insertó correctamente")
				else:
					messagebox.showerror("Alerta","Al menos inserte un diagnostico")
			else:
				messagebox.showerror("Alerta","ya se registro al paciente!!")
				self.TopInsert.destroy()

		except Exception as e:
			messagebox.showerror("error!!",e)

	def diagnosticos_data(self):
		diagnosticos=[]
		for item in self.table_datos.get_children():
			valores=self.table_datos.item(item)["values"]
			diagnosticos.append(valores)
		return diagnosticos

	def Top_EditarData(self,codigo,ventana):
		font1=('Comic Sans MS',12,'bold')
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")
		rows=self.obj_consultas.Query_HisDeta(codigo)
		self.Top_Editar=Toplevel(ventana)
		self.Top_Editar.geometry("750x600")
		self.Top_Editar.title("Datos de Paciente")
		self.Top_Editar.iconbitmap('img/paciente.ico')
		self.Top_Editar.resizable(0,0)
		self.Top_Editar.grab_set()

		label=Label(self.Top_Editar,text="DATOS DEL PACIENTE A MODIFICAR",font=font1)	
		label.grid(row=1,column=2,columnspan=3)
		
		label=Label(self.Top_Editar,text="DNI.........:",font=font1)	
		label.grid(row=2,column=2)
		label_dni=Label(self.Top_Editar,text=f"{rows[0].DNI_PAC}")
		label_dni.grid(row=2,column=3,sticky=W)

		label=Label(self.Top_Editar,text="HCL:",font=font1)	
		label.grid(row=2,column=4)
		label_nombre=Label(self.Top_Editar,text=f"{rows[0].HCL}")
		label_nombre.grid(row=2,column=5,sticky=W)	

		label=Label(self.Top_Editar,text="PACIENTE:",font=font1)	
		label.grid(row=3,column=2)
		label_nombre=Label(self.Top_Editar,text=f"{rows[0].NOMBRE} {rows[0].APELLIDOS}")
		label_nombre.grid(row=3,column=3,sticky=W)

		marco_perimetro=LabelFrame(self.Top_Editar,text="Datos",font=("Helvetica",11,"italic"),width=200)
		marco_perimetro.grid(row=4,column=0,columnspan=7,padx=5)

		label=Label(marco_perimetro,text="PC",font=font1)
		label.grid(row=1,column=1)

		Entry_PC=ttk.Entry(marco_perimetro,width=15,style="MyEntry.TEntry")
		Entry_PC.insert(0,rows[0].PC)
		Entry_PC.grid(row=1,column=2,pady=5)	

		label=Label(marco_perimetro,text="Pab",font=font1)
		label.grid(row=1,column=3)

		Entry_Pab=ttk.Entry(marco_perimetro,width=15,style="MyEntry.TEntry")
		Entry_Pab.insert(0,rows[0].PAB)
		Entry_Pab.grid(row=1,column=4,pady=5)

		label=Label(marco_perimetro,text="Peso",font=font1)
		label.grid(row=2,column=1)

		Entry_Peso=ttk.Entry(marco_perimetro,width=15,style="MyEntry.TEntry")
		Entry_Peso.insert(0,rows[0].Peso)
		Entry_Peso.grid(row=2,column=2,pady=5)	

		label=Label(marco_perimetro,text="Talla",font=font1)
		label.grid(row=2,column=3)

		Entry_Talla=ttk.Entry(marco_perimetro,width=15,style="MyEntry.TEntry")
		Entry_Talla.insert(0,rows[0].Talla)
		Entry_Talla.grid(row=2,column=4,pady=5)

		label=Label(marco_perimetro,text="HB",font=font1)
		label.grid(row=2,column=5)

		Entry_Hb=ttk.Entry(marco_perimetro,width=15,style="MyEntry.TEntry")
		Entry_Hb.insert(0,rows[0].Hb)
		Entry_Hb.grid(row=2,column=6,pady=5)


		self.table_editar=ttk.Treeview(self.Top_Editar,height=5,columns=('#1','#2','#3','#4','#5'),show='headings')	

		self.table_editar.heading("#1",text="ID")
		self.table_editar.column("#1",width=50,anchor="w",stretch='NO')
		self.table_editar.heading("#2",text="DESCRIPCION")
		self.table_editar.column("#2",width=250,anchor="w",stretch='NO')	
		self.table_editar.heading("#3",text="Tipo DX")
		self.table_editar.column("#3",width=80,anchor="w",stretch='NO')
		self.table_editar.heading("#4",text="LAB")
		self.table_editar.column("#4",width=80,anchor="w",stretch='NO')
		self.table_editar.heading("#5",text="CIE")
		self.table_editar.column("#5",width=80,anchor="w",stretch='NO')				
		self.table_editar.grid(row=7,column=0,columnspan=20)
		self.table_editar.bind("<Double-Button-1>",self.top_EditarCie) 
		self.table_editar.configure(height=5)
		id_detalle=rows[0].ID_DETA
		self.llenar_EditaDiagnostico(id_detalle)

		btn_guardar=ttk.Button(self.Top_Editar,width=10,text="Grabar")
		#error here
		btn_guardar["command"]=lambda:self.Update_Deta(codigo,Entry_PC.get(),Entry_Pab.get(),Entry_Peso.get(),Entry_Talla.get(),Entry_Hb.get())
		btn_guardar.grid(row=9,column=3,pady=5)
	def Update_Deta(self,codigo,pc,pab,peso,talla,hb):

		iden=self.table_editar.get_children()
		dat=[]
		for a in iden:
			datos=self.table_editar.item(a)["values"]			
			self.obj_consultas.Update_diagnostico(datos)

		nro=self.obj_consultas.Update_DetalleHis(codigo,pc,pab,peso,talla,hb)
		if nro>0:
			messagebox.showinfo('Alerta','Successful!')
			self.Top_Editar.destroy()

	def top_EditarCie(self,event):
		self.top_EditarC=Toplevel(self.Top_Editar)
		self.top_EditarC.title("Buscar Diagnostico")
		self.top_EditarC.iconbitmap('img/buscar.ico')
		self.top_EditarC.geometry("700x100")
		self.top_EditarC.resizable(0,0)
		self.top_EditarC.grab_set()

		itemTable=self.table_editar.selection()[0]
		id_diagnostico=self.table_editar.item(self.table_editar.selection()[0])['values'][0]
	

		label=Label(self.top_EditarC,text="CIE")
		label.grid(row=1,column=1)
		self.cie_entryEditar=ttk.Entry(self.top_EditarC,width=15)
		self.cie_entryEditar.bind("<Return>",self.fill_DXv2)
		self.cie_entryEditar.grid(row=1,column=2)

		label=Label(self.top_EditarC,text="Descripcion")
		label.grid(row=1,column=3)
		self.Descripcion_entryEditar=ttk.Entry(self.top_EditarC,width=30)
		self.Descripcion_entryEditar.grid(row=1,column=4)

		label=Label(self.top_EditarC,text="Tipo")
		label.grid(row=1,column=5)
		self.Tipo_entryEditar=ttk.Combobox(self.top_EditarC,width=15,values=["P","D","R"])
		self.Tipo_entryEditar.current(0)
		self.Tipo_entryEditar.grid(row=1,column=6)

		label=Label(self.top_EditarC,text="Lab")
		label.grid(row=1,column=7)
		self.Lab_entryEditar=ttk.Entry(self.top_EditarC,width=15)
		self.Lab_entryEditar.grid(row=1,column=8)

		button_GrabarDX=ttk.Button(self.top_EditarC,text="Aceptar")
		button_GrabarDX["command"]=lambda:self.insert_TablaEditar(itemTable,id_diagnostico)

		button_GrabarDX.grid(row=2,column=4,pady=5)

	def insert_TablaEditar(self,itemTable,id_diagnostico):
		codigo_cie=self.cie_entryEditar.get()
		descripcionDX=self.Descripcion_entryEditar.get()
		tipoDx=self.Tipo_entryEditar.get()
		lab=self.Lab_entryEditar.get()

		self.table_editar.insert('','end',values=(id_diagnostico,descripcionDX,tipoDx,lab,codigo_cie))
		self.top_EditarC.destroy()
		self.Top_Editar.grab_set()
		self.table_editar.delete(itemTable)
		
				
	def fill_DXv2(self,event):
		param=self.cie_entryEditar.get()
		rows=self.obj_consultas.query_cie10Param(param)

		try:
			self.Descripcion_entryEditar.delete(0,'end')
			self.Descripcion_entryEditar.insert(0,rows[0].NOMBRE)
		except Exception as e:
			messagebox.showerror("Alerta","Datos no Encontrados")			
			self.top_EditarC.destroy()
			self.Top_Editar.grab_set()		

	def llenar_EditaDiagnostico(self,iddeta):
		rows=self.obj_consultas.query_DIAGNOSTICOS(iddeta)
		for data in rows:
			self.table_editar.insert('','end',values=(data.Id_Diagnostico,data.Descripcion,data.TipDx,data.Lab,data.CODCIE))
		

			
		