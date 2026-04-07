# 🚀 Satellite Orbit Simulation

## 📌 Project Description

This project simulates the motion of satellites orbiting around the Earth using fundamental principles of orbital mechanics. The simulation visually demonstrates how a satellite moves in a curved path due to the gravitational force exerted by the Earth, the concepts from orbital mechanics and satellite motion using numerical simulation.

The Earth is placed at the center, and satellites revolve around it in real time, showing how velocity and gravity combine to maintain stable orbits.

---

## ⚙️ Tools and Technologies Used

* Python
* NumPy (for numerical calculations)
* Matplotlib (for visualization and animation)
* Visual Studio Code (VS Code)

---

## ▶️ Steps to Run the Program

1. Ensure Python is installed on your system  
   (Check using: python --version)

2. Install required libraries:
   pip install numpy matplotlib  

3. Download or clone the project:
   git clone https://github.com/SathyaAnandh/satellite-orbit-simulation.git  

4. Navigate to the project folder:
   cd satellite_orbit_simulation  

5. Run the program:
   python main.py  

6. A window will open showing the Earth and satellites orbiting in real time  

---

## 🧠 Explanation of the Simulation

### 🌍 What is an Orbit?

An orbit is the path followed by an object around a massive body like Earth due to gravitational attraction. In this simulation, satellites follow circular paths around the Earth.

---

### 🛰️ Why Do Satellites Orbit the Earth?

Satellites remain in orbit because of the balance between:

* **Gravitational Force** → pulls the satellite toward Earth
* **Forward Velocity** → keeps the satellite moving ahead

This balance prevents the satellite from falling straight down and results in continuous orbital motion.

---

### ⚡ Physics Used

#### 🔹 Newton’s Law of Gravitation

F = GMm / r²

Where:

* G → Gravitational constant
* M → Mass of Earth
* m → Mass of satellite
* r → Distance from Earth's center

This force pulls the satellite inward.

---

#### 🔹 Orbital Velocity

v = √(GM / r)

This velocity ensures that the satellite stays in orbit.

---

#### 🔹 Motion Calculation

The simulation updates the satellite’s motion step-by-step using:

* Acceleration due to gravity
* Velocity updates
* Position updates over time

This creates a smooth and continuous orbit.

---

## 🎯 Features Implemented

* ✅ Visualization of Earth and satellite orbit
* ✅ Real-time satellite movement
* ✅ Multiple satellites orbiting simultaneously
* ✅ Adjustable satellite speed
* ✅ Display of orbital path (trajectory)

---

## 🛰️ Satellite Configuration Details

| Satellite | Color | Initial Radius (m) | Initial Velocity (m/s) | Orbit Type | Description |
|----------|------|--------------------|------------------------|------------|------------|
| Satellite 1 | 🔴 Red | 7 × 10⁶ | 7700 | Near-circular | Inner satellite with stable orbit closer to Earth |
| Satellite 2 | 🟢 Green | 8 × 10⁶ | 7200 | Near-circular | Outer satellite with slower velocity and larger orbit |

---

### 🧠 Notes:
- Satellites closer to Earth require **higher velocity** to maintain orbit  
- Satellites farther away move with **lower velocity**  
- Changing velocity affects orbit shape (circular → elliptical → escape)  

---

## 📸 Output

![Simulation Output](output.png)
![Simulation Output](output1.png)
---

## 📁 Project Structure

* main.py → Runs the simulation
* simulation.py → Handles physics calculations
* visualization.py → Displays animation
* constants.py → Stores physical constants

---

## 🚀 Future Improvements

* Add graphical user interface (GUI) for controls
* Implement elliptical orbits (Kepler’s laws)
* Add interactive parameter inputs
* Simulate real-world satellite data

---

## 📌 Conclusion

This project provides a clear understanding of how satellites orbit the Earth using fundamental physics concepts. It demonstrates how gravitational force and velocity work together to create stable orbital motion in space.

