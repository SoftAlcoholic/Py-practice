# -*- coding: utf-8 -*-
continuee = "s"
def password_verification(contra,confirm):
    if contra==confirm:
        verif= True
    else:
        verif= False
    return verif
while continuee=="s":
    contra = int(input("ingrese una contraseña numerica  mmgvo: \n"))
    confirm = int(input("confirme su contraseña: \n"))
    pssvrf= password_verification(contra, confirm)
    if pssvrf==True:
        print("contraseña definida correctamente")
    elif pssvrf==False:
        print("las contraseñas no coinciden vuelva a intentarlo")
    else:
        pass
    continuee=input("desea continuar? (s/n) \n")
