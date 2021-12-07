package com.example.tezrt;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.io.IOException;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    String ip = "192.168.56.1";
    int puerto = 59988;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Client client = new Client();
        client.start();

    }
}