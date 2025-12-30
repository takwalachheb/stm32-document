import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Gestion des I/O STM32 - Document Technique",
    page_icon="🔌",
    layout="wide"
)

# Style CSS pour une présentation professionnelle
st.markdown("""
<style>
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-title {
        color: #3a56d4;
        border-bottom: 3px solid #3a56d4;
        padding-bottom: 10px;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    .card {
        background: #f8f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4f6df5;
        margin: 1rem 0;
    }
    
    .code-block {
        background: #2d2d2d;
        color: #f8f8f2;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 0.95rem;
        overflow-x: auto;
        margin: 1rem 0;
    }
    
    .contact-info {
        background: #e8f4ff;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# En-tête principale
st.markdown("""
<div class="main-title">
    <h1>🔌 Gestion des I/O STM32</h1>
    <h3>Document Technique - Programmation Embarquée</h3>
    <p>Takwa Lachheb | 2ème année Mécatronique | 2025</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
## 📋 Introduction
Ce document présente trois applications pratiques de gestion des entrées/sorties sur microcontrôleurs STM32. 
Ces applications ont été développées dans le cadre de ma formation en mécatronique et illustrent les concepts 
fondamentaux de la programmation embarquée avec la bibliothèque HAL.
""")

# Application 1
st.markdown('<div class="section-title">Application 1 : Clignotement d\'une LED</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<strong>Description :</strong> Cette application fait clignoter une LED connectée au pin PA5 toutes les 500ms.
</div>
""", unsafe_allow_html=True)

st.markdown("**Configuration GPIO :**")
st.write("- Pin: PA5")
st.write("- Mode: GPIO_MODE_OUTPUT_PP")
st.write("- Pull: GPIO_NOPULL")
st.write("- Speed: GPIO_SPEED_FREQ_LOW")

st.markdown("**Code source :**")
st.code("""
/* USER CODE BEGIN WHILE */
while (1)
{
    // Inverser l'état de la LED
    HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
    
    // Attente 500 ms
    HAL_Delay(500);
}
/* USER CODE END WHILE */
""", language='c')

# Application 2
st.markdown('<div class="section-title">Application 2 : Commande LED par bouton poussoir</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<strong>Description :</strong> Contrôle d'une LED avec un bouton poussoir. La LED s'allume et s'éteint en alternance à chaque pression.
</div>
""", unsafe_allow_html=True)

st.markdown("**Pins utilisées :**")
st.write("- PA0 : Bouton poussoir (entrée)")
st.write("- PA5 : LED (sortie)")

st.markdown("**Code source :**")
st.code("""
while (1)
{
    // Vérifier si le bouton est appuyé (PA0 = 0)
    if (HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0) == GPIO_PIN_RESET)
    {
        // LED ON
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_SET);
        HAL_Delay(300);
        
        // LED OFF
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_RESET);
        HAL_Delay(300);
    }
    else
    {
        // Bouton relâché → LED OFF
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_RESET);
    }
}
""", language='c')

# Application 3
st.markdown('<div class="section-title">Application 3 : Afficheur 7 segments</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<strong>Description :</strong> Contrôle d'un afficheur 7 segments avec un bouton d'incrémentation. L'afficheur compte de 0 à 9.
</div>
""", unsafe_allow_html=True)

st.markdown("**Configuration des pins :**")
col1, col2 = st.columns(2)
with col1:
    st.write("**Segments :**")
    st.write("- A : PI3")
    st.write("- B : PI0")
    st.write("- C : PB4")
    st.write("- D : PC6")
    st.write("- E : PC7")
    st.write("- F : PI2")
    st.write("- G : PB14")

with col2:
    st.write("**Bouton :**")
    st.write("- PI11 : Bouton d'incrémentation")

st.markdown("**Exemple de code pour le chiffre 0 :**")
st.code("""
if(k == 0){
    HAL_GPIO_WritePin(GPIOI, GPIO_PIN_3, 0);  // Segment A
    HAL_GPIO_WritePin(GPIOI, GPIO_PIN_0, 0);  // Segment B
    HAL_GPIO_WritePin(GPIOB, GPIO_PIN_4, 0);  // Segment C
    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_6, 0);  // Segment D
    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_7, 0);  // Segment E
    HAL_GPIO_WritePin(GPIOI, GPIO_PIN_2, 0);  // Segment F
    HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, 1); // Segment G
}
""", language='c')

# Technologies et compétences
st.markdown('<div class="section-title">🛠️ Technologies et Compétences</div>', unsafe_allow_html=True)

col_tech, col_comp = st.columns(2)

with col_tech:
    st.markdown("**Technologies maîtrisées :**")
    st.markdown("""
    <div class="card">
    • STM32 Microcontrôleurs<br>
    • HAL Library (Hardware Abstraction Layer)<br>
    • Programmation en C embarqué<br>
    • Configuration GPIO<br>
    • Gestion des temporisations
    </div>
    """, unsafe_allow_html=True)

with col_comp:
    st.markdown("**Compétences développées :**")
    st.markdown("""
    <div class="card">
    • Configuration des périphériques GPIO<br>
    • Utilisation de la bibliothèque HAL<br>
    • Gestion des entrées/sorties<br>
    • Débogage de systèmes embarqués<br>
    • Développement d'applications complètes
    </div>
    """, unsafe_allow_html=True)

# Configuration système
st.markdown('<div class="section-title">⚙️ Configuration Système</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<strong>Configuration matérielle :</strong><br>
• Horloge : HSI 16MHz<br>
• Voltage : PWR_REGULATOR_VOLTAGE_SCALE3<br>
• Pas de PLL utilisé
</div>
""", unsafe_allow_html=True)

# Pied de page avec contact
st.markdown("""
<div class="contact-info">
<h3>📬 Contact et Informations</h3>
<p>Ce document a été réalisé dans le cadre de ma formation en mécatronique.</p>
<p><strong>Auteur :</strong> Takwa Lachheb</p>
<p><strong>Formation :</strong> 2ème année Mécatronique</p>
<p><strong>Date :</strong> 2025</p>
<p>Document pédagogique à usage éducatif</p>
</div>
""", unsafe_allow_html=True)

# Sidebar avec navigation
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/STMicroelectronics_logo_2015.svg/1200px-STMicroelectronics_logo_2015.svg.png", 
             width=150)
    
    st.markdown("## 📋 Navigation")
    st.markdown("""
    - [Introduction](#introduction)
    - [Application 1](#application-1-clignotement-d-une-led)
    - [Application 2](#application-2-commande-led-par-bouton-poussoir)
    - [Application 3](#application-3-afficheur-7-segments)
    - [Technologies](#technologies-et-compétences)
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Liens utiles")
    st.markdown("[Documentation STM32](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)")
    st.markdown("[HAL Library](https://www.st.com/en/embedded-software/stm32cubemx.html)")
    
    st.markdown("---")
    st.markdown("### 📊 À propos")
    st.info("""
    **Applications :** 3  
    **Pins utilisées :** 11  
    **Lignes de code :** ~150  
    **Niveau :** Intermédiaire
    """)