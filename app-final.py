import funciones
from bottle import request, run, route, redirect, template
import sqlite3
import paste
import serial

PORT = 'COM5'

conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

id=0
eid=0
user=""
rol=""
borrar=0
esquema=0
hab=0
habilitacion=""

@route('/login')
@route('/login', method='POST')
def login():
    error1 = 0
    error2 = 0

    if len(request.POST) == 0:
       
        return template('templates/login.html', error1 = error1, error2 = error2)

    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        a = request.POST['username'];
        b = request.POST['password'];
       
        if len(a) and len(b):
            consulta_login =f"select user, pass from usuarios where user = '{a}' and pass = '{b}';"

            if len(tuple(conn.execute(consulta_login))):

                cursor.execute(f"select id from usuarios where user = '{a}'")
                id = (cursor.fetchone())[0]
                redirect("/inicio?id=" + str(id))
               
            else:
                error1 = 1
                error2 = 0
                return template('templates/login.html', error1 = error1, error2 = error2)    

        else:
                error1 = 0
                error2 = 1
                return template('templates/login.html', error1 = error1, error2 = error2)
        
@route('/logout')
def logout():
    id=0
    rol=""
    user=""
    redirect('/login')

@route('/change-password')
@route('/change-password', method='POST')
def changepassword():
    if len(request.POST) == 0:
                error1 = 0
                error2 = 0
                error3 = 0
                error4 = 0
                contra = 0
                return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        a = request.POST['username'];
        b = request.POST['password'];
        c = request.POST['pregunta'];
        c=c.lower()
        d = request.POST['password2'];
        
        if len(a) and len(b) and len(c) and len(d):
            consulta_verificacion = f"select user from usuarios where user = '{a}';"
            consulta_verif = cursor.execute(f"select pregunta from usuarios where user = '{a}';")
            consulta_verificacion2=""
            
            if len(tuple(conn.execute(consulta_verificacion))):
                consulta_verificacion2=(consulta_verif.fetchone())[0]
                
            if len(tuple(conn.execute(consulta_verificacion))) and c == consulta_verificacion2 and b == d:
            
                conn.execute(f"UPDATE usuarios SET pass='{b}' WHERE user = '{a}'")
                conn.commit()
                conn.close()
                
                error1 = 0
                error2 = 0
                error3 = 0
                error4 = 0
                contra = 1
                return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
            
            elif len(tuple(conn.execute(consulta_verificacion)))==0:
                
                error1 = 1
                error2 = 0
                error3 = 0
                error4 = 0
                contra = 0
                return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
                
            elif c != consulta_verificacion2:
                error1 = 0
                error2 = 1
                error3 = 0
                error4 = 0
                contra = 0
                return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
            
            elif b != d:
                error1 = 0
                error2 = 0
                error3 = 0
                error4 = 1
                contra = 0
                return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
    
        else:
            error1 = 0
            error2 = 0
            error3 = 1
            error4 = 0
            contra = 0
            return template('templates/olvidar-contra.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, contra = contra)
       
       
@route('/register')
@route('/register', method='POST')
def register():
    error1 = 0
    error2 = 0
    error3 = 0
    error4 = 0
    login = 0
           
    if len(request.POST) == 0:
        return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)

    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        a = request.POST['username'];
        b = request.POST['password'];
        c = request.POST['nombre'];
        d = request.POST['apellido'];
        e = request.POST['documento'];
        f = request.POST['password2'];
        g = request.POST['pregunta'];
       
        if len(a) and len(b) and len(c) and len(d) and len(g) and len(f) and len(e)==8:
   
            consulta_verificacion = f"select user from usuarios where user = '{a}';"
            consulta_verificacion2 = f"select DNI from usuarios where DNI = '{e}';"
                   
            if len(tuple(conn.execute(consulta_verificacion))):
                error1 = 1
                error2 = 0
                error3 = 0
                error4 = 0
                login = 0
                return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)
           
            if b != f:
                error1 = 0
                error2 = 1
                error3 = 0
                error4 = 0
                login = 0
                return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)
               
           
            if len(tuple(conn.execute(consulta_verificacion2))):
                error1 = 0
                error2 = 0
                error3 = 1
                error4 = 0
                login = 0
                return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)
            
            else:
                g=g.lower()
                consulta_register = f"insert into usuarios (user, pass, nombre, apellido, DNI, rol, pregunta) values ('{a}', '{b}','{c}','{d}','{e}', 'USUARIO', '{g}');"

                conn.execute(consulta_register)
                conn.commit()
               
                error1 = 0
                error2 = 0
                error3 = 0
                error4 = 0
                login = 1
                return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)
        else:
                error1 = 0
                error2 = 0
                error3 = 0
                error4 = 1
                login = 0
                return template('templates/register.html', error1 = error1, error2 = error2, error3 = error3, error4 = error4, login = login)
    
    
@route('/inicio', method='get')
@route('/inicio', method='post')
def menu():
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    if id==0:
        rol=""
        user=""
    else:
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
      
    return template('templates/menu.html', rol = rol, user = user, id = id)
    
@route('/esquema')
@route('/esquema', method='POST')
def eleccionesquema():
    
    esquema = 0
    id = request.GET.get("id")
    id=int(id)
    
    if id == 0:
        redirect('/inicio?id=0')
    else:  
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        recibir_listapast=conn.execute("select nombrepastilla from pastillas")
        listadopast=list(recibir_listapast)
        
        consulta_rutina1 = f"select id from rutinas where id='{id}';"
        consulta_rutina2 = f"select id from rutinassemanales where id='{id}';"
        
    if len(request.POST) == 0:
        return template('templates/esquema.html', rol = rol, user = user, id = id, listapas=list(listadopast), esquema = esquema)
    else:
        tipodepastillero = request.POST['tipopastillero'];
        
        if tipodepastillero == "semanal" and len(tuple(conn.execute(consulta_rutina1)))==0 and len(tuple(conn.execute(consulta_rutina2)))==0:
            redirect('/esquema-semanal')

        elif tipodepastillero == "semanalyhorario" and len(tuple(conn.execute(consulta_rutina1)))==0 and len(tuple(conn.execute(consulta_rutina2)))==0:
            redirect('/esquema-tres-tomas')
        else:
            esquema = 1
            return template('templates/esquema.html', rol = rol, user = user, id = id, listapas=list(listadopast), esquema = esquema)
    
@route('/esquema-tres-tomas')
@route('/esquema-tres-tomas', method='POST')
def esquema1(): 

    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    recibir_listapast=conn.execute("select nombrepastilla from pastillas")
    listadopast=list(recibir_listapast)
    trestomas = 0
    error = 0
 
    if id == 0:
        redirect('/inicio?id=0')
    else:
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        consulta_rutina1 = f"select id from rutinas where id='{id}';"
        consulta_rutina2 = f"select id from rutinassemanales where id='{id}';"
        
        if len(tuple(conn.execute(consulta_rutina1))) or len(tuple(conn.execute(consulta_rutina2))):

            error = 1
            return template('templates/esquematrestomas.html', rol = rol, user = user, id = id, listapas=list(listadopast),trestomas = trestomas, error = error)

        else:
            if len(request.POST) == 0:
                return template('templates/esquematrestomas.html', rol = rol, user = user, id = id, listapas=list(listadopast),trestomas = trestomas, error = error)

            else:
                var=0
                lista_rutinas1=funciones.recibirrutina1(id, var)
                conn.execute(lista_rutinas1)
                conn.commit()
                
                trestomas = 1
                return template('templates/esquematrestomas.html', rol = rol, user = user, id = id, listapas=list(listadopast),trestomas = trestomas, error = error)

            
@route('/esquema-semanal')
@route('/esquema-semanal', method='POST')
def esquema2():
        
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    recibir_listapast=conn.execute("select nombrepastilla from pastillas")
    listadopast=list(recibir_listapast)
    semanal = 0
    error = 0
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        consulta_rutina1 = f"select id from rutinas where id='{id}';"
        consulta_rutina2 = f"select id from rutinassemanales where id='{id}';"
        
        if len(tuple(conn.execute(consulta_rutina1))) or len(tuple(conn.execute(consulta_rutina2))):
                error = 1
                return template('templates/esquemasemanal.html', rol = rol, user = user, id = id, listapas=list(listadopast), semanal = semanal, error = error)

        else:
            if len(request.POST) == 0:
                return template('templates/esquemasemanal.html', rol = rol, user = user, id = id, listapas=list(listadopast), semanal = semanal, error = error)

            else:
                var=0
                lista_rutinas2=funciones.recibirrutina2(id, var)
                conn.execute(lista_rutinas2)
                conn.commit()
                semanal = 1 
                return template('templates/esquemasemanal.html', rol = rol, user = user, id = id, listapas=list(listadopast), semanal = semanal, error = error)
            
@route('/lista')
@route('/lista', method='POST')
def ver_lista(): 
        
    id = request.GET.get("id")
    id=int(id)
    
    nada = 0
    borrar=0
    buscar=0
    nodisponibles=""
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        consulta_rutina1 = f"select id from rutinas where id='{id}';"
        consulta_rutina2 = f"select id from rutinassemanales where id='{id}';"
        
        if len(tuple(conn.execute(consulta_rutina1)))==0 and len(tuple(conn.execute(consulta_rutina2)))==0 and rol!="ADMIN" and rol!="CREADOR":
            
            listado=""
            listado2=""
            recibir_listapast=conn.execute("select nombrepastilla from pastillas")
            listapas=list(recibir_listapast)
            nada = 1
            return template('templates/listas.html', rol = rol, user = user, id = id, listado = listado, listado2=listado2, listapas=listapas, borrar = borrar, nada = nada, buscar = buscar, hab = hab)
            
        else:
            listado=""
            listado2=""
            recibir_listapast=conn.execute("select nombrepastilla from pastillas")
            listapas=list(recibir_listapast)
            if rol=="ADMIN" or rol=="CREADOR":
                recibir_lista1=conn.execute("select * from rutinas")
                recibir_lista2=conn.execute("select * from rutinassemanales")
                listado=list(recibir_lista2)
                listado2=list(recibir_lista1)

            else:
                if len(tuple(conn.execute(consulta_rutina1))):
                    recibir_lista = conn.execute(f"select * from rutinas where id='{id}'")
                    listado2=list(recibir_lista)
                    listado=""
                    
                if len(tuple(conn.execute(consulta_rutina2))):
                    recibir_list = conn.execute(f"select * from rutinassemanales where id='{id}'")
                    listado= list(recibir_list)
                    listado2=""
            
            return template('templates/listas.html', rol = rol, user = user, id = id, listado = listado, listado2=listado2, listapas=listapas, borrar = borrar, nada = nada, buscar = buscar, hab = hab)

@route('/imprimir-lista', method='GET')
def printlista():
    
    rid = request.GET.get("rid")
    id = request.GET.get("id")
    id=int(id)
    
    borrar=0
    nada=0
    buscar=0
    nodisponibles=""
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        try:
            ser = serial.Serial(PORT, timeout=1.5)

            ser.baudrate = 9600
            ser.bytesize = 8
            ser.parity = 'N'
            ser.stopbits = 1
            ser.timeout = 1.5
        except:
            pass

        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        recibir_lista1=conn.execute("select * from rutinas")
        recibir_lista2=conn.execute("select * from rutinassemanales")
        listado=list(recibir_lista2)
        listado2=list(recibir_lista1)
        recibir_listapast=conn.execute("select nombrepastilla from pastillas")
        listapas=list(recibir_listapast)

        if rol=="ADMIN" or rol=="CREADOR":
            habilitacion = ser.read(4)
            print(habilitacion)
            habilitacion = habilitacion.decode()
            print(habilitacion)
#             habilitacion=":H0&"
            if int(habilitacion[2])==0:
                x=1
                num=1
                printeo=""
                nodisponibles=""
                while x<=21:
                    if x<=3:
                        dia="lunes"
                    if x>3 and x<=6:
                        dia="martes"
                    if x>6 and x<=9:
                        dia="miercoles"
                    if x>9 and x<=12:
                        dia="jueves"
                    if x>12 and x<=15:
                        dia="viernes"
                    if x>15 and x<=18:
                        dia="sabado"
                    if x>18 and x<=21:
                        dia="domingo"
                    num1=str(num)
                    var1= dia + num1
                    printvar1=f"select {var1} from rutinassemanales where id='{rid}'"
                    cursor.execute(printvar1)
                    printvar1=(cursor.fetchone())[0]
                    printvar2=f"select nropastilla from pastillas where nombrepastilla='{printvar1}'"
                    if len(tuple(conn.execute(printvar2))):
                        cursor.execute(printvar2)
                        printvar=(cursor.fetchone())[0]
                    elif printvar1!="-":
                        nodisponibles += printvar1 + "-"
                        printvar=0
                    else:
                        printvar=0
                    printvar=str(printvar)
                    printeo+=printvar
                    msj=':' + '%03d' %(int(rid)) + 'A' + printeo + '&'
                    x+=1
                    num+=1
                    if num>3:
                        num=1
                nodisponibles=nodisponibles[:-1]
                print(msj)
                ser.write(msj.encode())
                
                hab=2
                ser.close()
                return template('templates/listas.html', rol = rol, user = user, id = id, listado = listado, listado2=listado2, listapas=listapas, borrar = borrar, nada = nada, buscar = buscar, hab = hab)
            else:
                hab=1
                return template('templates/listas.html', rol = rol, user = user, id = id, listado = listado, listado2=listado2, listapas=listapas, borrar = borrar, nada = nada, buscar = buscar, hab = hab)
            
        else:
            return '''
                <h1>ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio?id=0'">Volver al inicio</button>
            '''
 
    
@route('/buscar_resultado', method='get')
def buscar():
    
    abuscar = request.GET.get("idbuscar")
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
    recibir_listapast=conn.execute("select nombrepastilla from pastillas")
    listapas=list(recibir_listapast)
    
    buscar = 0
    nada=0
    borrar=0
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        if rol=="ADMIN" or rol=="CREADOR" or id==int(abuscar):
            listado=""
            listado2=""
            nodisponibles
            
            if len(tuple(conn.execute(f"select id from rutinas where id='{abuscar}';"))):
                listitas=f"select * from rutinas where id='{abuscar}';"
                recib_lista=conn.execute(listitas)
                listado2=list(recib_lista)
                listado=""
            elif len(tuple(conn.execute(f"select id from rutinassemanales where id='{abuscar}';"))):
                listitas2 =f"select * from rutinassemanales where id='{abuscar}';" 
                recib_lista2=conn.execute(listitas2)
                listado=list(recib_lista2)
                listado2=""
            else:
                buscar=1
                return template('templates/listas.html', rol = rol, user = user, id = id,  listado = listado, listado2 = listado2, listapas=listapas, borrar=borrar, nada=nada, buscar = buscar, hab = hab)

                
            return template('templates/listas.html', rol = rol, user = user, id = id,  listado = listado, listado2 = listado2, listapas=listapas, borrar=borrar, nada=nada, buscar = buscar, hab = hab)
    
        else:
            abuscar=0
            return '''
                <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio'">Volver a Inicio</button>
            '''
    
@route('/borrar-lista', method='GET')
@route('/borrar-lista', method='POST')
def borrar():
    
    rid = request.GET.get("rid")
    print(rid)
    id = request.GET.get("id")
    id=int(id)
    
    nada=0
    buscar=0
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        recibir_listapast=conn.execute("select nombrepastilla from pastillas")
        listapas=list(recibir_listapast)

        if rol=="ADMIN" or rol=="CREADOR" or id==int(rid):
            funciones.borrarrutina(rid)
            borrar=1
            if rol=="ADMIN" or rol=="CREADOR":
                recibir_lista1=conn.execute("select * from rutinas")
                recibir_lista2=conn.execute("select * from rutinassemanales")
                listado=list(recibir_lista2)
                listado2=list(recibir_lista1)
            else:
                listado=""
                listado2=""
            return template('templates/listas.html', rol = rol, user = user, id = id, listado = listado, listado2=listado2, listapas=listapas, borrar = borrar, nada = nada, buscar = buscar, hab = hab)
        
        else:
            return '''
                <h1>ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio'">Volver al inicio</button>
            '''
        
@route('/editar-lista', method='GET')
def editarlistaget():

    eid = request.GET.get("rid")

    print(eid)
    id = request.GET.get("id")
    id=int(id)
    
    if id == 0:
        redirect('/inicio?id=0')
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        
        cursor.execute(f"select rol from usuarios where id = '{id}'")
        rol = (cursor.fetchone())[0]
        cursor.execute(f"select user from usuarios where id = '{id}'")
        user = (cursor.fetchone())[0]
        
        if rol=="ADMIN" or rol=="CREADOR" or id==int(eid):
            redirect('/editar-listas?rid=' + str(eid) + '&&id=' + str(id))
        else:
            eid=0
            return '''
                <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio'">Volver a Inicio</button>
            '''
            

@route('/editar-listas')
@route('/editar-listas', method='POST')
def editarlistapost():
    
    eid = request.GET.get("rid")
    print(eid)
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
        
    
    if id == 0:
        redirect('/inicio?id=0')
        
    elif rol=="ADMIN" or rol=="CREADOR" or id==int(eid):

        recibir_listapast=conn.execute("select nombrepastilla from pastillas")
        listadopast=list(recibir_listapast)
        print(eid)
        consulta1=f"select id from rutinassemanales where id='{eid}';"
        consulta2=f"select id from rutinas where id='{eid}';"
        if len(tuple(conn.execute(consulta1))):
            if len(request.POST) == 0:
                coso=list(conn.execute(f"select * from rutinassemanales where id='{eid}';"))
                return template('templates/editar.html', lista=coso[0], listapas=list(listadopast), user=user, rol=rol, id=id, eid=eid)
            else:
                var=1
                lista_rutinas3=funciones.recibirrutina2(eid, var)
                print(lista_rutinas3)
                conn.execute(lista_rutinas3)
                conn.commit()
                redirect('/lista?id=' + str(id))
                
        elif len(tuple(conn.execute(consulta2))):
            if len(request.POST) == 0:
                coso=list(conn.execute(f"select * from rutinas where id='{eid}';"))
                return template('templates/editar-tres-tomas.html', lista=coso[0], listapas=list(listadopast), user=user, rol=rol, id=id, eid=eid)
            else:
                var=1
                lista_rutinas1=funciones.recibirrutina1(eid, var)
                conn.execute(lista_rutinas1)
                conn.commit()
                redirect('/lista?id=' + str(id))
        else:
            return '''
                <h1> ERROR - NO HAY RUTINAS INGRESADAS CON ESA CUENTA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio'">Volver a Inicio</button>
            '''
    else:
        return '''
            <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
                
            <button onClick="javascript:window.location.href='/inicio'">Volver a Inicio</button>
        '''
    
@route('/pastillas')
@route('/pastillas', method='POST')
def pastillas():
    
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
    
    if id == 0:
        redirect('/inicio?id=0')
        
    else:
        if rol!="ADMIN" and rol!="CREADOR":
            return '''
                <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ACCEDER A ESTA PAGINA.</h1>
            
                <button onClick="javascript:window.location.href='/login'">Logearse</button>
                <button onClick="javascript:window.location.href='/register'">Registrarse</button>
            '''
        else:
            conn = sqlite3.connect('datos.db')
            cursor = conn.cursor()
            recibir_listapast=conn.execute("select * from pastillas")
            listadopast=list(recibir_listapast)
            return template('templates/pastillas.html', rol = rol, user = user, id = id, listadopast=listadopast)

@route('/borrar-pastilla', method='GET')
def borrar():
    
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
    recibir_listapast=conn.execute("select * from pastillas")
    listadopast=list(recibir_listapast)
    
    if id == 0:
        redirect('/inicio?id=0')

    elif rol!="ADMIN" and rol!="CREADOR":
        return '''
            <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
            
            <button onClick="javascript:window.location.href='/login'">Logearse</button>
            <button onClick="javascript:window.location.href='/register'">Registrarse</button>
        '''
    else:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        slot = request.GET.get("slot")
        
        borrar_past = f"update pastillas set nombrepastilla='Nada' where nropastilla='{slot}';"
        conn.execute(borrar_past)
        conn.commit()
        
        redirect('/pastillas?id=' + str(id))
               
@route('/editar-pastillas')
@route('/editar-pastillas', method='POST')
def editarpastillas():
    
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
    
    if id == 0:
        redirect('/inicio?id=0')
        
    if rol!="ADMIN" and rol!="CREADOR":
        return '''
            <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ESTA TAREA.</h1>
            
            <button onClick="javascript:window.location.href='/login'">Logearse</button>
            <button onClick="javascript:window.location.href='/register'">Registrarse</button>
        '''
    else:
        if len(request.POST) == 0:
            recibir_listapast=conn.execute("select * from pastillas")
            listadopast=list(recibir_listapast)
            return template('templates/editar-pastillas.html', user=user, rol=rol, id=id, listadopast=listadopast)
        else:
            past1=request.POST['entry1']
            past2=request.POST['entry2']
            past3=request.POST['entry3']
            past4=request.POST['entry4']
            past5=request.POST['entry5']
            if len(past1):
                conn.execute(f"update pastillas set nombrepastilla='{past1}' where nropastilla=1")
                conn.commit()
            if len(past2):
                conn.execute(f"update pastillas set nombrepastilla='{past2}' where nropastilla=2")
                conn.commit()
            if len(past3):
                conn.execute(f"update pastillas set nombrepastilla='{past3}' where nropastilla=3")
                conn.commit()
            if len(past4):
                conn.execute(f"update pastillas set nombrepastilla='{past4}' where nropastilla=4")
                conn.commit()
            if len(past5):
                conn.execute(f"update pastillas set nombrepastilla='{past5}' where nropastilla=5")
                conn.commit()
            redirect('/pastillas?id=' + str(id))
        

@route('/usuarios')
@route('/usuarios', method='POST')
def usuarios():

    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]

    if id == 0:
        redirect('/inicio?id=0')
        
    else:
        if rol!="ADMIN" and rol != "CREADOR":
            return '''
                <h1> ERROR - NECESITA PERMISOS DE ADMINISTRADOR PARA ACCEDER A ESTA PAGINA.</h1>
            
                <button onClick="javascript:window.location.href='/login'">Logearse</button>
                <button onClick="javascript:window.location.href='/register'">Registrarse</button>
            '''
        else:
            conn = sqlite3.connect('datos.db')
            cursor = conn.cursor()
            recibir_listauser=conn.execute("select * from usuarios")
            listadouser=list(recibir_listauser)
            return template('templates/usuarios.html', rol = rol, user = user, id = id, listadouser=listadouser)
        
@route('/update-roles', method='GET')
def actualizarRoles():
    
    rid = request.GET.get("rid")    
    id = request.GET.get("id")
    id=int(id)
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    cursor.execute(f"select rol from usuarios where id = '{id}'")
    rol = (cursor.fetchone())[0]
    cursor.execute(f"select user from usuarios where id = '{id}'")
    user = (cursor.fetchone())[0]
    
    if id == 0:
        redirect('/inicio?id=0')
        
    else:
        if rol=="CREADOR":
            consulta_rol=cursor.execute(f"select rol from usuarios where id='{rid}';")
            consulta_rol2=(consulta_rol.fetchone())[0]
            if consulta_rol2 == "ADMIN":
                conn.execute(f"update usuarios set rol='USUARIO' where id='{rid}';")
                conn.commit()
                redirect('/usuarios?id=' + str(id))
            else:
                conn.execute(f"update usuarios set rol='ADMIN' where id='{rid}';")
                conn.commit()
                redirect('/usuarios?id=' + str(id))
        else:
            return '''
                <h1>ERROR - NECESITA PERMISOS DE CREADOR PARA ESTA TAREA.</h1>
                
                <button onClick="javascript:window.location.href='/inicio'">Volver al inicio</button>
            '''

conn.close()
run(host='localhost', port=8000, server='paste', reloader='True')
