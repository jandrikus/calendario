dias=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
mes={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
from time import sleep
def calendario():
	fecha=input('Fecha de hoy en formato D/M/AAAA: ')
	D=input('Día de la semana actual (escribir exactamente lunes,martes,miércoles,jueves,viernes,sábado,domingo): ')
	I='1/1/1600'
	F='31/12/2100'
	fecha=fecha.split('/')
	N=int(fecha[0])
	M=int(fecha[1])
	A=int(fecha[2])
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
	
def buscador():
	print("Este programa devuelve el día de la semana de la fecha indicada. Para ello, hay que escribir la fecha actual de referencia, el día de la semana actual y la fecha deseada.")
	print("Este calendario funciona sólamente para los años entre 1600 y 2100, aunque la fiabilidad de siglos anteriores no es asegurada debido a posibles cambios históricos de calendario.")
	print("Gracias por utilizar este programa.")
	print("Autor: Alejandro Álvarez de Gracia Twitter: @jandrikus")
	print("\n")
	p=input('Fecha deseada en formato D/M/AAAA del día: ')
	calend=calendario()
	print("Día de la semana: "+calend[p])
	print("Esta ventana se cerrará en 10 segundos.")
	sleep(10)
	print("Saliendo...")
buscador()