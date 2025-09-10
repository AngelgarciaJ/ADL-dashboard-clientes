# 📊 Dashboard de Segmentación de Clientes

Este proyecto es un **dashboard interactivo con Streamlit** para analizar información financiera de clientes y visualizar su **segmentación crediticia** (ej. A, A+, B).  

El enfoque actual es **descriptivo**, centrado en:
- 📈 Estadísticas básicas de las variables.
- 🎨 Gráficos interactivos (barras, distribuciones, correlaciones).
- ⚙️ Filtros dinámicos por segmento.
- 🧩 Organización en pestañas para navegar entre diferentes vistas.

---

## 🔎 Funcionalidades principales
1. **Vista previa de datos** con filtros por segmento.  
2. **Distribución de clientes** según características financieras.  
3. **Visualizaciones interactivas** (Seaborn + Matplotlib).  
4. **Estadística descriptiva** de las variables.  
5. **Interfaz en Streamlit** lista para usar en la web o localmente.  

---

## ⚙️ Instalación y ejecución en tu máquina

### 1. Clonar el repositorio
```bash
git clone https://github.com/AngelgarciaJ/ADL-dashboard-clientes.git
cd ADL-dashboard-clientes
```
### 2. Crear un entorno virtual
```bash
python -m venv venv
```
#### Activar el entorno:
```bash
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar la aplicación
```bash
streamlit run app.py
```
