from abc import ABC, abstractmethod

class OrganismoBase(ABC):

    def __init__(self, nombre_cientifico, reino):
        self.nombre_cientifico = nombre_cientifico
        self.reino = reino

    @abstractmethod
    def realizar_metabolismo(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class SistemaReproductor:

    def __init__(self, tipo_reproduccion, tasa_reproduccion):
        self.tipo_reproduccion = tipo_reproduccion
        self.tasa_reproduccion = tasa_reproduccion
        self.ciclos_realizados = 0

    def reproducirse(self):
        self.ciclos_realizados += 1
        print(f"La celula se reprodujo! ya van {self.ciclos_realizados} veces")
        print(f"Tipo de reproduccion: {self.tipo_reproduccion}, velocidad: {self.tasa_reproduccion} por hora")


class SistemaDefensa:

    def __init__(self):
        self.barrera_activa = False
        self.nivel_anticuerpos = 0.0

    def activar_defensa(self):
        self.barrera_activa = True
        print("Se activo la defensa! el sistema inmune esta listo")

    def producir_anticuerpos(self, cantidad):
        self.nivel_anticuerpos += cantidad
        print(f"Se produjeron {cantidad} anticuerpos, ahora hay {self.nivel_anticuerpos} en total")


class Celula(OrganismoBase, SistemaReproductor, SistemaDefensa):

    def __init__(self, nombre_cientifico, reino, tipo_reproduccion, tasa_reproduccion, energia_inicial=0.0):
        OrganismoBase.__init__(self, nombre_cientifico, reino)
        SistemaReproductor.__init__(self, tipo_reproduccion, tasa_reproduccion)
        SistemaDefensa.__init__(self)

        self._energia = energia_inicial

    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, nuevo_valor):
        if not isinstance(nuevo_valor, (int, float)):
            print(f"Error: eso no es un numero, intenta de nuevo (pusiste: {nuevo_valor})")
            return
        if nuevo_valor < 0:
            print(f"Error: la energia no puede ser negativa, una celula no funciona asi (pusiste: {nuevo_valor})")
            return
        if nuevo_valor > 10000:
            print(f"Error: ese valor es demasiado alto para una celula, el maximo es 10000 (pusiste: {nuevo_valor})")
            return
        self._energia = nuevo_valor
        print(f"Listo! la energia quedo en {self._energia} ATP")
    def realizar_metabolismo(self):
        costo = 50.0
        if self._energia >= costo:
            self._energia -= costo
            print(f"{self.nombre_cientifico} hizo metabolismo y gasto {costo} ATP, le quedan {self._energia}")
        else:
            print(f"{self.nombre_cientifico} no tiene suficiente energia para metabolizar, solo tiene {self._energia} ATP")
    def __str__(self):
        if self.barrera_activa:
            defensa = "si"
        else:
            defensa = "no"

        return (f"Celula: {self.nombre_cientifico} | Reino: {self.reino} | "
                f"Energia: {self._energia} ATP | Reproduccion: {self.tipo_reproduccion} | "
                f"Defensa activa: {defensa}")


if __name__ == "__main__":
    print("-" * 55)
    print("creando 3 celulas distintas para probar el codigo")
    print("-" * 55)

    celula1 = Celula("Escherichia coli",    "Bacteria", "Biparticion",    2.0,  500.0)
    celula2 = Celula("Paramecium caudatum", "Protista", "Fision binaria", 1.0,  300.0)
    celula3 = Celula("Saccharomyces sp.",   "Fungi",    "Gemacion",       0.5, 1200.0)

    lista_celulas = [celula1, celula2, celula3]

    print("\n--- probando polimorfismo con las 3 celulas ---")
    for celula in lista_celulas:
        celula.realizar_metabolismo()
        print(celula)
        print()

    print("--- probando herencia multiple ---")
    celula1.reproducirse()
    celula2.activar_defensa()
    celula3.producir_anticuerpos(75.0)
    print("\n--- probando el encapsulamiento (getter y setter) ---")

    print(f"\nenergia actual de celula3: {celula3.energia} ATP")

    print("\nPrueba 1: subimos la energia a 1500...")
    celula3.energia = 1500

    print("\nPrueba 2: intentamos poner energia negativa, deberia dar error...")
    celula3.energia = -200

    print("\nPrueba 3: intentamos poner 20000, que esta fuera del rango...")
    celula3.energia = 20000

    print("\nPrueba 4: intentamos poner un texto en vez de numero...")
    celula3.energia = "mucha"

    print(f"\ncomo quedo la celula3 al final: {celula3}")
