import streamlit as st
import psycopg2 

st.set_page_config(
    page_title="Inicio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def main():
    st.header("Bienvenido al Metodo de Ansiedad",divider="green")

    col1,col2 =st.columns(2)

    with col1:

        st.write("**¿QUÉ ES LA ANSIEDAD?**")
        st.write("")
        st.text("""Es un desequilibrio emocional que se experimenta como desazón, intranquilidad, confusión, incertidumbre, miedo, sentimiento de amenaza, aprensión o tensión puede ir
        desde una leve sensación de inquietud por la anticipación de un peligro (externo o interno) hasta una enorme agitación, pánico o temor.
        Generalmente, el surgimiento de la ansiedad se relaciona con la posibilidad de que se
        generen acontecimientos desagradables, por ello suele manifestarse como una mezcla de
        miedo, incertidumbre y pavor. No toda respuesta de ansiedad se considera inadecuada, ya
        que en forma moderada podría cumplir una función útil o de adaptación, al prevenir a la
        persona contra posibles estímulos de peligro; sin embargo, se podría considerar como
        respuesta inadecuada o inadaptable cuando se dan sin que exista relación con un peligro
        específico externo; o cuando abruma y altera totalmente el funcionamiento social, laboral y
        afectivo de una persona y llega a incapacitarla totalmente.
        """, width="stretch")
        st.write("**¿Qué lo ocasiona?**")
        st.text(""" La ansiedad obedece a múltiples causas. Generalmente es un aviso; nos indica que dentro
        de nosotros existe un problema real o simbólico que debemos solucionar. Existen
        básicamente dos tipos de ansiedad:
        • Externa: Cuando existe un peligro real externo o una amenaza a nuestra integridad
        física o emocional, como un siniestro, asalto, un terremoto, una cirugía, una pérdida de
        empleo.
        • Interna: Cuando la causa no aparece del todo clara ante nuestros ojos, ya que
        probablemente provenga de nuestro inconsciente y, por lo tanto, puede tener sus
        orígenes en vivencias del pasado no resultas, o en acontecimientos presentes que no
        queremos afrontar. Por ejemplo: miedo al castigo por sentir que tal vez hicimos algo
        inadecuado; pensamientos negativos hacia algún miembro de la familia; impotencia por
        sentir que no somos aceptados en un determinado grupo social.""")

    with col2:
        st.image("images/imagen1.jpg",width=500,output_format="JPEG",channels="RGB",use_container_width=True)
    


if __name__ == "__main__":
    main()