# 🚀 Home Automation with Raspberry Pi Pico W (Bluetooth)  

## 📌 Overview  
This project enables **home automation** using **Raspberry Pi Pico W** with built-in **Bluetooth**.  
The system allows **wireless control of GPIO pins** via a **Serial Bluetooth Terminal** on an Android phone.  

---

## 🎯 Features  
- ✅ Wireless control of **GPIO pins** using Bluetooth commands.  
- ✅ Simple and efficient **BLE (Bluetooth Low Energy)** communication.  
- ✅ Easy setup using **Thonny IDE**.  

---

## 🔧 Requirements  

### 📟 Hardware  
- 🟢 **Raspberry Pi Pico W**  
- 📱 Android phone with **Serial Bluetooth Terminal** app  
- 💡 Any external devices to control via GPIO (LEDs, relays, etc.)  

### 💻 Software  
- 🖥 **Thonny IDE** (to flash Python scripts onto Pico W)  
- 📲 **Serial Bluetooth Terminal** (available on the Play Store)  

---

## 📥 Setup Instructions  

### 1️⃣ Prepare Raspberry Pi Pico W  
- 🔌 **Connect** Pico W to your PC via **USB**.  
- 🖥 Open **Thonny IDE** and ensure **Pico W** is detected.  

### 2️⃣ Upload Python Scripts  
- 🚀 Upload the following files to **Pico W** using **Thonny IDE**:  
  - 📜 `ble_advertising.py`  
  - 📜 `ble_simple_peripheral.py`  
  - 📜 `main.py`  
- 🔄 Restart **Pico W** after flashing the scripts.  

### 3️⃣ Install Bluetooth Terminal on Android  
- 📲 Download **Serial Bluetooth Terminal** from the **Google Play Store**.  
- 🔗 Open the app and **connect** to the **Pico W Bluetooth** device.  

### 4️⃣ Control GPIO Pins via Bluetooth  
- 📡 Send **"Toggel_GP2"** → Toggle **GP2** pin **ON/OFF**.  
- 🔴 Send **"NO_GP2"** → Turn **GP2 OFF**.  
- 🔄 Use similar commands for other **GPIO pins**.  

---

## 📜 Commands Reference  

| Command        | Action                        |
|---------------|--------------------------------|
| `Toggel_GP2`  | Toggle GPIO2 ON/OFF           |
| `NO_GP2`      | Turn OFF GPIO2                |
| `Toggel_GPX`  | Toggle GPIOX (replace X)      |
| `NO_GPX`      | Turn OFF GPIOX (replace X)    |

---

## 🚀 Future Enhancements  
🔹 **Adding support for more GPIO pins.**  
🔹 **Implementing a mobile app for better UI control.**  
🔹 **Expanding to include sensor data readings.**  

---

✅ **Like this project?** Give it a ⭐ on **GitHub!**  
🔗 **Contributions welcome!** Feel free to submit a **Pull Request (PR).**  

---

This `.md` file now looks **clean, structured, and visually appealing** for GitHub. 🚀 Let me know if you need more modifications! 😊  
