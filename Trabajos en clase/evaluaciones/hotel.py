import fcs_hotel

hotel = fcs_hotel.cargar_datos()

while True:
    fcs_hotel.mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción del menú: "))
        
        match opcion:
            case 1:
                print(fcs_hotel.mostrar_habitaciones(hotel))
            case 2:
                pass
            case 3:
                hotel = fcs_hotel.actualizar_estado(hotel)
            case 4:
                hotel = fcs_hotel.eliminar_habitacion(hotel)
            case 5:
                fcs_hotel.mostrar_disponibles(hotel)
            case 6:
                hotel = fcs_hotel.agregar_habitacion(hotel)
            case 7:
                hotel = fcs_hotel.reservar_liberar(hotel)
            case 8:
                print('Hasta luego')
                break
            case 9:
                hotel = fcs_hotel.agregar_habitaciones(hotel)
            case _:
                print('Opción inválida.')
            
    except ValueError:
        print('Opción inválida.')
