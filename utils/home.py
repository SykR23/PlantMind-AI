import streamlit as st


class Home:

    @staticmethod
    def render():

        st.markdown(
            """
   # 🌿 PlantMind AI

   ### Enterprise RAG Copilot for Process Industries

   Ask technical questions about engineering manuals using
   Retrieval-Augmented Generation (RAG).

   ---
   """
        )

        st.markdown("### 💡 Example Questions")

        examples = [
            "How should a plate heat exchanger be cleaned?",
            "What refrigerants are approved?",
            "Explain CIP cleaning.",
            "How should the BPHE be mounted?"
        ]

        for example in examples:
            st.markdown(f"- {example}")