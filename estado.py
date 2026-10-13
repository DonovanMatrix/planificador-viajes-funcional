from dataclasses import dataclass
# ===== DATACLASS =====

@dataclass
class Viaje:
    destino: str
    presupuesto: float
    dias: int
    tipo: str
# ===== ESTADO =====

viajes = []
