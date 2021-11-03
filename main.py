import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    cursor.execute("SELECT APELLIDO ,TELEFONO "
                   "FROM DOCTOR "
                   "INNER JOIN  HOSPITAL "
                   "ON (DOCTOR.HOSPITAL_COD=HOSPITAL.HOSPITAL_COD) "
                   "ORDER BY DOCTOR.APELLIDO")

    print("Lista de Doctores y Telefonos de donde trabajan:")
    print("---------------------------------------")

    for ape,numtel   in cursor:
            print("Apellido del Doctor:", ape, "Número de Teléfono:", numtel)


except connection.Error as error:
    print("Error: ", error)

connection.close()
