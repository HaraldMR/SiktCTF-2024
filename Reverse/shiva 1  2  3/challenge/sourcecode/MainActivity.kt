// MainActivity.kt
package com.example.shiva

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.example.shiva.ui.theme.ShivaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ShivaTheme {
                EntryScreen() // Corrected to use EntryScreen instead of MainScreen
            }
        }
    }
}
