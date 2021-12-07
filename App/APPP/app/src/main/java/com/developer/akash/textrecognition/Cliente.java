package com.developer.akash.textrecognition;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class Cliente {
    private void ejecutaCliente(){
        String ip = "172.217.162.4";
        int puerto = 7;
        //log(" socket " + ip + " " + puerto);
        try{
            Socket sk = new Socket(ip,puerto);
            BufferedReader entrada = new BufferedReader(new
                    InputStreamReader(sk.getInputStream()));
            PrintWriter salida = new PrintWriter(
                    new OutputStreamWriter(sk.getOutputStream()),true);
           // log("enviando ... Hola Mundo!");
            salida.println("Hola mundo");
           // log("recibiendo ... " + entrada.readLine());
            sk.close();
        }
        catch (Exception e){
            //log("error: " + e.toString());
        }
    }
}
