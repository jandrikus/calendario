import time
examenes={'7/1/2015':'Álgebra','9/1/2015':'Informática','16/1/2015':'Mecánica','21/1/2015':'Química','26/1/2015':'Cálculo'}
dias=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
mes={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
asignaturas={'Álgebra':['Teoría','Apuntes','Exámenes','Varios'],'Cálculo':['Teoría','Apuntes','Exámenes','Varios'],'Mecánica':['Teoría','Apuntes','Exámenes','Varios'],'Química':['Teoría','Apuntes','Exámenes','Varios'],'Informática':['Teoría','Apuntes','Exámenes','Varios']}


def crear_horario():
	biblio=makebiblio() #crea los intervalos de horas (en tuples) disponibles en la biblio durante las fechas
	home=makehome() #crea los intervalos de horas(en tuples) disponibles en casa durante las fechas
	nombre=input('Nombre? ')
	n=input('Numero? ')
	f=open(nombre+n,'w')
	f.write('Horarios en biblio:\n')
	f.write(biblio+'\n')
	f.write('Horarios en casa:\n')
	f.write(home+'\n')
	f.close()
	print('Se cerrará en 5 segundos')
	time.sleep(5)
	
	
def horas():
	horas=[]
	n=0
	while n<24:
		a='{0:02d}:00'.format(n)
		horas.append(a)
		a='{0:02d}:15'.format(n)
		horas.append(a)
		a='{0:02d}:30'.format(n)
		horas.append(a)
		a='{0:02d}:45'.format(n)
		horas.append(a)
		n+=1
	return horas
	
def calendario(N,M,A,D,I,F):
	"""fecha=input('Fecha de hoy en formato D/M/AAAA: ')
	D=input('Día de la semana actual (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=input('Fecha inicial del calendario en formato D/M/AAAA: ')
	F=input('Fecha final del calendario en formato D/M/AAAA: ')
	fecha=fecha.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])"""
	N_inicio=N
	M_inicio=M
	A_inicio=A
	D_inicio=D
	a=''
	calen1={}
	while a!=F:
		a='{0}/{1}/{2}'.format(N_inicio,M_inicio,A_inicio)
		b='{0}'.format(D_inicio)
		calen1[a]=b
		if D_inicio=='domingo':
			D_inicio=dias[0]
			if mes[M_inicio]==N_inicio and M_inicio==12:
				M_inicio=1
				A_inicio+=1
				N_inicio=0
			elif M_inicio==2 and A_inicio%4==0:
				if mes[M_inicio]+1==N_inicio:
					M_inicio+=1
					N_inicio=0
			elif mes[M_inicio]==N_inicio:
				M_inicio+=1
				N_inicio=0
		else:
			D_inicio=dias[dias.index(D_inicio)+1]
			if mes[M_inicio]==N_inicio and M_inicio==12:
				M_inicio=1
				A_inicio+=1
				N_inicio=0
			elif M_inicio==2 and A_inicio%4==0:
				if mes[M_inicio]+1==N_inicio:
					M_inicio+=1
					N_inicio=0
			elif mes[M_inicio]==N_inicio:
				M_inicio+=1
				N_inicio=0
		N_inicio+=1
	N_inicio=N
	M_inicio=M
	A_inicio=A
	D_inicio=D
	a=''
	calen2={}
	while a!=I:
		a='{0}/{1}/{2}'.format(N_inicio,M_inicio,A_inicio)
		b='{0}'.format(D_inicio)
		calen2[a]=b
		if D_inicio=='lunes':
			D_inicio=dias[6]
			if N_inicio==1 and M_inicio==1:
				M_inicio=12
				A_inicio-=1
				N_inicio=mes[M_inicio]+1
			elif M_inicio==3 and A_inicio%4==0 and N_inicio==1:
				M_inicio=2
				N_inicio=mes[M_inicio]+2
			elif M_inicio==2 and mes[M_inicio]+1==N_inicio:
				pass
			elif N_inicio==1:
				M_inicio-=1
				N_inicio=mes[M_inicio]+1
		else:
			D_inicio=dias[dias.index(D_inicio)-1]
			if N_inicio==1 and M_inicio==1:
				M_inicio=12
				A_inicio-=1
				N_inicio=mes[M_inicio]+1
			elif M_inicio==3 and A_inicio%4==0 and N_inicio==1:
				M_inicio=2
				N_inicio=mes[M_inicio]+2
			elif M_inicio==2 and mes[M_inicio]+1==N_inicio:
				pass
			elif N_inicio==1:
				M_inicio-=1
				N_inicio=mes[M_inicio]+1
		N_inicio-=1
	a='{0}/{1}/{2}'.format(N,M,A)
	del calen2[a]
	calen=calen1.copy()
	calen.update(calen2)
	return calen

def avance(N_inicio,M_inicio,A_inicio):
	a='{0}/{1}/{2}'.format(N_inicio,M_inicio,A_inicio)
	if mes[M_inicio]==N_inicio and M_inicio==12:
		M_inicio=1
		A_inicio+=1
		N_inicio=0
	elif M_inicio==2 and A_inicio%4==0:
		if mes[M_inicio]+1==N_inicio:
			M_inicio+=1
			N_inicio=0
	elif mes[M_inicio]==N_inicio:
		M_inicio+=1
		N_inicio=0
	N_inicio+=1
	a='{0}/{1}/{2}'.format(N_inicio,M_inicio,A_inicio)
	return (a,N_inicio,M_inicio,A_inicio)

def biblio_antes_nav():
	biblio={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio antes de las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')	
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if calend[I]=='martes':
				biblio[calend[I]][I]=[('15:00','20:00')]
			elif calend[I]=='jueves':
				biblio[calend[I]][I]=[('15:00','20:00')]
		(I,N,M,A)=avance(N,M,A)
	return biblio	
	
def biblio_apartir_8():
	biblio={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio después de las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')	
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if I in examenes:
				biblio[calend[I]][I]=[(examenes[I])]
			elif calend[I]=='lunes':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='martes':
				biblio[calend[I]][I]=[('15:00','20:00')]
			elif calend[I]=='miércoles':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='jueves':
				biblio[calend[I]][I]=[('15:00','20:00')]
			elif calend[I]=='viernes':
				biblio[calend[I]][I]=[('09:00','14:00')]
		(I,N,M,A)=avance(N,M,A)
	return biblio
	
def biblio_vacaciones():
	biblio={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio durante las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if calend[I]=='lunes':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='martes':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='miércoles':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='jueves':
				biblio[calend[I]][I]=[('09:00','14:00')]
			elif calend[I]=='viernes':
				biblio[calend[I]][I]=[('09:00','14:00')]
		(I,N,M,A)=avance(N,M,A)
	return biblio

def makebiblio():
	print("Primero obtendremos los días de biblioteca antes de las vacaciones de navidad")
	biblio_antes=biblio_antes_nav()
	print("Segundo obtendremos los días de biblioteca durante las vacaciones de navidad")
	biblio_vacas=biblio_vacaciones()
	print("Tercero obtendremos los días de biblioteca después de las vacaciones de navidad")
	biblio_enero=biblio_apartir_8()
	biblio=biblio_antes.copy()
	"""for i in biblio_vacas:
		if i in biblio:
			biblio[i]+=[biblio_vacas[i]]
		else:
			biblio[i]=[biblio_vacas[i]]
	for i in biblio_enero:
		if i in biblio:
			biblio[i]+=[biblio_enero[i]]
		else:
			biblio[i]=[biblio_enero[i]]
	
	biblio.update(biblio_vacas)
	biblio.update(biblio_enero)
	"""
	return biblio

def home_antes():
	home={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio antes de las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if calend[I]=='lunes':
				home[calend[I]][I]=[('14:00','18:00'),('22:00','01:00')]
			elif calend[I]=='miércoles':
				home[calend[I]][I]=[('14:00','18:00'),('22:30','01:00')]
			elif calend[I]=='viernes':
				home[calend[I]][I]=[('14:00','17:30'),('21:30','01:00')]
		(I,N,M,A)=avance(N,M,A)
	return home	
	
def home_durante():
	home={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio durante las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if calend[I]=='lunes':
				home[calend[I]][I]=[('15:00','21:00'),('22:00','01:00')]
			elif calend[I]=='martes':
				home[calend[I]][I]=[('15:00','21:00'),('22:00','01:00')]
			elif calend[I]=='miércoles':
				home[calend[I]][I]=[('15:00','21:00'),('22:00','01:00')]
			elif calend[I]=='jueves':
				home[calend[I]][I]=[('15:00','21:00'),('22:00','01:00')]
			elif calend[I]=='viernes':
				home[calend[I]][I]=[('15:00','21:00'),('22:00','01:00')]
		(I,N,M,A)=avance(N,M,A)
	return home	

def home_despues():
	home={'lunes':{},'martes':{},'miércoles':{},'jueves':{},'viernes':{}}
	fecha=input('Fecha inicial del calendario de estudio después de las vacaciones de navidad en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if I in examenes:
				home[calend[I]][I]=[(examenes[I])]
			elif calend[I]=='lunes':
				home[calend[I]][I]=[('15:30','18:00'),('22:00','01:00')]
			elif calend[I]=='martes':
				home[calend[I]][I]=[('09:00','13:00'),('22:00','01:00')]
			elif calend[I]=='miércoles':
				home[calend[I]][I]=[('15:30','18:00'),('22:30','01:00')]
			elif calend[I]=='jueves':
				home[calend[I]][I]=[('09:00','13:00'),('22:00','01:00')]
			elif calend[I]=='viernes':
				home[calend[I]][I]=[('15:00','17:30'),('21:30','01:00')]
		(I,N,M,A)=avance(N,M,A)
	return home

def findes():
	finde={'sábado':{},'domingo':{}}
	fecha=input('Fecha inicial del calendario de estudio de finde de semana en formato D/M/AAAA: ')
	D=input('Día de la semana de esa fecha (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I=fecha
	F=input('Fecha final del calendario de estudio en formato D/M/AAAA: ')
	fecha=I.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
	calend=calendario(N,M,A,D,I,F)
	x=input('Quieres quitar fechas entre medio? Si/No: ')
	if x=='Si':
		print('Introduce una fecha en formato D/M/AAAA que desees eliminar, cuando hayas acabado, escribe -1')
		y=input('Fecha: ')
		while y!='-1':
			del calend[y]
			y=input('Fecha: ')
	fecha2=I.split('/')
	N=int(fecha2[0])
	M=int(fecha2[1])
	A=int(fecha2[2])
	while I!=F:
		if I in calend:
			if calend[I]=='sábado':
				finde[calend[I]][I]=[('10:00','14:00'),('15:00','01:00')]
			elif calend[I]=='domingo':
				if I=='14/12/14' or I=='11/1/15' or I=='18/1/15':
					finde[calend[I]][I]=[('10:00','13:30'),('18:30','01:00')]
				else:
					finde[calend[I]][I]=[('10:00','13:30'),('14:30','01:00')]
		(I,N,M,A)=avance(N,M,A)
	return finde
	
def makehome():
	print("Primero obtendremos los días de estudio en casa antes de las vacaciones de navidad")
	home_ant=home_antes()
	print("Segundo obtendremos los días de estudio en casa durante las vacaciones de navidad")
	home_dur=home_durante()
	print("Tercero obtendremos los días de estudio en casa después de las vacaciones de navidad")
	home_des=home_despues()
	print("Cuarto obtendremos los días de estudio en casa en fin de semana")
	home_finde=findes()
	home=home_ant.copy()
	"""for i in home_dur:
		if i in home:
			home[i]+=[home_dur[i]]
		else:
			home[i]=[home_dur[i]]
	for i in home_des:
		if i in home:
			home[i]+=[home_des[i]]
		else:
			home[i]=[home_des[i]]
	for i in home_finde:
		if i in home:
			home[i]+=[home_finde[i]]
		else:
			home[i]=[home_finde[i]]
	
	home.update(home_dur)
	home.update(home_des)
	home.update(home_finde)
	"""
	return home



crear_horario()
