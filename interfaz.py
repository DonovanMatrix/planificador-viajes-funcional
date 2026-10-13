import ttkbootstrap as ttk
from tkinter import END

from logica import *


def crear_interfaz():

    app = ttk.Window(themename="flatly")

    app.title("Planificador de Viajes")
    app.geometry("900x700")

    titulo = ttk.Label(
        app,
        text="Planificador de Viajes Inteligente",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=10)

    ttk.Label(app, text="Destino").pack()

    entry_destino = ttk.Entry(app, width=40)
    entry_destino.pack()

    ttk.Label(app, text="Presupuesto").pack()

    entry_presupuesto = ttk.Entry(app, width=40)
    entry_presupuesto.pack()

    ttk.Label(app, text="Días").pack()

    entry_dias = ttk.Entry(app, width=40)
    entry_dias.pack()

    ttk.Label(app, text="Tipo de viaje").pack()

    combo_tipo = ttk.Combobox(
        app,
        values=[
            "Playa",
            "Aventura",
            "Cultural",
            "Negocios",
            "Ecoturismo",
            "Gastronómico"
        ]
    )

    combo_tipo.pack()
    combo_tipo.current(0)

    resultado = ttk.Text(
        app,
        height=15,
        width=80
    )

    def limpiar():
        resultado.delete(1.0, END)

    def agregar():

        try:
            destino = entry_destino.get()
            presupuesto = float(
                entry_presupuesto.get()
            )
            dias = int(
                entry_dias.get()
            )
            tipo = combo_tipo.get()

            mensaje = agregar_viaje(
                destino,
                presupuesto,
                dias,
                tipo
            )

            limpiar()

            resultado.insert(
                END,
                f"Viaje agregado\n{mensaje}"
            )

        except ValueError:

            limpiar()

            resultado.insert(
                END,
                "Datos inválidos"
            )

    def mostrar():

        limpiar()

        for v in mostrar_viajes():

            resultado.insert(
                END,
                f"{v.destino} | "
                f"${v.presupuesto} | "
                f"{v.dias} días | "
                f"{v.tipo}\n"
            )

    def total():

        limpiar()

        resultado.insert(
            END,
            f"Total: ${presupuesto_total():.2f}"
        )

    def economicos():

        limpiar()

        for v in viajes_economicos():

            resultado.insert(
                END,
                f"{v.destino} - "
                f"${v.presupuesto}\n"
            )

    def ordenar():

        limpiar()

        for v in ordenar_viajes():

            resultado.insert(
                END,
                f"{v.destino} - "
                f"${v.presupuesto}\n"
            )

    def descuento():

        limpiar()

        for destino, precio in aplicar_descuento():

            resultado.insert(
                END,
                f"{destino}: ${precio:.2f}\n"
            )

    def barato():

        limpiar()

        v = viaje_mas_barato()

        if v:

            resultado.insert(
                END,
                f"Más barato:\n"
                f"{v.destino}\n"
                f"${v.presupuesto}"
            )

    def caro():

        limpiar()

        v = viaje_mas_caro()

        if v:

            resultado.insert(
                END,
                f"Más caro:\n"
                f"{v.destino}\n"
                f"${v.presupuesto}"
            )

    def promedio():

        limpiar()

        resultado.insert(
            END,
            f"Promedio: "
            f"${presupuesto_promedio():.2f}"
        )

    ttk.Button(
        app,
        text="Agregar Viaje",
        bootstyle="success",
        command=agregar
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Mostrar Viajes",
        bootstyle="info",
        command=mostrar
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Presupuesto Total",
        bootstyle="warning",
        command=total
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Viajes Económicos",
        bootstyle="secondary",
        command=economicos
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Ordenar por Presupuesto",
        bootstyle="dark",
        command=ordenar
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Aplicar 10% Descuento",
        bootstyle="success",
        command=descuento
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Viaje Más Barato",
        bootstyle="info",
        command=barato
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Viaje Más Caro",
        bootstyle="danger",
        command=caro
    ).pack(pady=5)

    ttk.Button(
        app,
        text="Presupuesto Promedio",
        bootstyle="primary",
        command=promedio
    ).pack(pady=5)

    resultado.pack(pady=20)

    return app