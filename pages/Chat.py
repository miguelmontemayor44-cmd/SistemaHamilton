import streamlit as st

# --- Diccionario de palabras clave y respuestas ---
qa_pairs = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como te llamas": "Soy un pequeño chatbot 🤖",
    "quien te creo": "Fui creado por un estudiante de Ingeniería llamado Miguel Montemayor",
    "que puedes hacer": "Puedo responder preguntas predefinidas y conversar un poco contigo 😊",
    "adios": "¡Hasta luego! 😊",
    "bye": "¡Hasta luego! 😊",
    "chao": "¡Hasta luego! 😊",
    "cerrar": "¡Hasta luego! 😊",
}

st.set_page_config(page_title="Mini Chatbot", page_icon="🤖")
st.title("🤖 Mini Chatbot")
st.caption("""**Escribe:** "test de ansiedad" para comenzar el test.""")


if "messages" not in st.session_state:
    st.session_state.messages = []
if "doing_test" not in st.session_state:
    st.session_state.doing_test = False

# --- Mostrar historial ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# --- Mostrar formulario si el usuario está haciendo el test ---
if st.session_state.doing_test:
    with st.form("test_ansiedad"):
        st.subheader("Porfavor completa el test seleccionando los valores")
        p1 = st.radio("1.- ¿HUMOR ANSIOSO: Inquietud, Expectativas de catástrofe, Aprensiónanticipación temerosa,Irritabilidad? ", ["Nunca","Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p1")
        p2 = st.radio("2.- ¿TENSION: Sensaciones de tensión, Fatigabilidad, Imposibilidad de estar quieto, Reacciones de sobresalto, Llanto fácil, Temblores, Sensaciones de incapacidad para esperar?", ["Nunca","Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p2")
        p3 = st.radio("3.- ¿MIEDOS: A la oscuridad, A los desconocidos, A quedarse solo, A los animales, A la circulación, A la muchedumbre?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p3")
        p4 = st.radio("4.- ¿INSOMNIO: Dificultades de conciliación, Sueño interrumpido, Sueño no satisfactorio, con cansancio al despertar, Sueños penosos, Pesadillas, Terrores nocturnos?", ["Nunca","Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p4")
        p5 = st.radio("5.- ¿FUNCIONES INTELECTUALES (COGNITIVAS): Dificultad de concentración, Mala memoria?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p5")
        p6 = st.radio("6.- ¿HUMOR DEPRESIVO: Perdida de interés. No disfruta del tiempo libre, Depresión, Insomnio de madrugada.,Variaciones anímicas a lo largo del día?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p6")
        p7 = st.radio("7.- ¿SINTOMAS SOMATICOS MUSCULARES: Dolores musculares, Rigidez muscular,Sacudidas musculares, Sacudidas clónicas, Rechinar de dientes, Voz quebrada?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p7")
        p8 = st.radio("8.- ¿SINTOMAS SOMATICOS GENERALES: Zumbido de oídos, Visión borrosa, Oleadas de calor o frio, Sensación de debilidad, Sensaciones parestésicas (pinchazos u hormigueos)?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p8")
        p9 = st.radio("9.- ¿SINTOMAS CARDIOVASCULARES: Taquicardia, Palpitaciones, Dolor torácico, Sensación pulsátil en vasos, Sensaciones de “baja presión” o desmayos, Extrasístoles (arritmias cardiacas benignas)?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p9")
        p10 = st.radio("10.- ¿SINTOMAS RESPIRATORIOS: Opresión pretorácica, Constricción precordial, Sensación de ahogo o falta de aire, Suspiros, Disnea (dificultad para respirar)?", ["Nunca","Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p10")
        p11 = st.radio("11.- ¿SINTOMAS GASTROINTESTINALES: Dificultades evacuatorias, Gases, Dispepsia: dolores antes o después de comer, ardor, hinchazón abdominal, nauseas, vómitos, constricción epigástrica, Cólicos (espasmos) abdominals, Borborigmos, Diarrea, Pérdida de peso, Estreñimiento?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p11")
        p12 = st.radio("12.- ¿SINTOMAS GENITOURINARIOS: Micciones frecuentes, Micción imperiosa, Amenorrea (falta del período menstrual), Metrorragia (hemorragia genital), Frigidez, Eyaculación precoz, Impotencia, Ausencia de erección?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p12")
        p13 = st.radio("13.- ¿SINTOMAS GENITOURINARIOS: Micciones frecuentes, Micción imperiosa, Amenorrea (falta del período menstrual), Metrorragia (hemorragia genital), Frigidez, Eyaculación precoz, Impotencia, Ausencia de erección?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p13")
        p14 = st.radio("14.- ¿CONDUCTA EN EL TRANSCURSO DEL TEST: Tendencia al abatimiento, Agitación: manos inquietas, juega con los dedos, cierra los puños, tic, aprieta el pañuelo en las manos, Rostro preocupado, Aumento del tono muscular o contracturas musculares, Respiración entrecortada, Palidez facial, Traga saliva, Eructos, Taquicardia o palpitaciones, Ritmo respiratorio acelerado, Sudoración, Pestañeo?", ["Nunca", "Casi Nunca", "A veces", "Frecuentemente", "Siempre"], key="p14")


        submitted = st.form_submit_button("Enviar respuestas")

    if submitted:
        # Asignar puntaje
        opciones = {"Nunca": 0,"Casi Nunca":1, "A veces": 2, "Frecuentemente": 3, "Siempre": 4}
        puntaje = sum([opciones[st.session_state.p1], opciones[st.session_state.p2],
                       opciones[st.session_state.p3], opciones[st.session_state.p4],opciones[st.session_state.p5],opciones[st.session_state.p6],opciones[st.session_state.p7],opciones[st.session_state.p8],opciones[st.session_state.p9],opciones[st.session_state.p10],opciones[st.session_state.p11],opciones[st.session_state.p12],opciones[st.session_state.p13],opciones[st.session_state.p14]])

        # Interpretación
        if puntaje <=0:
            resultado = "Parece que no sufres ansiedad"
        elif puntaje <= 28:
            resultado = "**Podrias presentar Ansiedad Psíquica** - te recomiendo 1. Relájese profundamente e imagine una situación que normalmente le causa angustia o pánico. 2. Concéntrese en los pensamientos negativos y en las respuestas fisiológicas, emocionales y de conductas asociadas con ese hecho, como sudoración de manos, alteración del ritmo cardiaco y de la frecuencia respiratoria, sensación de miedo, temor o irritabilidad. 3. Congele esas imágenes mentales y reemplácelas por pensamientos más apropiados o por emociones y sentimientos agradables. Empezará a sentirse mejor y a tener resultados más positivos y gratificantes. 4. Obsérvese a sí mismo ante esa misma situación que le ocasionaba angustia, pero ahora tenga la seguridad de que no le va a provocar la desagradable reacción anterior. 5. Mantenga las imágenes positivas todo el tiempo necesario y recurra a ellas cuando sienta que la angustia empieza a aparecer. 6. Para reforzar sus sentimientos placenteros haga una lista de diez a quince experiencias positivas que haya experimentado y manténgalas en su mente durante treinta segundos al día. Practique esto durante cinco minutos diarios y así, cuando sienta que la angustia empieza a manifestarse, le será fácil sustituir sus emociones negativas por otras gratificantes. 7. Para evitar la tendencia a centrarse en los síntomas físicos que su angustia puede ocasionarle, así como a tener imágenes y pensamientos catastróficos de lo que le podría suceder, aleje su atención de todo aquello y manténgase concentrado en experiencias positivas y en sensaciones agradables. 8. Para solucionar los problemas que considera que son los motivadores de su angustia: o Elabore una lista de los principales conflictos. o Evalúe cada una de las situaciones de la manera más racional y objetiva posible. o Haga una lista de posibles soluciones. o Idee planes o cursos de acción. o Fortalezca sus recursos para enfrentarlos. o Proteja sus puntos débiles. 9. Busque la manera de realizar una catarsis positiva y de obtener el apoyo de personas cercanas. Se ha comprobado que cuando alguien enfrenta una situación angustiante, por el simple hechos de saberse escuchada, de poder expresar los que siente sabiéndose querida, aceptada y apoyada, su angustia disminuye considerablemente y, por lo tanto, podrá aplicar con éxito los mecanismos necesarios para solucionar el problema. 10. No busque a quien culpar por lo que le está pasando. Cuando la fuente de nuestra angustia es ambigua o difícil de definir, en ocasiones solemos desplazar nuestra agresión interna hacia otros blancos, en este caso a personas convenientes para nosotros; o culpamos inocentes. "
        else:
            resultado = "**Podrías presentar Ansiedad Somática** - Te recomiendo 1. Infórmese acerca de qué es la ansiedad, cómo se manifiesta y por qué surge, para evitar una visión distorsionada sobre o que probablemente está sucediendo en estos momentos, o lo que podría suceder; también evitar fantasías o temores innecesarios que pueden incrementar sus síntomas y empeorar su situación actual. Recuerde que estar informado hace que usted retome la sensación de control sobre su vida y sobre lo que acontece. 2. No se preocupe por sentir angustia. Ella no tiene poder alguno sobre usted. Cuando menos miedo tenga a la aparición de los síntomas, estos ocurrirán con menos frecuencia. En cambio, si permite que su ansiedad persista, puede llegar a generalizarse y agravarse. 3. Ponga en marcha todos los recursos externos que conozca (como relajación, respiración profunda), así como todos los recursos internos posibles (análisis de pensamiento y emociones negativas, etc.). Asimismo, le recomiendo practicar ejercicio moderado (por ejemplo: caminar veinte minutos diarios). 4. Practique la higiene del sueño para evitar el insomnio y retornar el ciclo normal de sueño. 5. No olvide que usted, con sólo desearlo, puede detener los pensamientos o emociones negativos que ocasionan su sintomatología y cambiarlos por algo positivo y agradable. Para volverse todo un experto en ello. "

        st.chat_message("assistant").markdown(resultado)
        st.session_state.messages.append({"role": "assistant", "content": resultado})

        # Terminar test
        st.session_state.doing_test = False
        if st.button("Cerrar test",use_container_width=True):
            st.rerun()

# --- Entrada del usuario ---
else:
    user_input = st.chat_input("Escribe tu mensaje...")

    if user_input:
        # Mostrar mensaje del usuario
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        user_text = user_input.lower()
        response = None

        # si el usuario pone test se llama la funcion
        if "test de ansiedad" in user_text:
            st.session_state.doing_test = True
            response = "Aquí tienes un pequeño test de ansiedad. Responde con sinceridad 😊"
            st.rerun()

        else:
            # --- Buscar coincidencia parcial ---
            for key, value in qa_pairs.items():
                if key in user_text:
                    response = value
                    break

            if response is None:
                response = "Lo siento, no entiendo esa pregunta 😅"

        # Mostrar respuesta del bot
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})



    
