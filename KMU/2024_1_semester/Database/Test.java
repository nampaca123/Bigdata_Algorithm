import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Types;

public class Test {
    public static void main(String[] args) {
        String url = "jdbc:oracle:thin:@localhost:1521:xe";
        // 프로시저 호출 형식 변경: 커서 대신 OUT 매개변수 사용
        String sql = "{call Interest(?)}"; 

        try {
            // JDBC 드라이버 로드
            Class.forName("oracle.jdbc.driver.OracleDriver");
            // 데이터베이스 연결
            Connection con = DriverManager.getConnection(url, "c##madang", "madang");
            // 프로시저 호출을 위한 CallableStatement 준비
            CallableStatement cstmt = con.prepareCall(sql);
            // OUT 매개변수 설정
            cstmt.registerOutParameter(1, Types.NUMERIC);
            // 프로시저 실행
            cstmt.execute();
            // 계산된 이익을 OUT 매개변수로부터 받음
            double interest = cstmt.getDouble(1);
            System.out.println("Calculated Interest: " + interest);
            
            cstmt.close();
            con.close();
        } catch (Exception err) {
            System.out.println("ERROR: " + err);
        }
    }
}
