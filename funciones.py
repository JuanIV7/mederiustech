from bottle import request, run, route, redirect, template
import sqlite3

conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

def borrarrutina(rid = ""):
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    
    consulta_rutina1 = f"select id from rutinas where id='{rid}';"
    consulta_rutina2 = f"select id from rutinassemanales where id='{rid}';"
        
    if len(tuple(conn.execute(consulta_rutina1))):
        borrar_rutina1 = f"delete from rutinas where id='{rid}';"
        conn.execute(borrar_rutina1)
        conn.commit()
    elif len(tuple(conn.execute(consulta_rutina2))):
        borrar_rutina2 = f"delete from rutinassemanales where id='{rid}';"
        conn.execute(borrar_rutina2)
        conn.commit()

def recibirrutina1(id = "", var=""):
    luM1 = request.POST['lunMan1'];
    luM2 = request.POST['lunMan2'];
    luM3 = request.POST['lunMan3'];
    luT1 = request.POST['lunTar1'];
    luT2 = request.POST['lunTar2'];
    luT3 = request.POST['lunTar3'];
    luN1 = request.POST['lunNoc1'];
    luN2 = request.POST['lunNoc2'];
    luN3 = request.POST['lunNoc3'];
    maM1 = request.POST['marMan1'];
    maM2 = request.POST['marMan2'];
    maM3 = request.POST['marMan3'];
    maT1 = request.POST['marTar1'];
    maT2 = request.POST['marTar2'];
    maT3 = request.POST['marTar3'];
    maN1 = request.POST['marNoc1'];
    maN2 = request.POST['marNoc2'];
    maN3 = request.POST['marNoc3'];
    miM1 = request.POST['mieMan1'];
    miM2 = request.POST['mieMan2'];
    miM3 = request.POST['mieMan3'];
    miT1 = request.POST['mieTar1'];
    miT2 = request.POST['mieTar2'];
    miT3 = request.POST['mieTar3'];
    miN1 = request.POST['mieNoc1'];
    miN2 = request.POST['mieNoc2'];
    miN3 = request.POST['mieNoc3'];
    juM1 = request.POST['jueMan1'];
    juM2 = request.POST['jueMan2'];
    juM3 = request.POST['jueMan3'];
    juT1 = request.POST['jueTar1'];
    juT2 = request.POST['jueTar2'];
    juT3 = request.POST['jueTar3'];
    juN1 = request.POST['jueNoc1'];
    juN2 = request.POST['jueNoc2'];
    juN3 = request.POST['jueNoc3'];
    viM1 = request.POST['vieMan1'];
    viM2 = request.POST['vieMan2'];
    viM3 = request.POST['vieMan3'];
    viT1 = request.POST['vieTar1'];
    viT2 = request.POST['vieTar2'];
    viT3 = request.POST['vieTar3'];
    viN1 = request.POST['vieNoc1'];
    viN2 = request.POST['vieNoc2'];
    viN3 = request.POST['vieNoc3'];
    saM1 = request.POST['sabMan1'];
    saM2 = request.POST['sabMan2'];
    saM3 = request.POST['sabMan3'];
    saT1 = request.POST['sabTar1'];
    saT2 = request.POST['sabTar2'];
    saT3 = request.POST['sabTar3'];
    saN1 = request.POST['sabNoc1'];
    saN2 = request.POST['sabNoc2'];
    saN3 = request.POST['sabNoc3'];
    doM1 = request.POST['domMan1'];
    doM2 = request.POST['domMan2'];
    doM3 = request.POST['domMan3'];
    doT1 = request.POST['domTar1'];
    doT2 = request.POST['domTar2'];
    doT3 = request.POST['domTar3'];
    doN1 = request.POST['domNoc1'];
    doN2 = request.POST['domNoc2'];
    doN3 = request.POST['domNoc3'];
    id=int(id)
    if int(var)==0:
        lista_rutinas2=f"insert into rutinas(id,lunMan1,lunMan2,lunMan3,lunTar1,lunTar2,lunTar3,lunNoc1,lunNoc2,lunNoc3,marMan1,marMan2,marMan3,marTar1,marTar2,marTar3,marNoc1,marNoc2,marNoc3,mieMan1,mieMan2,mieMan3,mieTar1,mieTar2,mieTar3,mieNoc1,mieNoc2,mieNoc3,jueMan1,jueMan2,jueMan3,jueTar1,jueTar2,jueTar3,jueNoc1,jueNoc2,jueNoc3,vieMan1,vieMan2,vieMan3,vieTar1,vieTar2,vieTar3,vieNoc1,vieNoc2,vieNoc3,sabMan1,sabMan2,sabMan3,sabTar1,sabTar2,sabTar3,sabNoc1,sabNoc2,sabNoc3,domMan1,domMan2,domMan3,domTar1,domTar2,domTar3,domNoc1,domNoc2,domNoc3) values('{id}','{luM1}','{luM2}','{luM3}','{luT1}','{luT2}','{luT3}','{luN1}','{luN2}','{luN3}','{maM1}','{maM2}','{maM3}','{maT1}','{maT2}','{maT3}','{maN1}','{maN2}','{maN3}','{miM1}','{miM2}','{miM3}','{miT1}','{miT2}','{miT3}','{miN1}','{miN2}','{miN3}','{juM1}','{juM2}','{juM3}','{juT1}','{juT2}','{juT3}','{juN1}','{juN2}','{juN3}','{viM1}','{viM2}','{viM3}','{viT1}','{viT2}','{viT3}','{viN1}','{viN2}','{viN3}','{saM1}','{saM2}','{saM3}','{saT1}','{saT2}','{saT3}','{saN1}','{saN2}','{saN3}','{doM1}','{doM2}','{doM3}','{doT1}','{doT2}','{doT3}','{doN1}','{doN2}','{doN3}')"
        return lista_rutinas2
    else:
        lista_rutinas3=f"update rutinas set lunMan1='{luM1}',lunMan2='{luM2}',lunMan3='{luM3}',lunTar1='{luT1}',lunTar2='{luT2}',lunTar3='{luT3}',lunNoc1='{luN1}',lunNoc2='{luN2}',lunNoc3='{luN3}',marMan1='{maM1}',marMan2='{maM2}',marMan3='{maM3}',marTar1='{maT1}',marTar2='{maT2}',marTar3='{maT3}',marNoc1='{maN1}',marNoc2='{maN2}',marNoc3='{maN3}',mieMan1='{miM1}',mieMan2='{miM2}',mieMan3='{miM3}',mieTar1='{miT1}',mieTar2='{miT2}',mieTar3='{miT3}',mieNoc1='{miN1}',mieNoc2='{miN2}',mieNoc3='{miN3}',jueMan1='{juM1}',jueMan2='{juM2}',jueMan3='{juM3}',jueTar1='{juT1}',jueTar2='{juT2}',jueTar3='{juT3}',jueNoc1='{juN1}',jueNoc2='{juN2}',jueNoc3='{juN3}',vieMan1='{viM1}',vieMan2='{viM2}',vieMan3='{viM3}',vieTar1='{viT1}',vieTar2='{viT2}',vieTar3='{viT3}',vieNoc1='{viN1}',vieNoc2='{viN2}',vieNoc3='{viN3}',sabMan1='{saM1}',sabMan2='{saM2}',sabMan3='{saM3}',sabTar1='{saT1}',sabTar2='{saT2}',sabTar3='{saT3}',sabNoc1='{saN1}',sabNoc2='{saN2}',sabNoc3='{saN3}',domMan1='{doM1}',domMan2='{doM2}',domMan3='{doM3}',domTar1='{doT1}',domTar2='{doT2}',domTar3='{doT3}',domNoc1='{doN1}',domNoc2='{doN2}',domNoc3='{doN3}' where id='{id}';"
        print(lista_rutinas3)
        return lista_rutinas3

def recibirrutina2(id = "", var=""):
    pastLun1 = request.POST['pastLunes1'];
    pastLun2 = request.POST['pastLunes2'];
    pastLun3 = request.POST['pastLunes3'];
    pastMar1 = request.POST['pastMartes1'];
    pastMar2 = request.POST['pastMartes2'];
    pastMar3 = request.POST['pastMartes3'];
    pastMie1 = request.POST['pastMiercoles1'];
    pastMie2 = request.POST['pastMiercoles2'];
    pastMie3 = request.POST['pastMiercoles3'];
    pastJue1 = request.POST['pastJueves1'];
    pastJue2 = request.POST['pastJueves2'];
    pastJue3 = request.POST['pastJueves3'];
    pastVie1 = request.POST['pastViernes1'];
    pastVie2 = request.POST['pastViernes2'];
    pastVie3 = request.POST['pastViernes3'];
    pastSab1 = request.POST['pastSabado1'];
    pastSab2 = request.POST['pastSabado2'];
    pastSab3 = request.POST['pastSabado3'];
    pastDom1 = request.POST['pastDomingo1'];
    pastDom2 = request.POST['pastDomingo2'];
    pastDom3 = request.POST['pastDomingo3'];
    id=int(id)
    if int(var)==0:
        lista_rutinas1=f"insert into rutinassemanales(id,lunes1,lunes2,lunes3,martes1,martes2,martes3,miercoles1,miercoles2,miercoles3,jueves1,jueves2,jueves3,viernes1,viernes2,viernes3,sabado1,sabado2,sabado3,domingo1,domingo2,domingo3) values('{id}','{pastLun1}','{pastLun2}','{pastLun3}','{pastMar1}','{pastMar2}','{pastMar3}','{pastMie1}','{pastMie2}','{pastMie3}','{pastJue1}','{pastJue2}','{pastJue3}','{pastVie1}','{pastVie2}','{pastVie3}','{pastSab1}','{pastSab2}','{pastSab3}','{pastDom1}','{pastDom2}','{pastDom3}')"
        return lista_rutinas1
    else:
        lista_rutinas1=f"update rutinassemanales set lunes1='{pastLun1}',lunes2='{pastLun2}',lunes3='{pastLun3}',martes1='{pastMar1}',martes2='{pastMar2}',martes3='{pastMar3}',miercoles1='{pastMie1}',miercoles2='{pastMie2}',miercoles3='{pastMie3}',jueves1='{pastJue1}',jueves2='{pastJue2}',jueves3='{pastJue3}',viernes1='{pastVie1}',viernes2='{pastVie2}',viernes3='{pastVie3}',sabado1='{pastSab1}',sabado2='{pastSab2}',sabado3='{pastSab3}',domingo1='{pastDom1}',domingo2='{pastDom2}',domingo3='{pastDom3}' where id='{id}';"
        return lista_rutinas1
    