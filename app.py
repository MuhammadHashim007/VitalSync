import streamlit as st
import streamlit.components.v1 as components
import os
from openai import OpenAI

# ---------------------------------------------------------
# PAGE SETUP (OLED Dark Cockpit Canvas)
# ---------------------------------------------------------
st.set_page_config(
    page_title="PulseCommand | 3D Emergency Lifeline & OpenAI 120B Copilot",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CYBERPUNK EMERGENCY THEME STYLESHEET
# ---------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #080B10;
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(255, 46, 84, 0.12) 0%, transparent 45%),
            radial-gradient(circle at 90% 90%, rgba(0, 242, 157, 0.08) 0%, transparent 45%),
            radial-gradient(circle at 50% 50%, rgba(255, 168, 0, 0.05) 0%, transparent 60%);
        color: #F1F5F9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    .emergency-card {
        background: rgba(14, 20, 32, 0.85);
        border: 1px solid rgba(255, 46, 84, 0.35);
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.7), 0 0 20px rgba(255, 46, 84, 0.15);
        backdrop-filter: blur(14px);
        margin-bottom: 20px;
    }

    .triage-card {
        background: rgba(16, 24, 38, 0.8);
        border: 1px solid rgba(0, 242, 157, 0.3);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 24px -8px rgba(0, 242, 157, 0.15);
        margin-bottom: 15px;
    }

    .alert-card {
        background: rgba(26, 18, 12, 0.85);
        border: 1px solid rgba(255, 168, 0, 0.45);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 15px;
    }

    .ai-console-card {
        background: rgba(18, 22, 34, 0.9);
        border: 1px solid rgba(0, 242, 157, 0.4);
        border-radius: 14px;
        padding: 18px;
        margin-top: 15px;
    }

    h1, h2, h3, h4 {
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
# API CLIENT INITIALIZATION (OpenRouter / Groq / OpenAI)
# ---------------------------------------------------------
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY", ""))
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))

def query_openai_120b(system_context: str, user_prompt: str) -> str:
    """Dispatches queries to OpenAI gpt-oss-120b using OpenRouter or Groq."""
    if OPENROUTER_API_KEY:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )
        model_name = "openai/gpt-oss-120b"
    elif GROQ_API_KEY:
        client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=GROQ_API_KEY
        )
        model_name = "openai/gpt-oss-120b"
    else:
        return "⚠️ API Key missing. Please provide `OPENROUTER_API_KEY` or `GROQ_API_KEY` in Streamlit Secrets."

    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are PulseCommand Emergency AI, powered by OpenAI 120B. "
                        "Your mission is clinical triage, CPR coaching, and crisis response. "
                        "Rules: 1) Under 75 words. 2) Strict numbered imperative actions. "
                        "3) Bold life-threatening contraindications (e.g. NEVER DO X). "
                        "4) If medical information is incomplete, request immediate vital checks "
                        "(breathing, consciousness, pulse) while giving baseline safe actions."
                    )
                },
                {"role": "system", "content": f"SPECIFIC DOMAIN CONTEXT: {system_context}"},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_tokens=220
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"🚨 Inference Engine Error: {str(e)}"

# ---------------------------------------------------------
# SIDEBAR: NAVIGATION & 1-TAP DISPATCH SCRIPT
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 class='neon-crimson'>🫀 PulseCommand</h2>", unsafe_allow_html=True)
    st.caption("AI-Powered Emergency Response | OpenAI 120B Engine")
    
    app_mode = st.radio(
        "Emergency Operational Station:",
        [
            "🫀 3D CPR & Cardiac Metronome", 
            "🐍 Snake & Animal Bite Protocol", 
            "🩸 Severe Bleeding & Tourniquet",
            "🫁 Choking (Heimlich Maneuver)",
            "🔥 Burns & Chemical Exposure",
            "🎒 72-Hour Go-Bag & Survival",
            "🚨 Unlisted Emergency & Rare Medical Crises"
        ]
    )

    st.divider()
    st.markdown("<h4 class='neon-amber'>🚨 1-Tap Emergency Dispatch</h4>", unsafe_allow_html=True)
    caller_loc = st.text_input("Exact Incident Location / Landmark:", "Building 4, Sector G-10, 2nd Floor")
    victim_state = st.selectbox("Observed Status:", [
        "Unresponsive & Not Breathing", 
        "Severe Arterial Bleeding", 
        "Venomous Snake / Animal Bite", 
        "Severe Airway Obstruction", 
        "Suspected Stroke / Fainting",
        "Unknown Critical Trauma"
    ])
    
    if st.button("Generate Operator Script", use_container_width=True):
        st.session_state["show_dispatch_script"] = True

    if st.session_state.get("show_dispatch_script", False):
        st.info(f"""
        **📢 Read this aloud to 911 / 1122:**
        > "Emergency Dispatch: I am reporting an urgent case of **{victim_state}**.
        > Exact location: **{caller_loc}**.
        > Resuscitation and first aid are underway. Dispatch an ALS ambulance immediately."
        """)

# =========================================================
# MODULE 1: CPR & 3D INTERACTIVE ANATOMICAL GUIDE
# =========================================================
if app_mode == "🫀 3D CPR & Cardiac Metronome":
    st.markdown("<h1>Cardiac Arrest Response & 3D Mannequin</h1>", unsafe_allow_html=True)
    st.markdown("Follow the 3D anatomical placement, synchronize your pumps to the metronome, and track cycles.")

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

            const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambientLight);

            const neonLight = new THREE.PointLight(0xff2e54, 2, 50);
            neonLight.position.set(0, 10, 10);
            scene.add(neonLight);

            const cyanLight = new THREE.PointLight(0x00f29d, 1, 50);
            cyanLight.position.set(0, -10, -10);
            scene.add(cyanLight);

            const mannequin = new THREE.Group();

            const torsoGeo = new THREE.BoxGeometry(10, 16, 5);
            const torsoMat = new THREE.MeshStandardMaterial({ color: 0x1E293B, roughness: 0.4, metalness: 0.2 });
            const torso = new THREE.Mesh(torsoGeo, torsoMat);
            torso.position.y = 0;
            mannequin.add(torso);

            const wireGeo = new THREE.BoxGeometry(10.2, 12, 5.2);
            const wireMat = new THREE.MeshBasicMaterial({ color: 0x334155, wireframe: true });
            const ribs = new THREE.Mesh(wireGeo, wireMat);
            ribs.position.y = -1;
            mannequin.add(ribs);

            const headGeo = new THREE.SphereGeometry(3, 32, 32);
            const headMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.6 });
            const head = new THREE.Mesh(headGeo, headMat);
            head.position.set(0, 11.5, 0);
            mannequin.add(head);

            const targetGeo = new THREE.RingGeometry(0.8, 1.4, 32);
            const targetMat = new THREE.MeshBasicMaterial({ color: 0xff2e54, side: THREE.DoubleSide });
            const targetRing = new THREE.Mesh(targetGeo, targetMat);
            targetRing.position.set(0, 1.5, 2.6);
            mannequin.add(targetRing);

            const handGeo = new THREE.BoxGeometry(3.5, 2, 1.5);
            const handMat = new THREE.MeshStandardMaterial({ color: 0xff4757, emissive: 0x880a1e, roughness: 0.3 });
            const hands = new THREE.Mesh(handGeo, handMat);
            hands.position.set(0, 1.5, 4.2);
            mannequin.add(hands);

            mannequin.rotation.x = -Math.PI / 2.5;
            scene.add(mannequin);

            let clock = new THREE.Clock();
            function animate() {
                requestAnimationFrame(animate);
                const elapsed = clock.getElapsedTime();
                const rate = 110 / 60;
                const cycle = Math.sin(elapsed * rate * Math.PI * 2);
                
                if (cycle > 0) {
                    hands.position.z = 4.2 - (cycle * 0.9);
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

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — CPR & Resuscitation Copilot</h4>", unsafe_allow_html=True)
    user_cpr_q = st.text_input("Ask any CPR question (e.g., 'What if I hear ribs cracking?' or 'Can I do CPR on a soft bed?'):", key="q_cpr")
    if st.button("Consult AI (CPR)", key="btn_cpr"):
        if user_cpr_q.strip():
            with st.spinner("OpenAI 120B analyzing resuscitation protocol..."):
                ans = query_openai_120b(f"CPR and Cardiac Arrest context. Patient type: {patient_type}", user_cpr_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 2: SNAKE & ANIMAL BITE PROTOCOL
# =========================================================
elif app_mode == "🐍 Snake & Animal Bite Protocol":
    st.markdown("<h1>Venomous Snake & Animal Bite Triage</h1>", unsafe_allow_html=True)

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
        2. **Remove All Constrictive Items:** Instantly strip rings, watches, bracelets, and tight shoes before severe edema sets in.
        3. **Pressure Immobilization Bandage:** For neurotoxic/elapid bites (kraits, cobras), wrap an elastic crepe bandage firmly from fingers/toes upwards.
        4. **Mark the Swelling Boundary:** Use a ballpoint pen to trace the border of redness/swelling and write the current time.
        5. **Rush to Emergency Facility:** Call ahead to ensure **Polyvalent Anti-Snake Venom (ASV)** or Rabies Immunoglobulin is available.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — Bite & Envenomation Copilot</h4>", unsafe_allow_html=True)
    user_bite_q = st.text_input("Ask any bite/sting question (e.g., 'Bitten by black scorpion, swelling rapidly' or 'Stray dog scratched leg without bleeding'):", key="q_bite")
    if st.button("Consult AI (Bite Triage)", key="btn_bite"):
        if user_bite_q.strip():
            with st.spinner("OpenAI 120B running toxicology assessment..."):
                ans = query_openai_120b("Venomous snake, scorpion, and rabid animal bites context.", user_bite_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 3: SEVERE BLEEDING & TOURNIQUET
# =========================================================
elif app_mode == "🩸 Severe Bleeding & Tourniquet":
    st.markdown("<h1>Massive Hemorrhage & Arterial Bleed Control</h1>", unsafe_allow_html=True)

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

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — Hemorrhage & Trauma Copilot</h4>", unsafe_allow_html=True)
    user_bleed_q = st.text_input("Ask any bleeding trauma question (e.g., 'Bleeding won't stop after 10 mins with cloth' or 'Improvised tourniquet using belt?'):", key="q_bleed")
    if st.button("Consult AI (Bleeding)", key="btn_bleed"):
        if user_bleed_q.strip():
            with st.spinner("OpenAI 120B analyzing hemorrhage protocol..."):
                ans = query_openai_120b("Arterial bleeding, deep puncture, junctional hemorrhage, and tourniquet protocols.", user_bleed_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
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

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — Airway & Choking Copilot</h4>", unsafe_allow_html=True)
    user_choke_q = st.text_input("Ask any airway obstruction question (e.g., 'Pregnant woman choking' or 'How to perform Heimlich on myself alone?'):", key="q_choke")
    if st.button("Consult AI (Choking)", key="btn_choke"):
        if user_choke_q.strip():
            with st.spinner("OpenAI 120B evaluating airway protocol..."):
                ans = query_openai_120b("Foreign body airway obstruction, conscious/unconscious choking, pediatric and pregnant patient adaptations.", user_choke_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
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

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — Burn & Toxin Copilot</h4>", unsafe_allow_html=True)
    user_burn_q = st.text_input("Ask any burn/chemical question (e.g., 'Sulfuric acid splashed in eye' or 'Third degree electrical burn with charred skin'):", key="q_burn")
    if st.button("Consult AI (Burns)", key="btn_burn"):
        if user_burn_q.strip():
            with st.spinner("OpenAI 120B assessing burn depth and triage..."):
                ans = query_openai_120b("Chemical burn, thermal burn, scalds, ocular acid flush, and electrical burn care.", user_burn_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 6: 72-HOUR DISASTER GO-BAG & PLANNING
# =========================================================
elif app_mode == "🎒 72-Hour Go-Bag & Survival":
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

    # INTERACTIVE AI TAB QUERY (OpenAI 120B)
    st.markdown("<div class='ai-console-card'>", unsafe_allow_html=True)
    st.markdown("<h4 class='neon-emerald'>🤖 Ask OpenAI 120B — Custom Disaster Plan Generator</h4>", unsafe_allow_html=True)
    user_plan_q = st.text_input("Describe your family & disaster scenario (e.g., '2 adults, 1 infant, 1 diabetic grandmother preparing for severe flood evacuation'):", key="q_plan")
    if st.button("Generate Custom Survival Plan", key="btn_plan"):
        if user_plan_q.strip():
            with st.spinner("OpenAI 120B synthesizing tailored 72-hour survival protocol..."):
                ans = query_openai_120b("Disaster survival planning, Go-Bag optimization, special medical dependencies (insulin/infant care).", user_plan_q)
                st.markdown(f"**⚡ Directive:**\n\n{ans}")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MODULE 7: UNLISTED EMERGENCY & RARE MEDICAL CRISES
# =========================================================
elif app_mode == "🚨 Unlisted Emergency & Rare Medical Crises":
    st.markdown("<h1>Universal Medical Emergency Triage (OpenAI 120B)</h1>", unsafe_allow_html=True)
    st.markdown("Use this module for **any emergency condition not explicitly covered** in the tabs above.")

    st.markdown("<div class='alert-card'>", unsafe_allow_html=True)
    st.markdown("### ⚡ Instant Rapid Recognition Matrix (Pre-loaded Basics)")
    
    u1, u2, u3 = st.columns(3)
    with u1:
        st.markdown("**🧠 Stroke (FAST Protocol)**")
        st.markdown("""
        * **F**ace drooping on one side.
        * **A**rm weakness / drift when raised.
        * **S**peech slurred or nonsensical.
        * **T**ime: Call 911/1122 instantly. Note exact time symptoms began. **Give NO food or water.**
        """)
    with u2:
        st.markdown("**⚡ Seizure / Convulsions**")
        st.markdown("""
        * Clear hard/sharp objects away.
        * Cushion head with a soft jacket.
        * **NEVER put anything in their mouth** (cannot swallow tongue).
        * Turn onto side in **Recovery Position** once shaking ceases.
        """)
    with u3:
        st.markdown("**🐝 Severe Anaphylaxis**")
        st.markdown("""
        * Facial swelling, wheezing, hives.
        * Use **EpiPen (Epinephrine)** immediately into outer mid-thigh.
        * Hold firmly for 3–5 seconds.
        * Keep person lying flat with feet elevated (unless breathing difficult).
        """)
    st.markdown("</div>", unsafe_allow_html=True)

    # DYNAMIC ARBITRARY MEDICAL EMERGENCY CONSOLE
    st.markdown("<div class='emergency-card'>", unsafe_allow_html=True)
    st.markdown("<h3 class='neon-crimson'>Describe Any Unlisted Emergency or Symptoms</h3>", unsafe_allow_html=True)
    st.caption("Tell OpenAI 120B what happened, visible symptoms, age, and environment.")
    
    unlisted_symptoms = st.text_area(
        "Symptoms / Emergency Details:",
        "Person collapsed, sweating profusely, pale skin, confused, known diabetic who took insulin 2 hours ago but skipped lunch."
    )
    
    if st.button("⚡ Run Emergency Triage Now", use_container_width=True):
        if unlisted_symptoms.strip():
            with st.spinner("OpenAI 120B analyzing clinical risk factors..."):
                ans = query_openai_120b(
                    "Universal acute emergency triage. Diagnose most probable crisis, immediate stabilization steps, and critical DO NOTs.",
                    unlisted_symptoms
                )
                st.markdown("---")
                st.markdown(f"### 📋 Immediate Protocol:\n\n{ans}")
    st.markdown("</div>", unsafe_allow_html=True)
