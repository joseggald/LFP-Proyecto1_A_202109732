#IMPORTE DE LIBRERIAS
import math
from tkinter import filedialog, ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import tkinter as tk
import webbrowser as wb


#VARIABLES
global open_status_name
open_status_name=False
data=[]
operaciones=[]
resultados=[]
errores=[]
lineaError=[]
contLinea=0
contOpe=0
contTexto=0
fin=0


#CLASE PARA EL PROGRAMA
class Main:

    #MAIN VENTANA
    def __init__(self, window):
        self.wind=window
        window.title('Menu Principal')
        width=800
        height=500
        window.config(bg = "#88cffa")
        screenwidth = self.wind.winfo_screenwidth()
        screenheight = self.wind.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.wind.geometry(alignstr)
        self.wind.resizable(width=False, height=False)
        frame=Frame(window, bg = "#88cffa")
        frame.pack(pady=4)
        self.texto = Text(frame, width=110, height=30, font=("Comic Sans MS",18), selectbackground="white", selectforeground="black")
        self.texto.pack(padx=10, pady=10)
        barra_scroll=Scrollbar(frame)
        barra_scroll.pack(side=RIGHT, fill=Y)
        barra_scroll.config(command=self.texto.yview)
        barra_navegar=tk.Menu()
        archivo=Menu(barra_navegar)
        barra_navegar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Abrir", command=self.abrirArchivo)
        archivo.add_command(label="Guardar", command=self.guardar)
        archivo.add_command(label="Guardar Como...", command=self.guardarComo)
        archivo.add_command(label="Analizar", command=self.analizar)
        archivo.add_command(label="Errores", command=self.abrirErrores)
        archivo.add_command(label="Resultados", command=self.abrirRes)
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.salirPrograma)
        ayuda=Menu(barra_navegar)
        barra_navegar.add_cascade(label="Ayuda", menu=ayuda)
        ayuda.add_command(label="Manual Tecnico", command=self.abrirMT)
        ayuda.add_command(label="Manual de Usuario", command=self.abrirMU)
        ayuda.add_command(label="Temas de ayuda", command=self.ayuda)
        window.config(menu=barra_navegar)

    #OPCIONES DE MENU BAR   

    #OBTENCION DE ARCHIVOS Y GUARDADO
    def abrirArchivo(self):
        global open_status_name
        try:
            self.texto.delete("1.0", END)
            a=filedialog.askopenfilename(title='Abrir Archivo', filetypes=(("Text Files","*.txt"),("HTML Files","*.hmtl"),("Python Files","*.py"),("XML Files",("*.xml")),("All files","*.")))
            self.archivo=open(a, "r",encoding="utf-8")
            stuff=self.archivo.read()
            open_status_name=a
            self.texto.insert(END, stuff)
            self.archivo.close()
            messagebox.showinfo(title="Explorador de archivos", message="El archivo fue encontrado.")
        except:
            messagebox.showerror(title="Explorador de archivos", message="Hubo un error al obtener el archivo")
    def guardarComo(self): 
        global open_status_name
        self.archivo=filedialog.asksaveasfilename(defaultextension=".*", title="Guardar Archivo Como", filetypes=(("Text Files","*.txt"),("HTML Files","*.hmtl"),("Python Files","*.py"),("XML Files",("*.xml")),("All files","*.")))
        open_status_name=self.archivo
        self.archivo=open(self.archivo,'w',encoding="utf-8")
        self.archivo.write(self.texto.get(1.0, END))
        self.archivo.close()
        messagebox.showinfo(title="Guardar", message="El archivo fue guardado.")  
    def guardar(self):

        global open_status_name
        res = messagebox.askquestion('Guardar archivo', '¿Desea guardar este archivo?')
        if res=='yes':
            self.archivo=open(open_status_name,'w',encoding="utf-8")
            self.archivo.write(self.texto.get(1.0, END))
            self.archivo.close()
            messagebox.showinfo(title="Guardar", message="El archivo fue guardado.")
        else:
            messagebox.showerror(title="Guardar", message="El archivo no fue guardado.")


    #BARRA AYUDA
    def ayuda(self):
           messagebox.showinfo(title="PROGRAMA ANALZADOR LEXICO", message="El siguiente programa consiste en analizar el archivo de cualquier tipo y detectar si tiene la estrcutura correctar y ejecutar las operaciones disponibles, si en dado caso hay errores este generara un reporte de errores y si no hay error generara el reporte de resultados de las operaciones.  Para mas informacion en: MANUAL TECNICO Y DE USUARIO.")
    def abrirErrores(self):
        try:
            wb.open_new_tab('Error.html')
        except:
            messagebox.showerror(title="Errores", message="El archivo no ha sido analizado o no se encotraron errores.")
    def abrirRes(self):
        try:
            wb.open_new_tab('Resultados.html')
        except:
            messagebox.showerror(title="Resultados", message="El archivo no ha sido analizado o se han encotrado errores.")
    
    #ABRIR MANUALES
    def abrirMT(self):
        wb.open_new('D:\Jose\CLASES\Lenguajes\Proyecto_1\Manuales\ManualTecnico.pdf')
    def abrirMU(self):
        wb.open_new('D:\Jose\CLASES\Lenguajes\Proyecto_1\Manuales\ManualDeUsuario.pdf')
            
    #ANALIZAR
    def analizar(self):
        global contLinea
        global fin
        fin=0
        try:
            contLinea=0
            data.clear()
            operaciones.clear()
            resultados.clear()
            errores.clear()
            lineaError.clear()
            analizar=open(open_status_name,"r",encoding="utf-8")
            lineas=analizar.readlines()
            for linea in lineas:
                linea=linea.replace(" ", "") 
                linea=linea.replace("\n", "")
                linea=linea.replace("\t", "")
                data.append(linea)
           
            self.tipo() 
        except:
            print("TERMINADO")


                            
    def tipo(self):
        global contLinea
        cadena_igual=[]
        elemento=""
        for elem in data[contLinea]:
            cadena_igual.append(elem)
        for j in range(len(cadena_igual)):
            if cadena_igual[j].isalpha():
                    elemento=elemento+str(cadena_igual[j])          
            
        if elemento=="Tipo": 
            contLinea=contLinea+1   
            self.ope()      
        else:
            errores.append("No se encontro Tipo.")
            lineaError.append(contLinea+1)
            self.reporteErro()   
          
    def ope(self):
        global contLinea
        cadena_ope=[]
        contLinea
        contCade=0
        cadena_ope.clear()
        elemento=""
        elemento2=""
        global fin
        for elem in data[contLinea]:
            cadena_ope.append(str(elem))
        
        for j in range(len(cadena_ope)):
            if cadena_ope[j].isalpha() and contCade<9:
                elemento=elemento+str(cadena_ope[j])
                contCade=contCade+1
        for j in range(len(cadena_ope)):
            if cadena_ope[j].isalpha():
                elemento2=elemento2+str(cadena_ope[j])
                contCade=contCade+1
              
        if elemento=="Tipo": 
            contLinea=1+contLinea
            fin=1
            self.generarHtml()  
        if elemento=="Operacion" and fin<1:
            self.igual()
        if elemento!="Operacion" and fin<1:
            errores.append("No se encontro Operacion.")
            lineaError.append(contLinea+1)
            self.reporteErro() 
             

    def igual(self):
        global contLinea
        cadena_igual=[]
        contCade=0
        elemento=""
        for elem in data[contLinea]:
            cadena_igual.append(elem)
        for j in range(len(cadena_igual)):
            if cadena_igual[j].isalpha() and contCade<9:
                    contCade=contCade+1           
            if contCade==9:
                elemento=cadena_igual[j+1]
                contCade=contCade+1   
        
                
        if elemento=='=':    
            self.tipoOpe() 
        else:
            errores.append("No se encontro =.")
            lineaError.append(contLinea+1)
            self.reporteErro()    
            
    def tipoOpe(self):
        global contLinea
        cadena_tipoOpe=[]
        contCade=0
        elemento=""
        for elem in data[contLinea]:
            cadena_tipoOpe.append(elem)
        for j in range(len(cadena_tipoOpe)):
            if cadena_tipoOpe[j].isalpha():
                contCade=contCade+1
                if contCade>9:
                    elemento=elemento+str(cadena_tipoOpe[j])

            
        if elemento=="SUMA":
            contLinea=contLinea+1
            self.numSuma()
        if elemento=="RESTA":
            contLinea=contLinea+1
            self.numResta()  
        if elemento=="MULTIPLICACION":
            contLinea=contLinea+1
            self.numMulti() 
        if elemento=="DIVISION":
            contLinea=contLinea+1
            self.numDiv() 
        if elemento=="POTENCIA":
            contLinea=contLinea+1
            self.numPot() 
        if elemento=="RAIZ":
            contLinea=contLinea+1
            self.numRAIZ() 
        if elemento=="INVERSO":
            contLinea=contLinea+1
            self.numInv()
        if elemento=="SENO":
            contLinea=contLinea+1
            self.numSen() 
        if elemento=="COSENO":
            contLinea=contLinea+1
            self.numCos() 
        if elemento=="TANGENTE":
            contLinea=contLinea+1
            self.numTan()
        if elemento=="MOD":
            contLinea=contLinea+1
            self.numMod() 
        else:
            if fin<1:
                errores.append("No se encontro ningun tipo de operación valida. (SUMA,RESTA,DIVISION...)")
                lineaError.append(contLinea+1)
                self.reporteErro() 
            
    def numSuma(self):
        global contLinea
        cadena_num=[]
        cadena_Res=""
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        while stop!=True:
            contCade=0
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            

            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            errores.append("No es valido los digitos de la operacion.")
                            lineaError.append(contLinea+1)
                            self.reporteErro()
             
            if elemento=="Numero":
                contOp=1+contOp
                ope=ope+num
                
                contLinea=contLinea+1
                if contOp==1:
                    cadena_Res=str(num)
                else: 
                    cadena_Res=cadena_Res+" + "+str(num)
            
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1        
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.sqrt(ope)
                cadena_Res="RAIZ("+cadena_Res+")"
                
            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.sin(ope)
                cadena_Res="SENO("+cadena_Res+")"
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.cos(ope)
                cadena_Res="COSENO("+cadena_Res+")"
                
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])       
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope%num
                    cadena_Res="("+cadena_Res+") % "+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                errores.append("La escritura de Numero incorrecte o cierre de operacion no valido.")
                lineaError.append(contLinea+1)
                self.reporteErro()
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope()



    def numResta(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            errores.append("No es valido los digitos de la operacion.")
                            lineaError.append(contLinea+1)
                            self.reporteErro() 
             
            if elemento=="Numero":
                contOp=1+contOp
                if contOp==1:
                    ope=ope+num
                    cadena_Res=str(num)
                else:
                    cadena_Res=cadena_Res+" - "+str(num)
                    ope=ope-num
                contLinea=contLinea+1
                
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1

            
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1        
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                       
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")

            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="INVERSO("+cadena_Res+")"
                ope=self.invertir_numero(ope)
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="SENO("+cadena_Res+")"
                ope=math.sin(ope)
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="COSENO("+cadena_Res+")"
                ope=math.cos(ope)
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="TANGENTE("+cadena_Res+")"
                ope=math.tan(ope)
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                errores.append("La escritura de Numero incorrecto o cierre de operacion no valido.")
                lineaError.append(contLinea+1)
                self.reporteErro()
                break
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope()    

    def numMulti(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            errores.append("No es valido los digitos de la operacion.")
                            lineaError.append(contLinea+1)
                            self.reporteErro() 
             
            if elemento=="Numero":
                contOp=1+contOp
                if contOp==1:
                    ope=num
                    cadena_Res=str(num)
                else:
                    ope=ope*num
                    cadena_Res=cadena_Res+" * "+str(num)
                contLinea=contLinea+1
                
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1

            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1 
             
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                       
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")

            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="INVERSO("+cadena_Res+")"
                ope=self.invertir_numero(ope)
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="SENO("+cadena_Res+")"
                ope=math.sin(ope)
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="COSENO("+cadena_Res+")"
                ope=math.cos(ope)
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="TANGENTE("+cadena_Res+")"
                ope=math.tan(ope)
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                errores.append("La escritura de Numero incorrecto o cierre de operacion no valido.")
                lineaError.append(contLinea+1)
                self.reporteErro()
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope() 

    def numDiv(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            errores.append("No es valido los digitos de la operacion.")
                            lineaError.append(contLinea+1)
                            self.reporteErro() 
             
            if elemento=="Numero":
                contOp=1+contOp
                if contOp==1:
                    ope=num
                    cadena_Res=str(num)
                else:
                    ope=ope/num
                    cadena_Res=cadena_Res+" / "+str(num)
                contLinea=contLinea+1
                
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1 
            
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                       
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")

            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.sin(ope)
                cadena_Res="SENO("+cadena_Res+")"
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.cos(ope)
                cadena_Res="COSENO("+cadena_Res+")"
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                errores.append("No es valido los digitos de la operacion.")
                                lineaError.append(contLinea+1)
                                self.reporteErro()
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                errores.append("La escritura de Numero incorrecto o cierre de operacion no valido.")
                lineaError.append(contLinea+1)
                self.reporteErro()
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope() 
        
    def numPot(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                contOp=1+contOp
                if contOp==1:
                    ope=num
                    cadena_Res=str(num)
                else:
                    ope=ope**num
                    cadena_Res=cadena_Res+'**'+str(num)
                contLinea=contLinea+1
            
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                    
                except:
                    print("error")

            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.sin(ope)
                cadena_Res="SENO("+cadena_Res+")"
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.cos(ope)
                cadena_Res="COSENO("+cadena_Res+")"
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope()        

    def numRAIZ(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                ope=math.sqrt(num)
                cadena_Res="RAIZ("+str(num)+")"
                contLinea=contLinea+1
                
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1

            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.sin(ope)
                cadena_Res="SENO("+cadena_Res+")"
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.cos(ope)
                cadena_Res="COSENO("+cadena_Res+")"
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num       
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            print(cadena_Res)
            resultados.append(cadena_Res)
            self.ope()

    def numInv(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                ope=self.invertir_numero(num)
                contLinea=contLinea+1
                cadena_Res="INVERSO("+str(num)+")"
                
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                    
                except:
                    print("error")
            
                
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="SENO("+cadena_Res+")"
                ope=math.sin(ope)
                       
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="COSENO("+cadena_Res+")"
                ope=math.cos(ope)
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            resultados.append(cadena_Res)
            print(cadena_Res)
            self.ope()

    def numSen(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                ope=math.sin(num)
                contLinea=contLinea+1
                cadena_Res="SENO("+str(num)+")"

            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")
            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
            
                      
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.cos(ope)
                cadena_Res="COSENO("+cadena_Res+")" 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=math.tan(ope)
                cadena_Res="TANGENTE("+cadena_Res+")"
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            resultados.append(cadena_Res)
            print(cadena_Res)
            self.ope()   

    def numCos(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                ope=math.cos(num)
                cadena_Res="COSENO("+str(num)+")"
                contLinea=contLinea+1
                
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")
            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="INVERSO("+cadena_Res+")"
                ope=self.invertir_numero(ope)
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="SENO("+cadena_Res+")"
                ope=math.sin(ope)    
            
                 
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="TANGENTE("+cadena_Res+")"
                ope=math.tan(ope)
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            resultados.append(cadena_Res)
            print(cadena_Res)
            self.ope()

    def numTan(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                ope=math.tan(num)
                contLinea=contLinea+1
                cadena_Res="TANGENTE("+str(num)+")"
                
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")
            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="INVERSO("+cadena_Res+")"
                ope=self.invertir_numero(ope)
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                cadena_Res="SENO("+cadena_Res+")"
                elemento="Numero"
                ope=math.sin(ope)    
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="COSENO("+cadena_Res+")"
                ope=math.cos(ope)
                 
            
                
            if elemento2=="OperacionMOD": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                    
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope%num
                    cadena_Res="("+cadena_Res+")%"+str(num)
                    contLinea=contLinea+1     

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            resultados.append(cadena_Res)
            print(cadena_Res)
            self.ope()

    def numMod(self):
        global contLinea
        cadena_num=[]
        contCade=0
        contCierre=0
        elemento=""
        stop=False
        cierre=""
        k=0
        num=0
        a=0
        ope=0
        contCierre=1
        contOp=0
        cadena_Res=""
        while stop!=True:
            contCade=0
            
            cadena_num.clear()
            elemento=""
            elemento2=""
            cierre=""
            num=0
            a=""
            for elem in data[contLinea]:
                cadena_num.append(elem)

            for j in range(len(cadena_num)):
                if cadena_num[j].isalpha() and contCade<6:
                    contCade=contCade+1
                    elemento=elemento+str(cadena_num[j])       
                if contCade<10:
                    cierre=cierre+str(cadena_num[j])
                if cadena_num[j].isalpha():
                    elemento2=elemento2+str(cadena_num[j])
  
            
            
            if elemento=="Numero":   
                for k in range(len(cadena_num)):
                    if cadena_num[k].isdigit() or cadena_num[k]==".":
                        try:
                            a=a+str(cadena_num[k])
                            num=float(a)    
                        except:
                            print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos") 
             
            if elemento=="Numero":
                contOp=1+contOp
                if contOp==1:
                    ope=num
                    cadena_Res=str(num)
                else:
                    ope=ope%num
                    cadena_Res=cadena_Res+" % "+str(num)
                contLinea=contLinea+1
            if elemento2=="OperacionRESTA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope-num
                    cadena_Res="("+cadena_Res+")-"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionSUMA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope+num
                    cadena_Res="("+cadena_Res+")+"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionMULTIPLICACION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope*num
                    cadena_Res="("+cadena_Res+")*"+str(num)
                    contLinea=contLinea+1       
            
            
            if elemento2=="OperacionDIVISION": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope/num
                    cadena_Res="("+cadena_Res+")/"+str(num)
                    contLinea=contLinea+1   
            if elemento2=="OperacionPOTENCIA": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento=""
                contCade=0
                a=""
                cadena_num.clear()
                for elem in data[contLinea]:
                    cadena_num.append(elem)
                for j in range(len(cadena_num)):
                    if cadena_num[j].isalpha() and contCade<6:
                        contCade=contCade+1
                        elemento=elemento+str(cadena_num[j])
                        
                if elemento=="Numero":   
                    for k in range(len(cadena_num)):
                        if cadena_num[k].isdigit() or cadena_num[k]==".":
                            try:
                                a=a+str(cadena_num[k])
                                num=float(a)    
                            except:
                                print("error en la linea: "+ str(contLinea+1)+" en la escritura de los digitos")
                    ope=ope**num
                    cadena_Res="("+cadena_Res+")**"+str(num)
                    contLinea=contLinea+1
            if elemento2=="OperacionRAIZ":
                try:  
                    contLinea=1+contLinea
                    contCierre=1+contCierre
                    elemento="Numero"
                    ope=math.sqrt(ope)
                    cadena_Res="RAIZ("+cadena_Res+")"
                except:
                    print("error")
            if elemento2=="OperacionINVERSO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                ope=self.invertir_numero(ope)
                cadena_Res="INVERSO("+cadena_Res+")"
            if elemento2=="OperacionSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="SENO("+cadena_Res+")"
                ope=math.sin(ope)    
            if elemento2=="OperacionCOSENO": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="COSENO("+cadena_Res+")"
                ope=math.cos(ope)
                
            if elemento2=="OperacionTANGENTE": 
                contLinea=1+contLinea
                contCierre=1+contCierre
                elemento="Numero"
                cadena_Res="TANGENTE("+cadena_Res+")"
                ope=math.tan(ope)    

            if elemento!="Numero" and cierre!="</Operacion>":
                print("error en la linea: "+ str(contLinea+1)+" en Numero")
                stop=True              
            if cierre=="</Operacion>": 
                contLinea=contLinea+1         
                contCierre=contCierre-1
            if contCierre==0:
                stop=True
        if cierre=="</Operacion>": 
            operaciones.append(ope)
            cadena_Res=cadena_Res+" = "+str(ope)
            resultados.append(cadena_Res)
            print(cadena_Res)
            self.ope()

    def generarHtml(self): 
        messagebox.showinfo(title="ARCHIVO ANALIZADO", message="Se ha ejecutado las operaciones y el reporte de operaciones en un HTML EN LA CARPETA.")
        archi1=open("Resultados.html","w") 
        archi1.write("<!DOCTYPE html>\n") 
        archi1.write('<html lang="en">\n') 
        archi1.write('<head>\n') 
        archi1.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n') 
        archi1.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n') 
        archi1.write('<title>RESULTADOS</title>\n') 
        archi1.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">\n') 
        archi1.write('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>\n')
        archi1.write('</head>\n')
        archi1.write('<body>\n')
        archi1.write('<h1 class="text-center">RESULTADOS DE OPERACIONES.</h1> \n')
        archi1.write('<h3 class="text-center">Archivo simple de pruebas aritmeticas de proyecto 1 LFP A+</h2>\n')
        archi1.write('<h4 class="text-center">Operaciones aritmeticas</h4>\n')
        archi1.write('<br>\n')
        archi1.write('<div class="container">\n')
        for i in range(len(resultados)):
            archi1.write('<div class="container">\n')
            archi1.write('<label class="mb-3"> <b>Operacion No. '+str(i+1)+':'+'</b></label>\n')
            archi1.write('<div>\n')
            archi1.write('<label class="mb-3">'+resultados[i]+'</label>\n')
            archi1.write('</div>\n')
            archi1.write('</div>\n')
            archi1.write('<br>\n')
        archi1.write('</div>\n')
        archi1.write('</body>\n')
        archi1.write('</html>\n')
        archi1.close() 
        
    def reporteErro(self):
        messagebox.showerror(title="ERROR DETECTADO", message="Hubo error en la ejecucion de analizar el archivo, Reporte Generado.")
        archi1=open("Error.html","w") 
        archi1.write("<!DOCTYPE html>\n") 
        archi1.write('<html lang="en">\n') 
        archi1.write('<head>\n') 
        archi1.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n') 
        archi1.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n') 
        archi1.write('<title>RESULTADOS</title>\n') 
        archi1.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">\n') 
        archi1.write('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>\n')
        archi1.write('</head>\n')
        archi1.write('<body>\n')
        archi1.write('<h1 class="text-center p-3">ERROR DETECTADO.</h1> \n')
        archi1.write('<br>\n')
        archi1.write('<table class="table table-dark table-bordered table-striped">\n')
        archi1.write('<thead>\n')
        archi1.write('<tr>\n')
        archi1.write('<th scope="col">Descripción de error</th>\n')
        archi1.write('<th scope="col">Linea</th>\n')
        archi1.write('</tr>\n')
        archi1.write('</thead>\n')
        archi1.write('<tbody>\n')
        archi1.write('<tr>\n')
        archi1.write('<td>'+errores[0]+'</td>\n')
        archi1.write('<td>'+str(lineaError[0])+'</td> \n')
        archi1.write('</tr> \n')
        archi1.write('</tbody>\n')
        archi1.write('</table>\n')
        archi1.write('<div class="container">\n')     
        archi1.write('</div>\n')
        archi1.write('</body>\n')
        archi1.write('</html>\n')
        archi1.close()           

    #SALIR DE LA VENTANA
    def salirPrograma(self):
        self.wind.destroy()
        
    def invertir_numero(self,n):
        numero = 0
        while n != 0:
            numero = 10*numero+n % 10
            n //= 10
        return numero           


if __name__ == '__main__':
    window=Tk()
    app=Main(window)
    window.mainloop()