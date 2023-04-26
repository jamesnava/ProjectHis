from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
from tkcalendar import Calendar,DateEntry
import His
from tkinter import messagebox


class Ventana(object):
	
	def __init__(self,usuario,servicio,dni):
		self.usuario_=usuario
		self.servicio_=servicio
		self.dni_=dni


		self.obj_his=His.HIS()
		self.codigo_servicio=None
		#self.Ventana_Main=Tk()
		
		self.Ventana_Main=ThemedTk(theme='radiance')
		self.Ventana_Main.title("Ventana Principal")
		self.height=int(self.Ventana_Main.winfo_screenheight()*0.90)
		self.width=int(self.Ventana_Main.winfo_screenwidth()*0.90)
		self.Ventana_Main.geometry("%dx%d" % (self.width,self.height)+"+0+0")
		self.Ventana_Main.resizable(0,0)

		self.Barra_Menu=Menu(self.Ventana_Main)
		self.Ventana_Main['menu']=self.Barra_Menu

		self.M_Configuracion=Menu(self.Barra_Menu,tearoff=False)
		self.M_Configuracion.add_command(label='Restablecer Contraseña')
		self.M_Configuracion.add_command(label='Minimizar',command=self.Ventana_Main.iconify)
		self.M_Configuracion.add_command(label='Cerrar',command=self.Ventana_Main.destroy)
		self.M_Configuracion.add_separator()		
		self.Barra_Menu.add_cascade(label='Archivo',menu=self.M_Configuracion)
		#creando menu configuracion
		self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)
		self.M_Usuario.add_command(label='Agregar Especialistas')
		self.M_Usuario.add_command(label='Listar Especialistas')		
		self.M_Usuario.add_separator()		
		self.Barra_Menu.add_cascade(label='Especialistas',menu=self.M_Usuario)

		# creando menu Acciones
		self.M_Acciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Acciones.add_command(label='Insertar His',command=self.Frame_NewHIS)
		self.M_Acciones.add_command(label='Bandeja de Entrada',)				
		self.M_Acciones.add_command(label='Seguimiento')
		self.M_Acciones.add_command(label='Historial de Documentos')		
		self.M_Acciones.add_separator()		
		self.Barra_Menu.add_cascade(label='His Minsa',menu=self.M_Acciones)				
		#Ayuda...
		self.M_Ayuda=Menu(self.Barra_Menu,tearoff=False)
		self.M_Ayuda.add_command(label='Acerca de...')
		self.M_Ayuda.add_command(label='Desarrollado por...')		
		self.M_Ayuda.add_separator()		
		self.Barra_Menu.add_cascade(label='Ayuda',menu=self.M_Ayuda)		
		self.Ventana_Main.mainloop()

	def Frame_NewHIS(self):
		self.frame_HIS=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.frame_HIS.place(x=0,y=0)
		font=('Comic Sans MS',18,'bold')
		etiqueta=Label(self.frame_HIS,text="GENERAR HOJA DE ATENCION HIS",font=font)
		etiqueta.grid(row=0,column=0,columnspan=6,sticky='e')
		font1=('Comic Sans MS',12,'bold')

		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")

		etiqueta=Label(self.frame_HIS,text="DNI MEDICO:",font=font1)
		etiqueta.grid(row=1,column=0)
	
		#
		self.entry_Dni=ttk.Entry(self.frame_HIS,width=30,style="MyEntry.TEntry")
		self.entry_Dni.grid(row=1,column=2,columnspan=2,pady=5)
		self.entry_Dni.bind("<Button>",self.event_focus)
		self.entry_Dni.bind("<Return>",self.data_cabecera)
		

		etiqueta=Label(self.frame_HIS,text="Medico :",font=font1)
		etiqueta.grid(row=1,column=4)
		self.entry_Medico=ttk.Entry(self.frame_HIS,width=30,style="MyEntry.TEntry")
		self.entry_Medico.grid(row=1,column=5,columnspan=2,pady=5)

		etiqueta=Label(self.frame_HIS,text="Servicio :",font=font1)
		etiqueta.grid(row=2,column=0)
		self.entry_Servicio=ttk.Entry(self.frame_HIS,width=30,style="MyEntry.TEntry")
		self.entry_Servicio.grid(row=2,column=2,columnspan=2,pady=5)

		#evento buscar medico		

		etiqueta=Label(self.frame_HIS,text="Establecimiento :",font=font1)
		etiqueta.grid(row=2,column=4)
		self.entry_Establecimiento=ttk.Entry(self.frame_HIS,width=30,style="MyEntry.TEntry")
		self.entry_Establecimiento.grid(row=2,column=5,columnspan=2,pady=5)
		self.entry_Establecimiento.insert(0,"Hospital sub Regional de Andahuaylas")
		self.entry_Establecimiento.configure(state="readonly")

		etiqueta=Label(self.frame_HIS,text="Fecha :",font=font1)
		etiqueta.grid(row=3,column=0)
		self.dateCalendar=StringVar()
		self.calendar=DateEntry(self.frame_HIS,selectmode='day',textvariable=self.dateCalendar,date_pattern="dd/mm/yy")
		self.calendar.grid(row=3,column=2)

		etiqueta=Label(self.frame_HIS,text="Turno :",font=font1)
		etiqueta.grid(row=3,column=4)
		self.combo_turno=ttk.Combobox(self.frame_HIS,width=30,style="MyEntry.TEntry",values=['MAÑANA','TARDE'],state='readonly')
		self.combo_turno.current(0)
		self.combo_turno.grid(row=3,column=5,columnspan=2,pady=5)

		Btn_Aceptar=ttk.Button(self.frame_HIS,text='Aceptar',cursor="hand2")
		Btn_Aceptar["command"]=self.datos_HISCAB
		Btn_Aceptar.grid(row=4,column=2)

		Btn_Cancelar=ttk.Button(self.frame_HIS,text='Cancelar',cursor="hand2")
		Btn_Cancelar.grid(row=4,column=5)

		font=('Comic Sans MS',18,'bold')
		etiqueta=Label(self.frame_HIS,text="HOJAS DE ATENCION",font=font)
		etiqueta.grid(row=5,column=0,columnspan=6,sticky='e')

		self.table_Hojas=ttk.Treeview(self.frame_HIS,height=5,columns=('#1','#2','#3','#4','#5','#6'),show='headings')
		

		self.table_Hojas.heading("#1",text="CODIGO")
		self.table_Hojas.column("#1",width=100,anchor="w",stretch='NO')	
		self.table_Hojas.heading("#2",text="MEDICO")
		self.table_Hojas.column("#2",width=300,anchor="w",stretch='NO')
		self.table_Hojas.heading("#3",text="ESTABLECIMIENTO")
		self.table_Hojas.column("#3",width=200,anchor="w",stretch='NO')
		self.table_Hojas.heading("#4",text="TURNO")
		self.table_Hojas.column("#4",width=100,anchor="w",stretch='NO')
		self.table_Hojas.heading("#5",text="SERVICIO")
		self.table_Hojas.column("#5",width=250,anchor="w",stretch='NO')
		self.table_Hojas.heading("#6",text="FECHA")
		self.table_Hojas.column("#6",width=250,anchor="w",stretch='NO')			
		self.table_Hojas.grid(row=6,column=0,columnspan=20) 
		self.table_Hojas.configure(height=15)
		self.llenar_table()


		Btn_Editar=ttk.Button(self.frame_HIS,text='Editar',cursor="hand2")
		Btn_Editar.grid(row=8,column=2)

		Btn_Insertar=ttk.Button(self.frame_HIS,text='Insertar Datos',cursor="hand2")
		Btn_Insertar["command"]=self.Insert_Data
		Btn_Insertar.grid(row=8,column=4)

		Btn_Eliminar=ttk.Button(self.frame_HIS,text='Eliminar',cursor="hand2")
		Btn_Eliminar.grid(row=8,column=6)

	def Insert_Data(self):
		if self.table_Hojas.selection():
			codigo=self.table_Hojas.item(self.table_Hojas.selection()[0])['values'][0]
			self.obj_his.Top_InsertarData(self.Ventana_Main,codigo,self.servicio_)
			
		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!")
		

	def datos_HISCAB(self):
		datos=[]
		codigo=self.obj_his.codigo_valido()		
		fecha=self.dateCalendar.get()
		self.entry_Establecimiento.configure(state="normal")
		Establecimiento=self.entry_Establecimiento.get()
		turno=self.combo_turno.get()		
		datos.append(codigo)
		datos.append(fecha)
		datos.append(Establecimiento)
		datos.append(turno)
		datos.append(self.dni_medico)		
		nro=self.obj_his.insertar_HISCAB(datos,self.dni_,self.servicio_)
		self.llenar_table()
		if nro==1:
			messagebox.showinfo("Alerta","Se insertó correctamente!!")
			self.Delete_()

		else:
			messagebox.showinfo("Alerta","No pudo agregarse!!")


	def data_cabecera(self,event):
		self.dni_medico=self.entry_Dni.get()		
		rows=self.obj_his.medico_return(self.dni_medico)
		if len(rows)>0:
			self.entry_Medico.insert(0,rows[0].NOMBRES+" "+rows[0].APELLIDOP+" "+rows[0].APELLIDOM)
			self.entry_Servicio.insert(0,rows[0].NOMBRE)
			self.codigo_servicio=rows[0].CODSERVICIO
		else:
			messagebox.showinfo("Notificacion","DNI NO ENCONTRADO")

	def llenar_table(self):		
		for item in self.table_Hojas.get_children():
			self.table_Hojas.delete(item)

		rows=self.obj_his.Hojas_HIS(self.dni_,self.servicio_)
		for valores in rows:
			self.table_Hojas.insert("","end",values=(valores.CODCABECERA,valores.NOMBRES+" "+ valores.APELLIDOP+" "+valores.APELLIDOM,valores.ESTABLECIMIENTO,valores.TURNO,valores.NOMBRE,valores.FECHA))
		
	def event_focus(self,event):
		self.entry_Dni.delete(0,"end")
		self.entry_Medico["state"]="normal"
		self.entry_Medico.delete(0,"end")
		self.entry_Servicio["state"]="normal"
		self.entry_Servicio.delete(0,"end")

	def Delete_(self):
		self.entry_Dni.delete(0,"end")
		self.entry_Medico["state"]="normal"
		self.entry_Medico.delete(0,"end")
		self.entry_Servicio["state"]="normal"
		self.entry_Servicio.delete(0,"end")
	
	

