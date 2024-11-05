// MainScreen.kt
package com.example.shiva

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import com.example.shiva.EncryptionUtils.encryptData
import com.example.shiva.EncryptionUtils.decryptData
import java.security.MessageDigest


@Composable
fun EntryScreen() {
    var userInput by remember { mutableStateOf("") }
    var displayMessage by remember { mutableStateOf("") }

    val context = LocalContext.current

    // Encrypted flags using EncryptionUtils
    val (ivZenos, encryptedZenosFlag) = encryptData(context.getString(R.string.flag1))
    val (ivZodiark, encryptedZodiarkFlag) = encryptData(context.getString(R.string.flag2))
    val (ivAzem, encryptedAzemFlag) = encryptData(context.getString(R.string.flag3))

    val firstFlag = "Mumbo5"

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            TextField(
                value = userInput,
                onValueChange = { userInput = it },
                label = { Text("Enter Password") },
                visualTransformation = PasswordVisualTransformation(),
                modifier = Modifier.fillMaxWidth()
            )
            Spacer(modifier = Modifier.height(16.dp))
            Button(
                onClick = {
                    displayMessage = when (computeHash(userInput)) {
                        computeHash(firstFlag) -> decryptData(ivZenos, encryptedZenosFlag)
                        computeHash(context.getString(R.string.key2)) ->  if (checkForHorses()) decryptData(ivZodiark, encryptedZodiarkFlag) else "Error: App Signature is not valid"
                        computeHash(context.getString(R.string.key3)) -> if (isItTrue()) decryptData(ivAzem, encryptedAzemFlag) else "Error: something is not true"
                        else -> "Invalid Password"
                    }
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Unlock")
            }
            Spacer(modifier = Modifier.height(16.dp))
            Text(text = displayMessage)
        }
    }
}


fun getCurrentAppSignature(): String {
    // Implement logic to retrieve the app's current signature
    return "someSignature"
}

fun checkForHorses(): Boolean {
    val originalSignature = "originalSignatureHash" // Replace with the actual original signature hash
    val currentSignature = getCurrentAppSignature()
    return currentSignature == originalSignature
}

fun isItTrue(): Boolean {
    // This condition is meant to be bypassed using instrumentation
    return false // Change this to true using instrumentation
}

fun computeHash(input: String): String {
    return md5(input.reversed() + "extra_salt")
}

fun md5(input: String): String {
    val md = MessageDigest.getInstance("MD5")
    val digest = md.digest(input.toByteArray())
    return digest.fold("") { str, it -> str + "%02x".format(it) }
}
