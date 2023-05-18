from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
from tkcalendar import Calendar,DateEntry
import His
import Consulta_doc
import Consulta_Galen
import reporte
from tkinter import messagebox


class Ventana(object):
	
	def __init__(self,usuario,servicio,dni,rol):
		self.usuario_=usuario
		self.servicio_=servicio
		self.dni_=dni
		self.rol=rol

		self.obj_his=His.HIS()
		self.obj_consult=Consulta_doc.Querys()
		self.obj_consultaGalen=Consulta_Galen.QuerysG()
		self.codigo_servicio=None
		#self.Ventana_Main=Tk()
		
		self.Ventana_Main=ThemedTk(theme='radiance')
		self.Ventana_Main.title("Ventana Principal")
		self.height=int(self.Ventana_Main.winfo_screenheight()*0.90)
		self.width=int(self.Ventana_Main.winfo_screenwidth()*0.80)
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
		if self.rol=="ADMINISTRADOR":
			self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)		
			self.M_Usuario.add_command(label='Especialistas',command=self.Frame_Especialistas)		
			self.M_Usuario.add_separator()
			self.M_Usuario.add_command(label='Usuarios',command=self.Frame_Usuarios)			
			self.Barra_Menu.add_cascade(label='Configuraciones',menu=self.M_Usuario)

		# creando menu Acciones
		self.M_Acciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Acciones.add_command(label='Insertar His',command=self.Frame_NewHIS)
		if self.rol=="ADMINISTRADOR":
			self.M_Acciones.add_command(label='Ver Hojas',command=self.Frame_ListaHojasHis)			
		self.M_Acciones.add_separator()		
		self.Barra_Menu.add_cascade(label='His Minsa',menu=self.M_Acciones)				
		#Ayuda...
		self.M_Ayuda=Menu(self.Barra_Menu,tearoff=False)
		self.M_Ayuda.add_command(label='Acerca de...',command=self.acercaDe_)
		self.M_Ayuda.add_command(label='Desarrollado por...',command=self.Author_)		
		self.M_Ayuda.add_separator()		
		self.Barra_Menu.add_cascade(label='Ayuda',menu=self.M_Ayuda)		
		self.Ventana_Main.mainloop()

	def Frame_Usuarios(self):
		self.Frame_Usuario=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.Frame_Usuario.place(x=0,y=0)
		self.Frame_Usuario.grid_propagate(False)
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")

		font=('Comic Sans MS',18,'bold')
		label=Label(self.Frame_Usuario,text="DATOS DE LOS USUARIOS",font=font)
		label.grid(row=0,column=0,columnspan=10,pady=5)

		font1=('Comic Sans MS',12,'bold')
		label=Label(self.Frame_Usuario,text="BUSCAR :",font=font1)
		label.grid(row=1,column=0,pady=5)
		self.Entry_Buscar=ttk.Entry(self.Frame_Usuario,style="MyEntry.TEntry")
		self.Entry_Buscar.grid(row=1,column=1,pady=5)
		self.Entry_Buscar.bind("<Return>",lambda event: self.search_MUsuario(event))
		self.Entry_Buscar.bind("<Button-1>",self.delete_EntryUser)


		label=Label(self.Frame_Usuario,text="DNI :",font=font1)
		label.grid(row=1,column=2,pady=5)
		self.Entry_DNIUsuario=ttk.Entry(self.Frame_Usuario,style="MyEntry.TEntry")
		self.Entry_DNIUsuario.grid(row=1,column=3,pady=5)
		self.Entry_DNIUsuario["state"]="readonly"

		label=Label(self.Frame_Usuario,text="USUARIO :",font=font1)
		label.grid(row=1,column=4,pady=5)
		self.Entry_NickUsuario=ttk.Entry(self.Frame_Usuario,style="MyEntry.TEntry")
		self.Entry_NickUsuario.grid(row=1,column=5,pady=5)

		label=Label(self.Frame_Usuario,text="PASSWORD :",font=font1)
		label.grid(row=2,column=2,pady=5)
		self.Entry_ContraseniaUsuario=ttk.Entry(self.Frame_Usuario,style="MyEntry.TEntry")
		self.Entry_ContraseniaUsuario.grid(row=2,column=3,pady=5)

		label=Label(self.Frame_Usuario,text="ESTADO:",font=font1)
		label.grid(row=2,column=4,pady=5)
		self.Combo_EstadoUsuario=ttk.Combobox(self.Frame_Usuario,style="MyEntry.TEntry",values=['ACTIVO','INACTIVO'])
		self.Combo_EstadoUsuario.current(0)
		self.Combo_EstadoUsuario.grid(row=2,column=5,pady=5)

		label=Label(self.Frame_Usuario,text="ROL:",font=font1)
		label.grid(row=1,column=6,pady=5)
		self.Combo_RolUsuario=ttk.Combobox(self.Frame_Usuario,style="MyEntry.TEntry",values=['ADMINISTRADOR','CLIENTE'])
		self.Combo_RolUsuario.current(0)
		self.Combo_RolUsuario.grid(row=1,column=7,pady=5)

		bnt_addUser=ttk.Button(self.Frame_Usuario,text="Agregar Usuario")
		bnt_addUser['command']=self.insert_User	
		bnt_addUser.grid(row=3,column=4,pady=5)		

		self.table_Usuarios=ttk.Treeview(self.Frame_Usuario,height=5,columns=('#1','#2','#3'),show='headings')		
		self.table_Usuarios.heading("#1",text="DNI")
		self.table_Usuarios.column("#1",width=100,anchor="w",stretch='NO')	
		self.table_Usuarios.heading("#2",text="USUARIO")
		self.table_Usuarios.column("#2",width=300,anchor="w",stretch='NO')
		self.table_Usuarios.heading("#3",text="ESTADO")		
		self.table_Usuarios.column("#3",width=300,anchor="w",stretch='NO')	
		self.table_Usuarios.grid(row=6,column=0,columnspan=20,pady=5) 
		self.table_Usuarios.configure(height=15)
		self.fill_table()

		btn_Cambiar=ttk.Button(self.Frame_Usuario,text="Estado")
		btn_Cambiar.config(command=self.Update_UserState)
		btn_Cambiar.grid(row=8,column=2)

		btn_contrasenia=ttk.Button(self.Frame_Usuario,text="Cambiar Contraseña")
		btn_contrasenia["command"]=self.Update_UserPassword
		btn_contrasenia.grid(row=8,column=3)

	def Update_UserPassword(self):
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")
		if self.table_Usuarios.selection():
			dni=self.table_Usuarios.item(self.table_Usuarios.selection()[0])['values'][0]
			self.Top_UsuarioPASS=Toplevel(self.Ventana_Main)
			self.Top_UsuarioPASS.geometry("300x150")
			self.Top_UsuarioPASS.title("Modificar el Estado")
			self.Top_UsuarioPASS.resizable(0,0)
			self.Top_UsuarioPASS.grab_set()				
			etiqueta=Label(self.Top_UsuarioPASS,text="Contraseña: ")
			etiqueta.grid(row=1,column=0)
			self.Entry_UPassword=ttk.Entry(self.Top_UsuarioPASS,style="MyEntry.TEntry",show='*')
			self.Entry_UPassword.grid(row=1,column=1)			
			btn_UpdatePASS=ttk.Button(self.Top_UsuarioPASS,text="Aceptar")
			btn_UpdatePASS['command']=self.Update_Password		
			btn_UpdatePASS.grid(row=2,column=0,columnspan=2)
		else:
			messagebox.showerror("Notificación","Seleccione un ITEM!!")

	def Update_Password(self):
		dni=self.table_Usuarios.item(self.table_Usuarios.selection()[0])['values'][0]
		password=self.Entry_UPassword.get()
		self.obj_consult.Update_UserPassword(dni,password)
		self.Top_UsuarioPASS.destroy()

	def Update_UserState(self):
		if self.table_Usuarios.selection():
			dni=self.table_Usuarios.item(self.table_Usuarios.selection()[0])['values'][0]
			self.Top_Usuario=Toplevel(self.Ventana_Main)
			self.Top_Usuario.geometry("300x150")
			self.Top_Usuario.title("Modificar el Estado")
			self.Top_Usuario.resizable(0,0)
			self.Top_Usuario.grab_set()				
			etiqueta=Label(self.Top_Usuario,text="Estado: ")
			etiqueta.grid(row=1,column=0)
			self.combo_UpdateUsuario=ttk.Combobox(self.Top_Usuario,values=['ACTIVO','INACTIVO'])
			self.combo_UpdateUsuario.grid(row=1,column=1)			
			self.combo_UpdateUsuario.current(0)
			btn_UpdateUsuario=ttk.Button(self.Top_Usuario,text="Aceptar")
			btn_UpdateUsuario['command']=self.Update_State		
			btn_UpdateUsuario.grid(row=2,column=0,columnspan=2)
		else:
			messagebox.showerror("Notificación","Seleccione un ITEM!!")
	
	def Update_State(self):
		dni=self.table_Usuarios.item(self.table_Usuarios.selection()[0])['values'][0]
		estado=self.combo_UpdateUsuario.get()
		self.obj_consult.Update_User(dni,estado)
		self.Top_Usuario.destroy()

	def fill_table(self):
		rows=self.obj_consult.query_usuarios()
		for val in rows:
			self.table_Usuarios.insert("",'end',values=(val.DNI,val.USUARIO,val.ESTADO))		

	def insert_User(self):
		self.Entry_DNIUsuario.config(state="normal")
		dni=self.Entry_DNIUsuario.get()
		user=self.Entry_NickUsuario.get()
		passw=self.Entry_ContraseniaUsuario.get()
		estado_user=self.Combo_EstadoUsuario.get()
		rol=self.Combo_RolUsuario.get()

		rows_user=self.obj_consult.search_User(user)
		if not len(rows_user)>0:
			rows_userDni=self.obj_consult.search_UserDni(dni)
			if not len(rows_userDni)>0:
				self.obj_consult.insert_User(dni,user,passw,estado_user,rol)				
			else:
				messagebox.showerror("Alerta",f"{dni} ya tiene asignado un usuario")
		else:
			messagebox.showerror("Alerta","Elija otro Usuario, ya existe!!")


	def search_MUsuario(self,event):
		dni=self.Entry_Buscar.get()
		rows=self.obj_consult.query_Medico(dni)

		if len(rows)>0:
			self.Entry_DNIUsuario.config(state="normal")
			self.Entry_DNIUsuario.insert(0,rows[0].DNI)
			self.Entry_DNIUsuario.config(state="readonly")
		else:
			messagebox.showerror("Alerta","Datos no encontrados")

	def delete_EntryUser(self,event):

		self.Entry_Buscar.delete(0,"end")
		self.Entry_DNIUsuario.config(state="normal")
		self.Entry_DNIUsuario.delete(0,"end")
		self.Entry_DNIUsuario["state"]="readonly"
		self.Entry_NickUsuario.delete(0,"end")
		self.Entry_ContraseniaUsuario.delete(0,"end")

	def Frame_Especialistas(self):
		self.frame_Especialista=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.frame_Especialista.place(x=0,y=0)
		self.frame_Especialista.grid_propagate(False)
		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")

		font=('Comic Sans MS',18,'bold')
		label=Label(self.frame_Especialista,text="DATOS DEL ESPECIALISTA",font=font)
		label.grid(row=0,column=0,columnspan=10,pady=5)

		font1=('Comic Sans MS',12,'bold')
		label=Label(self.frame_Especialista,text="DNI :",font=font1)
		label.grid(row=1,column=0,pady=5)
		self.Entry_DNIEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_DNIEspecialista.grid(row=1,column=1,pady=5)
		self.Entry_DNIEspecialista.bind("<Return>",lambda event: self.filldata_Especialista(event))
		self.Entry_DNIEspecialista.bind("<Button-1>",self.delete_EntryEsp)

		label=Label(self.frame_Especialista,text="NOMBRES :",font=font1)
		label.grid(row=1,column=2,pady=5)
		self.Entry_NOMBREEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_NOMBREEspecialista.grid(row=1,column=3,pady=5)

		label=Label(self.frame_Especialista,text="APELLIDO PATERNO :",font=font1)
		label.grid(row=2,column=0,pady=5)
		self.Entry_APEELIDOPEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_APEELIDOPEspecialista.grid(row=2,column=1,pady=5)

		label=Label(self.frame_Especialista,text="APELLIDO MATERNO :",font=font1)
		label.grid(row=2,column=2,pady=5)
		self.Entry_APEELIDOMEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_APEELIDOMEspecialista.grid(row=2,column=3,pady=5)

		label=Label(self.frame_Especialista,text="TELEFONO:",font=font1)
		label.grid(row=1,column=4,pady=5)
		self.Entry_TELEFONOEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_TELEFONOEspecialista.grid(row=1,column=5,pady=5)

		label=Label(self.frame_Especialista,text="CORREO :",font=font1)
		label.grid(row=2,column=4,pady=5)
		self.Entry_CORREOEspecialista=ttk.Entry(self.frame_Especialista,style="MyEntry.TEntry")
		self.Entry_CORREOEspecialista.grid(row=2,column=5,pady=5)

		label=Label(self.frame_Especialista,text="ESPECIALIDAD :",font=font1)
		label.grid(row=3,column=0,pady=5)
		self.Combo_Especialidad=ttk.Combobox(self.frame_Especialista,width=25)
		self.Combo_Especialidad.grid(row=3,column=1,pady=5)
		self.filldata_Especialidad()
		self.Combo_Especialidad.current(0)
		btn_insertaEspecialista=ttk.Button(self.frame_Especialista,text="Insertar")	
		btn_insertaEspecialista["command"]=self.insert_Medico
		btn_insertaEspecialista.grid(row=4,column=2,pady=5)
		


		self.table_Especialista=ttk.Treeview(self.frame_Especialista,height=5,columns=('#1','#2','#3','#4'),show='headings')		
		self.table_Especialista.heading("#1",text="DNI")
		self.table_Especialista.column("#1",width=100,anchor="w",stretch='NO')	
		self.table_Especialista.heading("#2",text="NOMBRE")
		self.table_Especialista.column("#2",width=300,anchor="w",stretch='NO')
		self.table_Especialista.heading("#3",text="APELLIDO PATERNO")
		self.table_Especialista.column("#3",width=200,anchor="w",stretch='NO')
		self.table_Especialista.heading("#4",text="APELLIDO MATERNO")
		self.table_Especialista.column("#4",width=200,anchor="w",stretch='NO')
		self.table_Especialista.heading("#4",text="SERVICIO")
		self.table_Especialista.column("#4",width=200,anchor="w",stretch='NO')					
		self.table_Especialista.grid(row=6,column=0,columnspan=20,pady=5) 
		self.table_Especialista.configure(height=15)
		self.Llenar_TablaMedico()
		btn_ExportarData=ttk.Button(self.frame_Especialista,text="Editar")
		btn_ExportarData["command"]=self.Update_Especialista
		btn_ExportarData.grid(row=8,column=2)	



	def Update_Especialista(self):
		if self.table_Especialista.selection():
			dni=self.table_Especialista.item(self.table_Especialista.selection()[0])['values'][0]
			self.Top_Especialista=Toplevel(self.Ventana_Main)
			self.Top_Especialista.geometry("500x100")
			self.Top_Especialista.title("Modificar al medico")
			self.Top_Especialista.resizable(0,0)		
			etiqueta=Label(self.Top_Especialista,text="DNI: ")
			etiqueta.grid(row=1,column=0)
			self.entry_DniUpdate=ttk.Entry(self.Top_Especialista)
			self.entry_DniUpdate.insert(0,dni)
			self.entry_DniUpdate.grid(row=1,column=1)
			etiqueta=Label(self.Top_Especialista,text="Servicio: ")
			etiqueta.grid(row=1,column=2)
			self.combo_UpdateServicio=ttk.Combobox(self.Top_Especialista)
			self.combo_UpdateServicio.grid(row=1,column=3)
			self.LlenarComboEspecialista()
			self.combo_UpdateServicio.current(0)
			btn_UpdateServicio=ttk.Button(self.Top_Especialista,text="Aceptar")
			btn_UpdateServicio.config(command=self.Cambiar_Servicio)
			btn_UpdateServicio.grid(row=2,column=2)
		else:
			messagebox.showerror("Notificación","Seleccione un ITEM!!")

	def Cambiar_Servicio(self):
		dni=self.entry_DniUpdate.get()
		servicio=self.combo_UpdateServicio.get()[:self.combo_UpdateServicio.get().find("_")]
		self.obj_consult.Update_Especialista(dni,servicio)
		self.Top_Especialista.destroy()
	def LlenarComboEspecialista(self):
		rows=self.obj_consult.Servicios()
		valores=[]
		for val in rows:
			valores.append(val.CODSERVICIO+"_"+val.NOMBRE)
		self.combo_UpdateServicio["values"]=valores

	def Llenar_TablaMedico(self):		
		rows=self.obj_consult.query_Especialista()
		for val in rows:
			self.table_Especialista.insert("",'end',values=(val.DNI,val.NOMBRES,val.APELLIDOP+" "+val.APELLIDOM,val.NOMBRE))		

	def insert_Medico(self):			
		dni_Especialista=self.Entry_DNIEspecialista.get()
		nombre_Especialista=self.Entry_NOMBREEspecialista.get()
		apellidop_Especialista=self.Entry_APEELIDOPEspecialista.get()
		apellidom_Especialista=self.Entry_APEELIDOPEspecialista.get()
		telefono_Especialista=self.Entry_TELEFONOEspecialista.get()
		correo_Especialista=self.Entry_CORREOEspecialista.get()
		especialidad_Especialista=self.Combo_Especialidad.get()[:self.Combo_Especialidad.get().find("_")]
		if len(dni_Especialista)>0 and len(correo_Especialista)>0:
			self.obj_consult.insert_Especialista(dni_Especialista,nombre_Especialista,apellidop_Especialista,apellidom_Especialista,telefono_Especialista,correo_Especialista,especialidad_Especialista)
		else:
			messagebox.showinfo("Alerta","Rellene los campos")

		for item in self.table_Especialista.get_children():
			self.table_Especialista.delete(item)
		self.Llenar_TablaMedico()

	def filldata_Especialista(self,event):
		dni=self.Entry_DNIEspecialista.get()
		rows=self.obj_consultaGalen.Especialista(dni)		
		self.delete_EntryEspecialista()
		for val in rows:
			self.Entry_NOMBREEspecialista.insert(0,val.Nombres)
			self.Entry_APEELIDOPEspecialista.insert(0,val.ApellidoPaterno)
			self.Entry_APEELIDOMEspecialista.insert(0,val.ApellidoMaterno)
	def filldata_Especialidad(self):
		rows=self.obj_consult.Servicios()
		data=[]
		for val in rows:
			data.append(val.CODSERVICIO+"_"+val.NOMBRE)
		self.Combo_Especialidad["values"]=data

	def delete_EntryEsp(self,event):
		self.Entry_NOMBREEspecialista.delete(0,"end")
		self.Entry_APEELIDOPEspecialista.delete(0,"end")
		self.Entry_APEELIDOMEspecialista.delete(0,"end")
		self.Entry_TELEFONOEspecialista.delete(0,"end")
		self.Entry_CORREOEspecialista.delete(0,"end")

	def delete_EntryEspecialista(self):
		self.Entry_NOMBREEspecialista.delete(0,"end")
		self.Entry_APEELIDOPEspecialista.delete(0,"end")
		self.Entry_APEELIDOMEspecialista.delete(0,"end")
		self.Entry_TELEFONOEspecialista.delete(0,"end")
		self.Entry_CORREOEspecialista.delete(0,"end")

	def Frame_ListaHojasHis(self):
		self.frame_HojasHIS=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.frame_HojasHIS.place(x=0,y=0)
		self.frame_HojasHIS.grid_propagate(False)

		font=('Comic Sans MS',18,'bold')
		etiqueta=Label(self.frame_HojasHIS,text="LISTA DE HOJAS HIS",font=font)
		etiqueta.grid(row=0,column=0,columnspan=6,sticky='e')
		font1=('Comic Sans MS',12,'bold')

		etiqueta=Label(self.frame_HojasHIS,text="Fecha :")
		etiqueta.grid(row=4,column=2)

		self.dateL=StringVar()
		self.calendarL=DateEntry(self.frame_HojasHIS,selectmode='day',textvariable=self.dateL,date_pattern="dd/mm/yy")
		self.calendarL.grid(row=4,column=3)

		etiqueta=Label(self.frame_HojasHIS,text="Servicio :")
		etiqueta.grid(row=4,column=4)
	
		self.combo_ServicioL=ttk.Combobox(self.frame_HojasHIS)
		self.combo_ServicioL.grid(row=4,column=5)
		self.combo_ServicioL.bind("<<ComboboxSelected>>",self.event_ComboServicio)
		self.llenarcomboServicio()

		style=ttk.Style()
		style.configure("MyEntry.TEntry",padding=6,foreground="#0000ff")	

		self.TListaHojas=ttk.Treeview(self.frame_HojasHIS,height=5,columns=('#1','#2','#3','#4','#5','#6'),show='headings')
		
		self.TListaHojas.heading("#1",text="CODIGO")
		self.TListaHojas.column("#1",width=100,anchor="w",stretch='NO')	
		self.TListaHojas.heading("#2",text="MEDICO")
		self.TListaHojas.column("#2",width=300,anchor="w",stretch='NO')
		self.TListaHojas.heading("#3",text="ESTABLECIMIENTO")
		self.TListaHojas.column("#3",width=200,anchor="w",stretch='NO')
		self.TListaHojas.heading("#4",text="TURNO")
		self.TListaHojas.column("#4",width=100,anchor="w",stretch='NO')
		self.TListaHojas.heading("#5",text="SERVICIO")
		self.TListaHojas.column("#5",width=250,anchor="w",stretch='NO')
		self.TListaHojas.heading("#6",text="FECHA")
		self.TListaHojas.column("#6",width=250,anchor="w",stretch='NO')			
		self.TListaHojas.grid(row=6,column=0,columnspan=20) 
		self.TListaHojas.configure(height=15)

		btn_ExportarData=ttk.Button(self.frame_HojasHIS,text="Exportar")
		btn_ExportarData["command"]=self.Exportar_data
		btn_ExportarData.grid(row=8,column=2)

		Btn_verHoja=ttk.Button(self.frame_HojasHIS,text="Ver Hoja")
		Btn_verHoja["command"]=self.ver_DatosHoja
		Btn_verHoja.grid(row=8,column=3)

	def ver_DatosHoja(self):
		if self.TListaHojas.selection():
			codigo1=self.TListaHojas.item(self.TListaHojas.selection()[0])['values'][0]
			self.Frame_HojaHis(codigo1,False)
		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!")

	def Exportar_data(self):
		if self.TListaHojas.selection():
			codigo=self.TListaHojas.item(self.TListaHojas.selection()[0])['values'][0]			
			obj_report=reporte.Reporte()
			aux=obj_report.Genera_RDatos(codigo)
			if aux:
				messagebox.showinfo("Alerta","Se generó correctamente!!")
			else:
				messagebox.showinfo("Alerta","Hoja Vacía, no pudo generarse!!")
		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!")

	def Frame_NewHIS(self):
		self.frame_HIS=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.frame_HIS.place(x=0,y=0)
		self.frame_HIS.grid_propagate(False)
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


		Btn_verHoja=ttk.Button(self.frame_HIS,text='Ver Hoja',cursor="hand2")	
		Btn_verHoja["command"]=self.see_HojaData
		Btn_verHoja.grid(row=8,column=2)



		Btn_Insertar=ttk.Button(self.frame_HIS,text='Insertar Datos',cursor="hand2")
		Btn_Insertar["command"]=self.Insert_Data
		Btn_Insertar.grid(row=8,column=4)

		Btn_Eliminar=ttk.Button(self.frame_HIS,text='Eliminar',cursor="hand2")
		Btn_Eliminar.grid(row=8,column=6)


	def see_HojaData(self):
		if self.table_Hojas.selection():
			codigo1=self.table_Hojas.item(self.table_Hojas.selection()[0])['values'][0]
			self.Frame_HojaHis(codigo1,True)
		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!")

	def Frame_HojaHis(self,codigo1,identificador):
		font=('Comic Sans MS',18,'bold')		
		self.frame_HOJAHIS=Frame(self.Ventana_Main,width=int(self.width*0.99),height=int(self.height*0.99))
		self.frame_HOJAHIS.grid_propagate(False)
		self.frame_HOJAHIS.place(x=0,y=0)
		etiqueta=Label(self.frame_HOJAHIS,text="PACIENTES REGISTRADOS EN LA HOJA",font=font)
		etiqueta.grid(row=5,column=0,columnspan=6,sticky='e')
		self.t_Hojas=ttk.Treeview(self.frame_HOJAHIS,height=5,columns=('#1','#2','#3','#4'),show='headings')
		self.t_Hojas.heading("#1",text="Codigo")
		self.t_Hojas.column("#1",width=100,anchor="w",stretch='NO')	
		self.t_Hojas.heading("#2",text="Documento")
		self.t_Hojas.column("#2",width=300,anchor="w",stretch='NO')
		self.t_Hojas.heading("#3",text="Nombres")
		self.t_Hojas.column("#3",width=200,anchor="w",stretch='NO')			
		self.t_Hojas.heading("#4",text="Fecha")
		self.t_Hojas.column("#4",width=250,anchor="w",stretch='NO')					
		self.t_Hojas.grid(row=6,column=0,columnspan=20) 
		self.t_Hojas.configure(height=30)

			#llenar table...
		for item in self.t_Hojas.get_children():
			self.t_Hojas.delete(item)

		ro_ws=self.obj_consult.datos_Hoja(codigo1)
		for valores in ro_ws:
			self.t_Hojas.insert("","end",values=(valores.ID_DETA,valores.DNI_PAC,valores.NOMBRE+" "+valores.APELLIDOS,valores.FECHA))


		btn_Exportar=ttk.Button(self.frame_HOJAHIS,text="Exportar",cursor="hand2")
		btn_Exportar["command"]=lambda:self.ReportData(codigo1)
		btn_Exportar.grid(row=8,column=2)

		if identificador:
			btn_Editar=ttk.Button(self.frame_HOJAHIS,text="Editar",cursor="hand2")
			btn_Editar["command"]=self.event_Editar
			btn_Editar.grid(row=8,column=4)
				
			btn_Eliminar=ttk.Button(self.frame_HOJAHIS,text="Eliminar",cursor="hand2")
			btn_Eliminar["command"]=lambda:self.delete_dataHIS(codigo1)
			btn_Eliminar.grid(row=8,column=6)		

	def event_Editar(self):
		if self.t_Hojas.selection():
			codigo1=self.t_Hojas.item(self.t_Hojas.selection()[0])['values'][0]			
			self.obj_his.Top_EditarData(codigo1,self.Ventana_Main)

		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!")

	def ReportData(self,codigo):
		obj_report=reporte.Reporte()
		try:
			aux=obj_report.Genera_RDatos(codigo)
			if aux:
				messagebox.showinfo("Alerta","Se generó el archivo correctamente")
			else:
				messagebox.showinfo("Alerta","No pudo generarse")
		except Exception as e:
			messagebox.showinfo("Alerta",f"No pudo generarse el Archivo {e}")
		
	def delete_dataHIS(self,codigo1):
		iddeta=self.t_Hojas.item(self.t_Hojas.selection()[0])['values'][0]
		nro_diagnostico=0		
		nro_diagnostico=self.obj_consult.delete_diagnostico(iddeta)
		if nro_diagnostico>0:
			nro_deta=0
			nro_deta=self.obj_consult.delete_deta(iddeta)
			if nro_deta>0:
				messagebox.showinfo("Alerta","Operacion Exitosa")

				for item in self.t_Hojas.get_children():
					self.t_Hojas.delete(item)

				ro_ws=self.obj_consult.datos_Hoja(codigo1)
				for valores in ro_ws:
					self.t_Hojas.insert("","end",values=(valores.ID_DETA,valores.DNI_PAC,valores.NOMBRE+" "+valores.APELLIDOS,valores.FECHA))

	def Insert_Data(self):
		if self.table_Hojas.selection():
			codigo=self.table_Hojas.item(self.table_Hojas.selection()[0])['values'][0]
			self.obj_his.Top_InsertarData(self.Ventana_Main,codigo,self.servicio_)
			
		else:
			messagebox.showinfo("Alerta","Seleccione un ITEM!!"'')		

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
		datos.append(self.servicio_)		
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
	
	def llenarcomboServicio(self):
		rows=self.obj_consult.Servicios()
		valores=[]
		for val in rows:
			valores.append(val.CODSERVICIO+"_"+val.NOMBRE)
		self.combo_ServicioL["values"]=valores

	def event_ComboServicio(self,event):
		fecha_=self.dateL.get()
		servicio=self.combo_ServicioL.get()
		rows=self.obj_consult.ServiciosVar(servicio[:servicio.find("_")],fecha_)
		
		for item in self.TListaHojas.get_children():
			self.TListaHojas.delete(item)
		for val in rows:
			self.TListaHojas.insert('','end',values=(val.CODCABECERA,val.NOMBRES+" "+val.APELLIDOP+" "+val.APELLIDOM,val.ESTABLECIMIENTO,val.TURNO,val.CODSERVICIO,val.FECHA))

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

	def acercaDe_(self):
		messagebox.showinfo("Acerca de...","Registro Diario de Hojas de Atencion HIS V1")
	def Author_(self):
		messagebox.showinfo("Acerca de...","Desarrollado por la Unidad de Estadistica e Informatica del HSRA mediante el área de 'Desarrollo Informático'\n by Jaime Navarro Cruz @todos los derechos reservados ")
	
	

