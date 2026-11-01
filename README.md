# VitalSync

# 🫀 PulseCommand: Lifeline & 3D Emergency CPR Copilot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Three.js](https://img.shields.io/badge/WebGL-Three.js-00f29d.svg)](https://threejs.org/)

**PulseCommand** is a mission-critical emergency triage platform and 3D CPR copilot designed for zero-latency execution during out-of-hospital medical emergencies. Built with an **OLED Dark Cockpit** UI, an embedded **WebGL 3D anatomical mannequin**, an **HTML5/Web Audio metronome**, and **dual-engine AI triage** (Groq Llama 3.3 70B & Google Gemini 2.5 Flash), PulseCommand delivers immediate, authoritative physical directives when seconds dictate survival.

---

## ⚡ Core Features

### 1. 🧊 Interactive 3D Mannequin & Hand Placement Visualizer
* **Embedded Three.js Canvas:** Renders a 3D anatomical torso displaying the ribcage, sternal target zone, and dynamic hand position.
* **Full Orbit Controls:** Rescuers can rotate, tilt, and zoom around the virtual mannequin to inspect exact sternal hand angles.
* **Live Compression Pump Simulation:** The 3D hands physically oscillate at 110 BPM to demonstrate proper compression recoil rhythm.

### 2. 🫀 Audio Metronome & Dual-Mode Cycle Tracker
* **110 BPM Rhythm Lock:** Uses the browser's low-latency `AudioContext` to output a crisp acoustic pulse within the clinical 100–120 compressions/minute window.
* **Reactive Bioluminescent Beacon:** A pulsing neon crimson cardiac orb provides peripheral visual pacing.
* **Cycle Accounting:**
  * Tracks 30:2 standard CPR and Hands-Only continuous compressions.
  * Triggers mandatory rest/rescuer swap and AED analysis alerts every 2 minutes (5 complete cycles).

### 3. 🚨 Multimodal Emergency Crisis Engine
Includes authoritative, step-by-step clinical triage flows for acute life threats:
* **🐍 Venomous Snake & Animal Bites:** Enforces pressure immobilization bandaging (PIB) and limb stabilization; explicitly flags lethal contraindications (no incision, suction, or arterial tourniquets).
* **🩸 Severe Bleeding & Hemorrhage:** Protocol for high-and-tight commercial windlass tourniquet (CAT) application and manual wound packing.
* **🫁 Airway Obstruction & Choking:** Immediate Heimlich instructions for adults/children and back-slap chest-thrust sequences for infants.
* **🔥 Burns & Scalds:** Thermal cooling duration protocols (10–20 min clean running water) and dry-chemical neutralizing directives.
* **🎒 72-Hour Go-Bag & Disaster Planner:** Interactive survival readiness checklist covering water purification, trauma dressings, power, and vital documents.

### 4. 🤖 Instant AI Emergency Copilot
* **Sub-Second Directives:** Powered by Groq (`llama-3.3-70b-versatile`) or Google AI Studio (`gemini-2.5-flash`).
* **Emergency Dispatch Scripting:** 1-tap generator that creates a plain-text read-aloud script for local emergency dispatchers (911 / 1122).

---

## 🎨 UI Architecture: OLED Dark Cockpit

PulseCommand abandons generic white/blue dashboard templates in favor of a high-contrast emergency palette designed for high stress and low-light field conditions:
* **Background Canvas:** Deep Carbon Void (`#080B10`) with ambient radial glows.
* **Neon Crimson (`#FF2E54`):** Primary emergency actions, heart rate indicators, and metronome pulse.
* **Cyber Emerald (`#00F29D`):** Verified protocols, safety clearance, and clinical recovery statuses.
* **Pulse Amber (`#FFA800`):** Rescue breath alerts and time-elapsed warnings.
* **Surfaces:** Translucent glassmorphism (`backdrop-filter: blur(14px)`) with crisp borders.

---

## 🛠️ Project Structure

```bash
pulsecommand/
├── .streamlit/
│   └── secrets.toml          # Local API keys (never commit to git)
├── app.py                    # Main Streamlit application & Three.js canvas
├── requirements.txt          # Python runtime dependencies
├── LICENSE                   # Open-source license (MIT)
└── README.md                 # System documentation
