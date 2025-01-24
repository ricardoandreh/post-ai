#!/usr/bin/env python
import sys
import warnings

import agentops
from dotenv import load_dotenv
from post_ai.crew import PostAi

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

agentops.init()

def run():
    """
    Run the crew.
    """
    Tema = "Avanço e contribuições nos modelos multimodais no contexto da medicina" # Any topic
    Tom = "sério, acadêmico, totalmente formal e técnico"
    Aspectos = "interessante, cativante e factualmente correto"

    inputs = {
        "tema": Tema,
        "tom": Tom,
        "aspectos": Aspectos,
    }
    
    try:
        PostAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


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
