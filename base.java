import java.sql.*;

public class base {
    public static void main(String[] args) {
        try {
            // Registrar el driver (necesario con el jar viejo)
            Class.forName("com.mysql.jdbc.Driver");

            // Conexión (root sin contraseña)
            Connection conexion = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/prueba", "root", "");

            // Consulta
            Statement s = conexion.createStatement();
            ResultSet rs = s.executeQuery("select * from persona");

            // Recorrer resultados
            while (rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2) + " " + rs.getDate(3));
            }

            // Cerrar
            rs.close();
            s.close();
            conexion.close();

        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
