print("""
    == Bienvenidos ==
    Sistema de cálculo de área y perímetro
    de la circunferencia
    ==========================================================================

    ███████╗████████╗███████╗██╗   ██╗
    ██╔════╝╚══██╔══╝██╔════╝██║   ██║
    ███████╗   ██║   █████╗  ██║   ██║
    ╚════██║   ██║   ██╔══╝  ╚██╗ ██╔╝
    ███████║   ██║   ███████╗ ╚████╔╝ 
    ╚══════╝   ╚═╝   ╚══════╝  ╚═══╝  

    ██████╗ ██████╗ ██████╗ ███████╗ ██████╗ ██╗     
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██║     
    ██║     ██║   ██║██║  ██║█████╗  ██║   ██║██║     
    ██║     ██║   ██║██║  ██║██╔══╝  ██║   ██║██║     
    ╚██████╗╚██████╔╝██████╔╝███████╗╚██████╔╝███████╗
    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝
    ==========================================================================
    """)

while(True):
    area = 0
    peri = 0
    print("Area y Perimetro de la circuferencia")
    print("======================================")
    print()

    radio = float(input("Ingrese radio:"))
    area = 3.14*radio*radio
    peri = 2*3.14*radio
    print("Mostrando Resultados")
    print("Area    : ", round(area, 2))
    print("Perimetro    : ", round(peri, 2))
    print()

    while(True):
        try:
            op = int(input("Deseas continuar : SI=1 / NO=0 "))
            if(op==0 or op==1):
                break
            else:
                print("Opción no válida")
        except:
            print("Opción no válida, no letras")

    if(op==0):
        break

print("Usted a terminado el programa")
print("Visitanos en www.codeolsoftware.wok")



