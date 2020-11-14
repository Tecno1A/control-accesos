sesion = input(prompt='Identificador de la sesion: \n')
cod = input(prompt='Escanea el código: \n')

s1=cod.replace('Ñ','/')
s2=s1.replace('¨/¨',' = ')
s3=s2.replace('^¨grupos¨/`','\n grupos = ')
s4=s3.replace('+,ëspacio','\n\n espacio')
s5=s4.replace('¨,¨fecha','\n fecha ')
s6=s5.replace('¨,ïd =','\n ID_reg = ')
s7=s6.replace('¨,ïnstalacion','\n instalacion')
s8=s7.replace('^¨ëntrenador','\n\n ENTRENADOR')
s8a=s8.replace('^¨entrenador','\n\n ENTRENADOR')
s9=s8a.replace('¨,¨grupo¨/','\n grupo entrenamiento = ')
s10=s9.replace('¨,örganizacion','\n entidad')
s11=s10.replace('¨,¨sesion¨/^¨deportistas¨/`','\n\n subgrupos y datos sesión: \n')
s12=s11.replace('+,ïd¨/','  ID_dep: ')
s13=s12.replace('*,',' ')
s14=s13.replace('¨**',' ')
s14=s13.replace('*',' ')

datos=s14
print('\n\n',sesion,'\n\n',datos)
print('ahora hacemos un archivo con los datos '\n\n')  #linea para depurar
sesion = input(prompt='cambia el nombre para el archivo, si lo deseas:  '+sesion \n')

arch=sesion+'txt'
f = open(sesion,'w')
f.write(datos) # almacenar objeto en un archivo con formato json
f.close() 






