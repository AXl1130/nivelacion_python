from abc import ABC, abstractmethod

class VehiculoBase(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        """Método abstracto para encender el vehículo"""
        pass

    @abstractmethod
    def __str__(self):
        """Método abstracto para representar el objeto como texto"""
        pass

class SistemaMotor:
    def __init__(self, tipo_combustible: str, capacidad_tanque: float):
        self.tipo_combustible = tipo_combustible
        self.capacidad_tanque = capacidad_tanque
        self.nivel_combustible = 0.0

    def repostar(self, litros: float):
        self.nivel_combustible += litros
        if self.nivel_combustible > self.capacidad_tanque:
            self.nivel_combustible = self.capacidad_tanque
        print(f"Repostaje completado. Nivel actual: {self.nivel_combustible}L de {self.tipo_combustible}")

class SistemaRastreo:
    def __init__(self):
        self.gps_activado = False

    def encender_gps(self):
        self.gps_activado = True
        print("El sistema de rastreo satelital (GPS) ha sido activado.")

class VehiculoInteligente(VehiculoBase, SistemaMotor, SistemaRastreo):
    def __init__(self, marca: str, modelo: str, tipo_combustible: str, capacidad_tanque: float, kilometraje_inicial: float = 0.0):
        VehiculoBase.__init__(self, marca, modelo)
        SistemaMotor.__init__(self, tipo_combustible, capacidad_tanque)
        SistemaRastreo.__init__(self)
        
        self._kilometraje = kilometraje_inicial

    @property
    def kilometraje(self) -> float:
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, nuevo_kilometraje: float):
        if not isinstance(nuevo_kilometraje, (int, float)):
            print(f"Error: El kilometraje debe ser un número (valor intentado: {nuevo_kilometraje}).")
            return
        
        if nuevo_kilometraje < self._kilometraje:
            print(f"Error: Movimiento inválido. El kilometraje nuevo ({nuevo_kilometraje}) no puede ser menor al actual ({self._kilometraje}).")
            return
            
        self._kilometraje = nuevo_kilometraje
        print(f"El kilometraje mediante 'setter' se ha actualizado a: {self._kilometraje} km")

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} se está encendiendo y verificando todos los sistemas...")

    def __str__(self):
        estado_gps = "Activado" if self.gps_activado else "Desactivado"
        return f"[Vehículo Inteligente] {self.marca} {self.modelo} | {self.tipo_combustible} | GPS: {estado_gps} | Kilometraje: {self.kilometraje} km"


if __name__ == "__main__":
    print("-" * 50)
    print("INSTANCIACIÓN DE 3 OBJETOS (POLIMORFISMO Y PRUEBAS)")
    print("-" * 50)

    coche1 = VehiculoInteligente("Toyota", "Corolla", "Gasolina", 45.0, 15000)
    coche2 = VehiculoInteligente("Tesla", "Model S", "Eléctrico", 100.0, 5000)
    coche3 = VehiculoInteligente("Ford", "Ranger", "Diesel", 65.0, 120000)

    lista_vehiculos = [coche1, coche2, coche3]

    print("\n--- Demostrando Polimorfismo y herencia ---")
    for vehiculo in lista_vehiculos:
        vehiculo.encender()
        print(vehiculo)
        print()

    print("--- Pruebas de otras clases padre (Herencia Múltiple) ---")
    coche1.repostar(20)
    coche2.encender_gps()

    print("\n--- Prueba de Encapsulamiento con Setter/Getter y Validaciones ---")
    
    print(f"Kilometraje actual del coche 3: {coche3.kilometraje} km")
    
    print("\nPrueba 1: Aumentamos el kilometraje de 120,000 a 120,500...")
    coche3.kilometraje = 120500 
    print("\nPrueba 2: Intentamos 'fraude' bajando el kilometraje a 50,000...")
    coche3.kilometraje = 50000

    print("\nPrueba 3: Asignar un valor no numérico...")
    coche3.kilometraje = "cien mil"

    print(f"\nResultado final de los atributos encapsulados: {coche3}")
