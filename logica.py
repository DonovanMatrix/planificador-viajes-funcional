from functools import reduce
from estado import Viaje, viajes


def agregar_viaje(destino, presupuesto, dias, tipo):

    viaje = Viaje(
        destino,
        presupuesto,
        dias,
        tipo
    )

    viajes.append(viaje)

    return recomendacion(tipo)


def mostrar_viajes():
    return viajes


def presupuesto_total():

    if not viajes:
        return 0

    presupuestos = list(
        map(lambda v: v.presupuesto, viajes)
    )

    return reduce(
        lambda a, b: a + b,
        presupuestos,
        0
    )


def viajes_economicos():

    return list(
        filter(
            lambda v: v.presupuesto < 200,
            viajes
        )
    )


def ordenar_viajes():

    return sorted(
        viajes,
        key=lambda v: v.presupuesto
    )


def recomendacion(tipo):

    match tipo:

        case "Playa":
            return "Ideal para descansar junto al mar."

        case "Aventura":
            return "Perfecto para actividades extremas."

        case "Cultural":
            return "Excelente para conocer historia y tradiciones."

        case "Negocios":
            return "Orientado a reuniones profesionales."

        case "Ecoturismo":
            return "Ideal para disfrutar la naturaleza."

        case "Gastronómico":
            return "Perfecto para descubrir nuevos sabores."

        case _:
            return "Disfruta tu viaje."


def crear_descuento(porcentaje):

    def descuento(valor):
        return valor * (1 - porcentaje)

    return descuento


def aplicar_descuento():

    descuento10 = crear_descuento(0.10)

    return [
        (v.destino, descuento10(v.presupuesto))
        for v in viajes
    ]


def viaje_mas_barato():

    if not viajes:
        return None

    return min(
        viajes,
        key=lambda v: v.presupuesto
    )


def viaje_mas_caro():

    if not viajes:
        return None

    return max(
        viajes,
        key=lambda v: v.presupuesto
    )


def presupuesto_promedio():

    if not viajes:
        return 0

    return sum(
        v.presupuesto for v in viajes
    ) / len(viajes)