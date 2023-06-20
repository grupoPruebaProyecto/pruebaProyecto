import sqlite3

conexion = sqlite3.connect("ProyectoFinal")
comando = conexion.cursor()
# comando.execute ("CREATE TABLE Consulta_leyes (NRO_REGISTRO integer, TIPO_NORMATIVA varchar (15), NRO_NORMATIVA integer, FECHA varchar (15), DESCRIPCION varchar (1000), CATEGORIA varchar (15), JURISDICCION varchar (15), ORGANO_LEGISLATIVO varchar (35), PALABRA_CLAVE varchar(35))")


class Leyes:
    def _init_(self, numero, tipo_normativa, nroNormativa, fecha, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave):
        self.numero = numero
        self.tipo = tipo_normativa
        self.nroNormativa = nroNormativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organo_legislativo = organo_legislativo
        self.palabras_clave = palabras_clave


class BD_Leyes:
    def _init_(self):
        self.conexion = sqlite3.connect("ProyectoFinal")
        self.cursor = self.conexion.cursor()
        self.conexion.commit()

    def Tipo_normativa(self, tipo, descripcion):
        self.cursor.execute("INSERT INTO Consulta_Leyes (Tipo_normativa, descripcion) VALUES (?, ?)", (tipo, descripcion))
        self.conexion.commit()
        print("Ley insertada exitosamente.")

    def Categoria_Normativa(self, categoria, descripcion):
        self.cursor.execute("INSERT INTO Consulta_Leyes (categoria, descripcion) VALUES (?, ?)", (categoria, descripcion))
        self.conexion.commit()
        print("Categoría insertada exitosamente.")

    def jurisdiccion(self, jurisdiccion, descripcion, org_legislativo):
        self.cursor.execute(
            "INSERT INTO Consulta_Leyes (jurisdiccion, descripcion, organo_legislativo) VALUES (?, ?, ?)",
            (jurisdiccion, descripcion, org_legislativo)
        )
        self.conexion.commit()
        print("Jurisdicción insertada exitosamente")

    def eliminar_Ley(self, NRO_REGISTRO):
        self.cursor.execute("DELETE FROM Consulta_Leyes WHERE id = ?", (NRO_REGISTRO,))
        self.conexion.commit()
        print("Ley eliminada exitosamente.")

    def seleccionar_Ley(self):
        self.cursor.execute("SELECT * FROM Consulta_leyes")
        Ley = self.cursor.fetchall()
        for Ley in Ley:
            print(Ley)

    def cerrar_conexion(self):
        self.conexion.close()


def main():
    base_datos = BD_Leyes()

    while True:
        print("\n--- Menú ---")
        print("1. Insertar Ley")
        print("2. Mostrar Ley")
        print("3. Actualizar Ley")
        print("4. Eliminar Ley")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            numero = input("Ingrese el número de ley: ")
            tipo = input("Ingrese el tipo de normativa: ")
            nroNormativa = int(input("Ingrese el número de normativa: "))
            fecha = input("Ingrese la fecha: ")
            descripcion = input("Ingrese la descripción: ")
            categoria = input("Ingrese la categoría: ")
            jurisdiccion = input("Ingrese la jurisdicción: ")
            organo_legislativo = input("Ingrese el órgano legislativo: ")
            palabras_clave = input("Ingrese las palabras clave (separadas por comas): ")

            ley = Leyes(numero, tipo, nroNormativa, fecha, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave)

            base_datos.Tipo_normativa(tipo, ley.descripcion)
            base_datos.Categoria_Normativa(ley.categoria, ley.descripcion)
            base_datos.jurisdiccion(ley.jurisdiccion, ley.descripcion, ley.organo_legislativo)

        elif opcion == "2":
            base_datos.seleccionar_Ley()

        elif opcion == "3":
            id_registro = input("Ingrese el ID de la ley que desea actualizar: ")
            base_datos.cursor.execute("SELECT * FROM Consulta_leyes WHERE NRO_REGISTRO = ?", (id_registro,))
            ley = base_datos.cursor.fetchone()

            if ley is None:
                print("No se encontró la ley con el ID proporcionado.")
            else:
                print("Datos actuales de la ley:")
                print("Número:", ley[0])
                print("Tipo de normativa:", ley[1])
                print("Número de normativa:", ley[2])
                print("Fecha:", ley[3])
                print("Descripción:", ley[4])
                print("Categoría:", ley[5])
                print("Jurisdicción:", ley[6])
                print("Órgano legislativo:", ley[7])
                print("Palabras clave:", ley[8])

                campo = input("Ingrese el campo que desea actualizar: ")
                nuevo_valor = input("Ingrese el nuevo valor para ese campo: ")

                base_datos.cursor.execute(
                    "UPDATE Consulta_leyes SET {} = ? WHERE NRO_REGISTRO = ?".format(campo),
                    (nuevo_valor, id_registro)
                )
                base_datos.conexion.commit()

                print("Ley actualizada exitosamente.")

        elif opcion == "4":
            id_registro = input("Ingrese el ID de la ley que desea eliminar: ")
            base_datos.eliminar_Ley(id_registro)

        elif opcion == "5":
            base_datos.cerrar_conexion()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "_main_":
 main()

 #prueba de rama milena