import pyodbc
import sys
def ModeloNegocioADW(tabla):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ezesql;'
                          'Database=ModeloDeNegocio;'
                          'Trusted_Connection=yes;')

    mod = "D_" + tabla[4:]
    f = open(tabla, "w+")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + tabla + "'")
    column_data = cursor.columns(table=tabla, catalog='ModeloDeNegocio', schema='dbo').fetchall()
    query ="CREATE PROCEDURE INSERTAR_" + mod + "\n"
    for r in column_data:
            if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
                query +="@r_DWH_" + r.column_name + " " +  GetDataType(r) + ",\r"
    query +="@v_CantIns int = 0 OUTPUT, " + "\r"
    query +="@v_CantUpd int = 0 OUTPUT  " + "\r"
    query +="AS " "\r" + "BEGIN" + " \r\n" + "DECLARE @v_sqlcode int,@v_sqlerrm varchar(4000)" + "\r\n" + "BEGIN TRY" + "\n"
    query +="\tINSERT INTO " + mod + " ( \n"
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
                query + "\t\t, "+mod + "." +r.column_name + "\r"
            else:
                query + "\t\t, "+mod + "." +r.column_name + "\r"
                primer = 1;
    query += "  ) values ( "
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
                query += "\t\t, @r_DWH_" + r.column_name  + "\r"
            else:
                query += "\t\t, @r_DWH_" + r.column_name  + "\r"
                primer =1
    query +=" \t) \n"
    query +="\tSET @v_CantIns = @v_CantIns + 1 " + "\n" + "END TRY " + "\r\n " + "BEGIN CATCH " + "\n"
    query +="\nIF (ERROR_NUMBER() = 2627)\n"
    query +="\tBEGIN \n"
    query +="\tUPDATE "+ mod + " SET \n"
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
                query += "\t\t, "+mod + "." +r.column_name + " = @r_DWH_" + r.column_name + "\r"
            else:
                query += "\t\t "+mod + "." +r.column_name + " = @r_DWH_" + r.column_name + "\r"
                primer = 1
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            query += "\t\t WHERE " + mod + "." + r.column_name + " = @r_DWH_" + r.column_name +"\n"
            break;
    query += "\t\tSET @v_CantUpd = @v_CantUpd + @@ROWCOUNT "
    query +="END \n"
    query +="ELSE \n"
    query +="\tBEGIN \n"
    query +="\tSET @v_sqlcode = 50000 + ERROR_NUMBER() \n"
    query +="\tSET @v_sqlerrm = CAST(ERROR_NUMBER() AS VARCHAR) + ': ' + ERROR_MESSAGE() \n"
    query +="\t RAISERROR (@v_sqlcode,-1,-1, @v_sqlerrm) \n"
    query +="END \n"
    query +="END CATCH \n"
    query +="END \n"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(" COMMIT ")
    except pyodbc.Error as ex:
        print ("Error !!!!!" + ex.args[1])
    f.write(query)
    f.close()

def ModeloNegocio(tabla):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ezesql;'
                          'Database=ModeloDeNegocio;'
                          'Trusted_Connection=yes;')

   # tabla = "MOD_IataAeropuertos"
    mod = tabla
    f = open(tabla, "w+")
    cursor = conn.cursor()
   # cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + tabla + "'")
    column_data = cursor.columns(table=tabla, catalog='ModeloDeNegocio', schema='dbo').fetchall()
    if len(column_data) == 0:
        print("Error la tabla " + tabla + " no existe")
        return
    query = "CREATE PROCEDURE INSERTAR_" + mod + "\n"
    for r in column_data:
            if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
                query +="@r_DWH_" + r.column_name + " " + GetDataType(r) + ",\r"
    query +="@v_CantIns int = 0 OUTPUT, " + "\r"
    query +="@v_CantUpd int = 0 OUTPUT  " + "\r"
    query +="AS " "\r" + "BEGIN" + " \r\n" + "DECLARE @v_sqlcode int,@v_sqlerrm varchar(4000)" + "\r\n" + "BEGIN TRY" + "\n"
    query +="\tINSERT INTO " + mod + " ( \n"
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
               query += " \t\t, "+mod + "." +r.column_name  + "\r"
            else:
                query += "\t\t"+mod + "." +r.column_name  + "\r"
                primer = 1
    query += "  ) values ( "
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
                query  += "\t\t, @r_DWH_" + r.column_name + "\r"
            else:
                query  += "\t\t @r_DWH_" + r.column_name  + "\r"
                primer = 1
    query +=" \t) \n"
    query +="\tSET @v_CantIns = @v_CantIns + 1 " + "\n" + "END TRY " + "\r\n " + "BEGIN CATCH " + "\n"
    query +="\nIF (ERROR_NUMBER() = 2627)\n"
    query +="\tBEGIN \n"
    query +="\tUPDATE "+ mod + " SET \n"
    primer = 0
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            if primer != 0:
                query += "\t\t, "+mod + "." +r.column_name + " = @r_DWH_" + r.column_name + "\r"
            else:
                query += "\t\t "+mod + "." +r.column_name + " = @r_DWH_" + r.column_name + "\r"
                primer = 1
    for  r in column_data:
        if "identity" not in  r.type_name and r.column_name != "FecUltAct"  and r.column_name != "UsuUltAct" :
            query += "\t\t WHERE " + mod + "." + r.column_name + " = @r_DWH_" + r.column_name +"\n"
            break;
    query += "\t\tSET @v_CantUpd = @v_CantUpd + @@ROWCOUNT "
    query +="END \n"
    query +="ELSE \n"
    query +="\tBEGIN \n"
    query +="\tSET @v_sqlcode = 50000 + ERROR_NUMBER() \n"
    query +="\tSET @v_sqlerrm = CAST(ERROR_NUMBER() AS VARCHAR) + ': ' + ERROR_MESSAGE() \n"
    query +="\t RAISERROR (@v_sqlcode,-1,-1, @v_sqlerrm) \n"
    query +="END \n"
    query +="END CATCH \n"
    query +="END \n"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.execute(" COMMIT ")
    except pyodbc.Error as ex:
        print ("Error !!!!!" + ex.args[0])
    f.write(query)
    f.close()
def GetDataType(r):
    if "char" in r.type_name:
        return r.type_name + " ( " + str(r.column_size) + " ) " 
    if  r.type_name == "numeric" or r.type_name == "decimal":
        return r.type_name + " ( " + str(r.column_size) + " , "  + str(r.decimal_digits) + " ) " 
    return r.type_name
if __name__ == "__main__":
   ModeloNegocio(sys.argv[1])
