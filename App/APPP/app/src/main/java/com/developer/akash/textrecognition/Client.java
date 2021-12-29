package com.developer.akash.textrecognition;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class Client extends Thread {
    String data ;

    public Client(String data) {
        this.data = data;
    }

    public void run(){
        ejecutarCliente(data);


    }

    private void ejecutarCliente(String data) {
        String ip = "192.168.0.13";
        int puerto = 1085;
        try{
            Socket sk = new Socket(ip,puerto);

            BufferedReader entrada = new BufferedReader(new
                    InputStreamReader(sk.getInputStream()));
            PrintWriter salida = new PrintWriter(
                    new OutputStreamWriter(sk.getOutputStream()),true);
            log("enviando ... Hola Mundo!");
            salida.println(data);
            salida.write("loleo");
            log("recibiendo ... " + entrada.readLine());
            sk.close();
        }
        catch (Exception e){
            log("error: " + e.toString());
        }

    }

    private void log(String cadena){
        //pantalla.append(cadena + "\n");

    }


}

