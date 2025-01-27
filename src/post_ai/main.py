#!/usr/bin/env python
import sys
import warnings

import agentops
from dotenv import load_dotenv
from post_ai.crew import PostAi

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

agentops.end_all_sessions()
agentops.init(auto_start_session=False, default_tags=["post-ai"])

Tema = "Avanço e contribuições nos modelos multimodais no contexto da medicina" # Any topic
Tom = "sério, acadêmico, totalmente formal e técnico"
Aspectos = "interessante, cativante e factualmente correto"


def run():
    """
    Run the crew.
    """
    inputs = {
        "tema": Tema,
        "tom": Tom,
        "aspectos": Aspectos,
    }
    
    agentops.start_session()
    
    try:
        PostAi().crew().kickoff(inputs=inputs)

    except Exception as e:
        agentops.end_session("Failure")

        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        agentops.end_session("Success")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "tema": "IA LLMs",
        "tom": "acadêmico e técnico",
        "aspectos": "cativante e interessante",
    }
    
    try:
        PostAi().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PostAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "tema": "IA LLMs",
        "tom": "acadêmico e técnico",
        "aspectos": "cativante e interessante",
    }

    try:
        PostAi().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_via_streamlit(inputs):
    """
    Run the crew via Streamlit.
    """   
    agentops.start_session()
    
    try:
        output = PostAi().crew().kickoff(inputs=inputs)

        return output.raw
    except Exception as e:
        agentops.end_session("Failure")

        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        agentops.end_session("Success")
