# from rasa.core.policies import  KerasPolicy, MemoizationPolicy
# from rasa.core.agent import Agent

# agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])


# # loading our neatly defined training dialogues
# training_data = agent.load_data('stories.md')

# agent.train(
#     training_data,
#     validation_split=0.0,
#     epochs=200
# )

# agent.persist('models/dialogue')

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa.core import *
from rasa.core import utils
from rasa.core.agent import Agent
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy


def train_nlu():
    training_data = load_data('data/nlu.md')
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")
    return model_directory

import asyncio
def train_dialogue(
        domain_file="domain.yml",
        model_path="models/dialogue",
        training_data_file="data/stories.md"
        ):
    agent = Agent(
        domain_file,
        policies=[MemoizationPolicy(max_history=3), KerasPolicy()]
        )
    training_data =  agent.load_data(training_data_file)
    agent.train(
        training_data,
        epochs=400,
        batch_size=100,
        validation_split=0.2
        )
    agent.persist(model_path)
    return agent


def train_all():
    model_directory = train_nlu()
    agent = train_dialogue()
    return [model_directory, agent]


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    # utils.configure.colored.logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot training')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "train-all"],
            help="what the bot should do?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "train-all":
        train_all()