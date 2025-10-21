<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:306998,100:FFD43B&height=180&section=header&text=Proyecto%20de%20Virtualización%20con%20Python%20🐍&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</p>

---

## 📚 Descripción  
Este repositorio contiene un **informe técnico sobre virtualización**, junto con la **documentación necesaria para instalar y ejecutar un programa simple en Python** dentro de una máquina virtual.  

Incluye **guías paso a paso** con imágenes para la instalación de las dependencias principales (**Python**, **Ubuntu** y **VirtualBox**), además de las instrucciones para **clonar y ejecutar el repositorio**.  

El objetivo es **documentar el proceso de aprendizaje y aplicar los fundamentos de la virtualización** mediante ejercicios prácticos y demostraciones funcionales.  

---

## ⚙️ Requisitos del sistema  
Antes de comenzar, asegúrate de contar con lo siguiente:  

- 💽 **VirtualBox** (última versión recomendada)  
- 🐧 **Ubuntu** (como sistema operativo invitado)  
- 🐍 **Python 3.x** instalado dentro de la máquina virtual  
- 🌐 Conexión a Internet para descargar dependencias y clonar el repositorio  

---

## 🧩 Instalación  

### 1. Instalar VirtualBox  
Sigue las instrucciones del documento `Instalacion_VirtualBox.pdf`.  

### 2. Configurar Ubuntu como máquina virtual  
Sigue las instrucciones del documento `Instalacion_Ubuntu.pdf`.   

### 3. Instalar Git Bash y clonar el repositorio dentro de la máquina virtual  
```bash
sudo apt install git
```

```bash
git clone https://github.com/CTapia10/AySO-TPI-Virtualizacion.git
cd AySO-TPI-Virtualizacion
```

### 4. Instalar Python dentro de la máquina virtual  
Una vez dentro de Ubuntu, abre la terminal y sigue los siguientes pasos:

1️⃣ Actualizar los repositorios
```bash
sudo apt update && sudo apt upgrade -y
```
2️⃣ Instalar Python
```bash
sudo apt update && sudo apt install python3 -y
```
3️⃣ Instalar pip (gestor de paquetes de Python)
```bash
sudo apt install python3-pip -y
```
4️⃣ Verificar la instalación
```bash
python3 --version
pip3 --version
```

### 5. Ejecutar el programa de prueba  
Navega a la carpeta "codigo" dentro del proyecto y ejecuta:  
```bash
python3 programa.py
```

---

## 📄 Contenido del repositorio  
- 📘 `/documentacion/` → Guías de instalación con imágenes y pasos detallados.  
- 🐍 `/codigo/` → Programa simple en Python para pruebas dentro de la VM.  
- 🧾 `/informe_tecnico/` → Informe sobre los fundamentos y aplicaciones de la virtualización.  
- 🖼️ `/imagenes/` → Capturas de pantalla del proceso de ejecución del programa.  

---

## 🎯 Objetivo del proyecto  
Aplicar los **principios básicos de la virtualización** mediante la creación y configuración de una máquina virtual funcional,  
ejecutando un programa en Python como demostración práctica del entorno configurado.  

---

## 👨‍💻 Autores  
**Cristian Tapia y Daniela Velazquez**  
📅 Año: 2025  

---

## 🧠 Licencia  
Este proyecto se distribuye bajo la licencia **MIT**, lo que permite su uso, modificación y distribución con los debidos créditos al autor.  
