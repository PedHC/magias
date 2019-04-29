import java.net.ServerSocket;
import java.io.IOException;
import java.util.Scanner;
import java.net.Socket;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.DataOutputStream;

public class ClienteThread extends Thread {
    protected Socket cliente;

    public ClienteThread(Socket clientSocket) {
        this.cliente = clientSocket;
    }

    public void run() {
        InputStream entrada = null;
        BufferedReader brinp = null;
        DataOutputStream saida = null;
        try {
            entrada = cliente.getInputStream();
            brinp = new BufferedReader(new InputStreamReader(entrada));
            saida = new DataOutputStream(cliente.getOutputStream());
        } catch (IOException e) {
            return;
        }
        String line;
        while (true) {
            try {
                line = brinp.readLine();
                if ((line == null) || line.equalsIgnoreCase("QUIT")) {
                    cliente.close();
                    return;
                } else {
                    saida.writeBytes(line + "\n\r");
                    saida.flush();
                }
            } catch (IOException e) {
                e.printStackTrace();
                return;
            }
        }
    }
}

public class Servidor {
    public static void main(String[] args) throws IOException {
	ServerSocket servidor = new ServerSocket(12345);
	System.out.println("Porta 12345 aberta!");


	while (true) {
	    Socket cliente = servidor.accept();
	    System.out.println("Nova conexao com o cliente " + cliente.getInetAddress().getHostAddress());

	    //gera a thread para o cliente:
	    new ClienteThread(cliente).start();
	    
	    
	}
	
	//servidor.close();
    }
}
