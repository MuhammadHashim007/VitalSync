import streamlit as st
import streamlit.components.v1 as components
import os

# ---------------------------------------------------------
# PAGE SETUP (OLED Dark Canvas)
# ---------------------------------------------------------
st.set_page_config(
    page_title="PulseCommand | Emergency Lifeline & 3D CPR Copilot",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CYBERPUNK EMERGENCY THEME STYLESHEET
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Dark Cockpit Canvas */
    .stApp {
        background-color: #080B10;
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(255, 46, 84, 0.12) 0%, transparent 45%),
            radial-gradient(circle at 90% 90%, rgba(0, 242, 157, 0.08) 0%, transparent 45%),
            radial-gradient(circle at 50% 50%, rgba(255, 168, 0, 0.05) 0%, transparent 60%);
        color: #F1F5F9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Glassmorphic Panels */
    .emergency-card {
        background: rgba(14, 20, 32, 0.82);
        border: 1px solid rgba(255, 46, 84, 0.3);
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.7), 0 0 20px rgba(255, 46, 84, 0.15);
        backdrop-filter: blur(14px);
        margin-bottom: 20px;
    }

    .triage-card {
        background: rgba(16, 24, 38, 0.75);
        border: 1px solid rgba(0, 242, 157, 0.25);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 24px -8px rgba(0, 242, 157, 0.15);
        margin-bottom: 15px;
    }

    .alert-card {
        background: rgba(26, 18, 12, 0.8);
        border: 1px solid rgba(255, 168, 0, 0.4);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 15px;
    }

    /* Headings & Neons */
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }
    
    .neon-crimson {
        color: #FF2E54 !important;
        text-shadow: 0 0 14px rgba(255, 46, 84, 0.6);
    }

    .neon-emerald {
        color: #00F29D !important;
        text-shadow: 0 0 12px rgba(0, 242, 157, 0.5);
    }

    .neon-amber {
        color: #FFA800 !important;
        text-shadow: 0 0 12px rgba(255, 168, 0, 0.5);
    }

    /* Action Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FF2E54 0%, #BA092B 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        border: 1px solid #FF6B8B !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 18px rgba(255, 46, 84, 0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 26px rgba(255, 46, 84, 0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECRETS / KEYS
# ---------------------------------------------------------
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))

# ---------------------------------------------------------
# SIDEBAR: NAVIGATION & EMERGENCY CALL SCRIPT
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 class='neon-crimson'>🫀 PulseCommand</h2>", unsafe_allow_html=True)
    st.caption("AHA / ERC Emergency First-Response System")
    
    app_mode = st.radio(
        "Select Emergency Operational Module:",
        [
            "🫀 Live CPR & 3D Anatomical Guide", 
            "🐍 Snake & Animal Bite Protocol", 
            "🩸 Severe Bleeding & Tourniquet",
            "🫁 Choking (Heimlich Maneuver)",
            "🔥 Burns & Chemical Exposure",
            "🎒 72-Hour Disaster Go-Bag & Planning",
            "🤖 AI Triage Copilot"
        ]
    )

    st.divider()
    st.markdown("<h4 class='neon-amber'>🚨 1-Tap Emergency Dispatch</h4>", unsafe_allow_html=True)
    caller_loc = st.text_input("Incident Location / Landmark:", "Building 4, Sector G-10, 2nd Floor")
    victim_state = st.selectbox("Victim State:", ["Unresponsive / Not Breathing", "Severe Bleeding", "Venomous Snake Bite", "Severe Choking"])
    
    if st.button("Generate Operator Script", use_container_width=True):
        st.session_state["show_dispatch_script"] = True

    if st.session_state.get("show_dispatch_script", False):
        st.info(f"""
        **📢 Speak clearly into phone:**
        > "Emergency Dispatch: I have a victim who is **{victim_state}**.
        > Exact location: **{caller_loc}**.
        > First-aid actions are underway. Dispatch an ALS ambulance immediately."
        """)

# =========================================================
# MODULE 1: CPR & 3D INTERACTIVE ANATOMICAL GUIDE
# =========================================================
if app_mode == "🫀 Live CPR & 3D Anatomical Guide":
    st.markdown("<h1>Cardiac Arrest Response & 3D Mannequin</h1>", unsafe_allow_html=True)
    st.markdown("Follow the 3D anatomical placement, synchronize your pumps to the metronome, and track cycles.")

    # Selection controls
    p_col1, p_col2 = st.columns([1, 1])
    with p_col1:
        patient_type = st.radio(
            "Victim Category:",
            ["Adult / Teen (2 Hands, 2+ inches)", "Child 1-8y (1-2 Hands, 2 inches)", "Infant <1y (2 Fingers / 2 Thumbs, 1.5 inches)"],
            horizontal=True
        )
    with p_col2:
        cpr_style = st.radio(
            "Protocol Mode:",
            ["Hands-Only CPR (Continuous compressions at 100-120 BPM)", "Full CPR (30 Compressions : 2 Rescue Breaths)"],
            horizontal=True
        )

    col_3d, col_audio = st.columns([1.2, 1], gap="medium")

    with col_3d:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("<h4 class='neon-crimson'>🧊 3D Mannequin & Hand Placement Visualizer</h4>", unsafe_allow_html=True)
        st.caption("Rotate, pan, and observe chest compression target (lower half of sternum, between nipples).")

        # Three.js 3D Interactive Mannequin Canvas
        three_js_html = """
        <!DOCTYPE html>
        <html>
        <head>
          <style>
            body { margin: 0; overflow: hidden; background: #0A0E17; }
            #canvas-container { width: 100%; height: 350px; position: relative; border-radius: 12px; }
            #labels { position: absolute; top: 12px; left: 14px; color: #FFF; font-family: monospace; font-size: 12px; }
            .badge { background: rgba(255,46,84,0.3); border: 1px solid #FF2E54; padding: 3px 8px; border-radius: 4px; color: #FF708F; }
          </style>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        </head>
        <body>
          <div id="canvas-container">
            <div id="labels">
              <span class="badge">TARGET: STERNUM CENTER</span><br/>
              <span style="color:#94A3B8;">Drag mouse to rotate 3D view</span>
            </div>
          </div>

          <script>
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x0a0e17);

            const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(0, 15, 30);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;

            // Ambient & Point Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambientLight);

            const neonLight = new THREE.PointLight(0xff2e54, 2, 50);
            neonLight.position.set(0, 10, 10);
            scene.add(neonLight);

            const cyanLight = new THREE.PointLight(0x00f29d, 1, 50);
            cyanLight.position.set(0, -10, -10);
            scene.add(cyanLight);

            // MANNEQUIN GROUP
            const mannequin = new THREE.Group();

            // 1. Torso
            const torsoGeo = new THREE.BoxGeometry(10, 16, 5);
            const torsoMat = new THREE.MeshStandardMaterial({ 
                color: 0x1E293B, 
                roughness: 0.4, 
                metalness: 0.2,
                wireframe: false 
            });
            const torso = new THREE.Mesh(torsoGeo, torsoMat);
            torso.position.y = 0;
            mannequin.add(torso);

            // 2. Ribcage Wireframe Guide
            const wireGeo = new THREE.BoxGeometry(10.2, 12, 5.2);
            const wireMat = new THREE.MeshBasicMaterial({ color: 0x334155, wireframe: true });
            const ribs = new THREE.Mesh(wireGeo, wireMat);
            ribs.position.y = -1;
            mannequin.add(ribs);

            // 3. Head & Neck
            const headGeo = new THREE.SphereGeometry(3, 32, 32);
            const headMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.6 });
            const head = new THREE.Mesh(headGeo, headMat);
            head.position.set(0, 11.5, 0);
            mannequin.add(head);

            // 4. Target Compression Crosshair (Sternum)
            const targetGeo = new THREE.RingGeometry(0.8, 1.4, 32);
            const targetMat = new THREE.MeshBasicMaterial({ color: 0xff2e54, side: THREE.DoubleSide });
            const targetRing = new THREE.Mesh(targetGeo, targetMat);
            targetRing.position.set(0, 1.5, 2.6);
            mannequin.add(targetRing);

            // 5. Interlocked Hands Indicator
            const handGeo = new THREE.BoxGeometry(3.5, 2, 1.5);
            const handMat = new THREE.MeshStandardMaterial({ 
                color: 0xff4757, 
                emissive: 0x880a1e,
                roughness: 0.3 
            });
            const hands = new THREE.Mesh(handGeo, handMat);
            hands.position.set(0, 1.5, 4.2);
            mannequin.add(hands);

            // Lay mannequin flat on its back for CPR
            mannequin.rotation.x = -Math.PI / 2.5;
            scene.add(mannequin);

            // Animation loop with sternum compression pump simulation
            let clock = new THREE.Clock();
            function animate() {
                requestAnimationFrame(animate);
                const elapsed = clock.getElapsedTime();

                // 110 BPM Compression rhythm animation
                const rate = 110 / 60; // beats per second
                const cycle = Math.sin(elapsed * rate * Math.PI * 2);
                
                if (cycle > 0) {
                    hands.position.z = 4.2 - (cycle * 0.9); // Hands push down
                    targetRing.scale.set(1 + cycle * 0.25, 1 + cycle * 0.25, 1);
                } else {
                    hands.position.z = 4.2;
                    targetRing.scale.set(1, 1, 1);
                }

                controls.update();
                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            });
          </script>
        </body>
        </html>
        """
        components.html(three_js_html, height=360)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_audio:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("<h4 class='neon-crimson'>⏱️ Audio Metronome & Heart Beacon</h4>", unsafe_allow_html=True)
        
        # Audio Metronome with Web Audio API (110 BPM)
        metronome_html = """
        <div style="text-align: center; padding: 10px 0;">
            <div id="heartBeacon" style="
                width: 110px; height: 110px; border-radius: 50%;
                background: radial-gradient(circle, #FF2E54 0%, #800A20 85%);
                margin: 0 auto; display: flex; align-items: center; justify-content: center;
                font-size: 38px; box-shadow: 0 0 20px rgba(255, 46, 84, 0.4);
                transition: transform 0.05s ease-out; cursor: pointer; user-select: none;
            ">🫀</div>
            
            <div style="margin-top: 18px;">
                <button id="toggleBtn" onclick="toggleMetronome()" style="
                    background: #FF2E54; color: #FFF; border: none; border-radius: 8px;
                    padding: 10px 22px; font-weight: 800; font-size: 15px; cursor: pointer;
                    box-shadow: 0 4px 15px rgba(255, 46, 84, 0.4);
                ">START METRONOME (110 BPM)</button>
            </div>
            <p id="statusTxt" style="color: #94A3B8; font-size: 13px; margin-top: 8px;">Status: Standby</p>
        </div>

        <script>
            let audioCtx = null;
            let isRunning = false;
            let intervalId = null;
            const bpm = 110;
            const intervalMs = (60 / bpm) * 1000;

            function playBeep() {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = "sine";
                osc.frequency.setValueAtTime(880, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.35, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.08);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.09);

                const beacon = document.getElementById("heartBeacon");
                beacon.style.transform = "scale(1.2)";
                beacon.style.boxShadow = "0 0 35px rgba(255, 46, 84, 0.9)";
                setTimeout(() => {
                    beacon.style.transform = "scale(1.0)";
                    beacon.style.boxShadow = "0 0 20px rgba(255, 46, 84, 0.4)";
                }, 80);
            }

            function toggleMetronome() {
                const btn = document.getElementById("toggleBtn");
                const status = document.getElementById("statusTxt");
                if (isRunning) {
                    clearInterval(intervalId);
                    isRunning = false;
                    btn.innerText = "START METRONOME (110 BPM)";
                    btn.style.background = "#FF2E54";
                    status.innerText = "Status: Standby";
                } else {
                    playBeep();
                    intervalId = setInterval(playBeep, intervalMs);
                    isRunning = true;
                    btn.innerText = "STOP METRONOME";
                    btn.style.background = "#475569";
                    status.innerText = "Beating at 110 compressions/min";
                }
            }
        </script>
        """
        components.html(metronome_html, height=210)
        
        # Interactive Cycle Counter
        if "cpr_count" not in st.session_state:
            st.session_state["cpr_count"] = 0
        if "cycles_completed" not in st.session_state:
            st.session_state["cycles_completed"] = 0

        c_col1, c_col2 = st.columns(2)
        c_col1.metric("Cycle Compressions", f"{st.session_state['cpr_count']} / 30")
        c_col2.metric("2-Min Sets Done", f"{st.session_state['cycles_completed']}")

        btn1, btn2 = st.columns(2)
        if btn1.button("➕ Push (+1)", use_container_width=True):
            st.session_state["cpr_count"] += 1
            if st.session_state["cpr_count"] >= 30:
                st.session_state["cpr_count"] = 0
                st.session_state["cycles_completed"] += 1
                st.warning("💨 PAUSE: Give 2 Rescue Breaths (1s each, watch chest rise). Resume immediately!")

        if btn2.button("🔄 Reset Counter", use_container_width=True):
            st.session_state["cpr_count"] = 0
            st.session_state["cycles_completed"] = 0

        if st.session_state["cycles_completed"] >= 5:
            st.error("⚠️ 2 MINUTES REACHED: Swap rescuers if fatigued to maintain 2-inch depth! Check AED.")
            
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 2: SNAKE & ANIMAL BITE PROTOCOL
# =========================================================
elif app_mode == "🐍 Snake & Animal Bite Protocol":
    st.markdown("<h1>Venomous Snake & Animal Bite Triage</h1>", unsafe_allow_html=True)
    st.markdown("Immediate, decisive actions to prevent systemic venom circulation and fatal infections.")

    b_col1, b_col2 = st.columns([1.1, 1], gap="medium")
    with b_col1:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-crimson'>⛔ WHAT YOU MUST NEVER DO</h3>", unsafe_allow_html=True)
        st.markdown("""
        * ❌ **DO NOT cut into the fang punctures** (causes fatal tissue necrosis and hemorrhage).
        * ❌ **DO NOT attempt to suck out venom** with your mouth or suction cups (ineffective, introduces oral bacteria).
        * ❌ **DO NOT apply an arterial tourniquet** (concentrates venom, leading to limb amputation).
        * ❌ **DO NOT apply ice packs or electric shocks**.
        * ❌ **DO NOT give aspirin, ibuprofen, or alcohol** (thins blood and worsens internal bleeding).
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with b_col2:
        st.markdown("<div class='triage-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-emerald'>✅ MANDATORY FIRST-RESPONSE STEPS</h3>", unsafe_allow_html=True)
        st.markdown("""
        1. **Immobilize the Limb:** Keep the bitten extremity **at or slightly below heart level**. Do not let the victim walk or move.
        2. **Remove All Constrictive Items:** Instantly strip rings, watches, bracelets, and tight shoes before severe edema (swelling) sets in.
        3. **Pressure Immobilization Bandage:** For neurotoxic/elapid bites (kraits, cobras), wrap an elastic crepe bandage firmly from fingers/toes upwards (like a sprain wrap), splinting the joint.
        4. **Mark the Swelling Boundary:** Use a ballpoint pen to trace the border of redness/swelling and write the current time next to it. Update every 15 minutes for the hospital toxicologist.
        5. **Rush to Emergency Facility:** Call ahead to ensure **Polyvalent Anti-Snake Venom (ASV)** or Rabies Immunoglobulin is available.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 3: SEVERE BLEEDING & TOURNIQUET
# =========================================================
elif app_mode == "🩸 Severe Bleeding & Tourniquet":
    st.markdown("<h1>Massive Hemorrhage & Arterial Bleed Control</h1>", unsafe_allow_html=True)
    st.markdown("Direct pressure, wound packing, and commercial/improvised tourniquet protocols.")

    t_col1, t_col2 = st.columns([1, 1], gap="medium")
    with t_col1:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-crimson'>🛑 Step 1: Direct Firm Pressure</h3>", unsafe_allow_html=True)
        st.markdown("""
        * Expose the wound: Cut clothing away to see the exact bleeding vessel.
        * Place clean sterile gauze or cloth directly onto the bleeding site.
        * **Lock your elbows straight** and apply your full body weight directly downward into the wound cavity.
        * **Do NOT peek:** Maintain unbroken continuous pressure for a minimum of 5 full minutes.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_col2:
        st.markdown("<div class='alert-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-amber'>⚡ Step 2: High & Tight Tourniquet (Limbs)</h3>", unsafe_allow_html=True)
        st.markdown("""
        If arterial blood is pulsing or spurting from an arm or leg:
        1. Place the tourniquet **2 to 3 inches above the bleed** (never directly over a joint like an elbow or knee).
        2. Pull the band completely tight to remove all slack before turning the windlass.
        3. **Twist the windlass rod** until the bright red pulsing bleed stops completely.
        4. Lock the windlass rod in the clip.
        5. **Write the exact application time (T = HH:MM)** on the victim's forehead or tourniquet strap. **Never loosen it.**
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 4: CHOKING (HEIMLICH MANEUVER)
# =========================================================
elif app_mode == "🫁 Choking (Heimlich Maneuver)":
    st.markdown("<h1>Acute Airway Obstruction & Choking</h1>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("### Adult / Child")
        st.markdown("""
        1. Stand behind the victim.
        2. Make a fist with one hand, thumb-side inward just **above the navel and below the breastbone**.
        3. Grasp your fist with your other hand.
        4. Deliver **quick, upward and inward thrusts** until the object pops out or the victim loses consciousness.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='triage-card'>", unsafe_allow_html=True)
        st.markdown("### Infant (< 1 Year)")
        st.markdown("""
        * **NEVER perform abdominal thrusts on an infant.**
        * Place infant face down along your forearm, supporting their jaw.
        * Deliver **5 firm back slaps** between shoulder blades.
        * Flip face up and give **5 quick chest thrusts** using 2 fingers in center of chest. Repeat.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='alert-card'>", unsafe_allow_html=True)
        st.markdown("### If Victim Becomes Unresponsive")
        st.markdown("""
        * Lower them carefully to the firm floor.
        * Call 911 / 1122 immediately.
        * **Begin 30 chest compressions right away.**
        * Look inside mouth before giving breaths: only remove an object if you clearly see it (no blind finger sweeps).
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 5: BURNS & CHEMICAL EXPOSURE
# =========================================================
elif app_mode == "🔥 Burns & Chemical Exposure":
    st.markdown("<h1>Thermal, Electrical & Chemical Burn Care</h1>", unsafe_allow_html=True)

    b1, b2 = st.columns([1, 1], gap="medium")
    with b1:
        st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-crimson'>🔥 Thermal & Scald Burns</h3>", unsafe_allow_html=True)
        st.markdown("""
        1. **Cool with Clean Running Water:** Flush for a full **10 to 20 minutes**. Never use ice or freezing water.
        2. **Do Not Burst Blisters:** Intact skin prevents severe septic infections.
        3. **Never Apply Home Remedies:** No toothpaste, butter, flour, or raw eggs.
        4. **Cover Loosely:** Drape with sterile non-adherent dressing or clean plastic wrap.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown("<div class='triage-card'>", unsafe_allow_html=True)
        st.markdown("<h3 class='neon-emerald'>🧪 Chemical & Acid Exposure</h3>", unsafe_allow_html=True)
        st.markdown("""
        1. **Dry Powders First:** Brush off dry chemical powders before washing (water may activate corrosive reactions).
        2. **Continuous 20-Min Water Flush:** Flood eyes or skin under low-pressure running tap water immediately.
        3. **Strip Contaminated Clothes:** Carefully cut away saturated clothing while water is running.
        4. Save chemical product container or label for poison control review.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 6: 72-HOUR DISASTER GO-BAG & PLANNING
# =========================================================
elif app_mode == "🎒 72-Hour Disaster Go-Bag & Planning":
    st.markdown("<h1>Family Crisis Readiness & 72-Hour Go-Bag</h1>", unsafe_allow_html=True)
    st.caption("Essential checklist for earthquakes, sudden floods, urban fires, or extended blackout events.")

    st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("### 💧 Hydration & Food")
        st.checkbox("4 Liters of clean drinking water / person / day (x3 days)")
        st.checkbox("Water purification tablets / life-straw filter")
        st.checkbox("Calorie-dense non-perishable bars, nuts, canned fish")
        st.checkbox("Manual can opener")

    with g2:
        st.markdown("### 💊 Health & First Aid")
        st.checkbox("7-day supply of critical prescription medications")
        st.checkbox("Commercial CAT / SWAT-T Tourniquet & sterile trauma gauze")
        st.checkbox("Burn dressings & antiseptic wipes")
        st.checkbox("N95 particulate masks (for dust, smoke, smog)")

    with g3:
        st.markdown("### ⚡ Power & Documents")
        st.checkbox("20,000 mAh charged power bank & heavy-duty cables")
        st.checkbox("Waterproof pouch with IDs, deeds, cash, insurance copies")
        st.checkbox("High-lumen LED flashlight + spare lithium batteries")
        st.checkbox("Multi-tool knife & emergency survival whistle")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 7: AI TRIAGE COPILOT (GROQ & GEMINI FLASH)
# =========================================================
elif app_mode == "🤖 AI Triage Copilot":
    st.markdown("<h1>Sub-Second Emergency AI Triage</h1>", unsafe_allow_html=True)
    st.caption("Ask high-speed first-aid instructions powered by Groq Llama 3.3 70B or Google AI Studio.")

    st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
    user_q = st.text_input("Enter the emergency condition or question:", "Someone drank bleach 5 minutes ago. Should I make them vomit?")
    
    if st.button("Consult Emergency AI"):
        if GROQ_API_KEY:
            try:
                from groq import Groq
                client = Groq(api_key=GROQ_API_KEY)
                resp = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system", 
                            "content": (
                                "You are an urgent tactical emergency medical responder. "
                                "Provide under 60 words, strictly numbered, imperative commands. "
                                "Highlight absolute life-threatening hazards (e.g. NEVER INDUCE VOMITING for corrosives) in all caps."
                            )
                        },
                        {"role": "user", "content": user_q}
                    ],
                    max_tokens=150
                )
                st.markdown(f"**⚡ Immediate Directives:**\n\n{resp.choices[0].message.content}")
            except Exception as e:
                st.error(f"Inference error: {e}")
        elif GEMINI_API_KEY:
            try:
                from google import genai
                client = genai.Client(api_key=GEMINI_API_KEY)
                resp = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Emergency first aid question: {user_q}. Answer in 3 ultra-short numbered directives under 50 words."
                )
                st.markdown(f"**⚡ Immediate Directives:**\n\n{resp.text}")
            except Exception as e:
                st.error(f"Inference error: {e}")
        else:
            st.warning("Set `GROQ_API_KEY` or `GEMINI_API_KEY` in Streamlit Secrets (`.streamlit/secrets.toml`) to activate live AI answers.")
    st.markdown("</div>", unsafe_allow_html=True)
