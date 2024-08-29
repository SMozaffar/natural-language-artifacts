import json
from checklist.editor import Editor
from checklist.perturb import Perturb
from checklist.test_suite import TestSuite
from checklist.test_types import MFT, INV, DIR
import spacy
import numpy as np
import itertools
import pandas as pd



editor = Editor()

coref_prem = editor.template('{male} and {female} are married. He is {a:profession} and she is {a:profession_two}.',
                              male=['Frank', 'Richard', 'Samuel'],
                              female=['Alice', 'Kelly', 'Amy'],
                              profession=['doctor', 'teacher', 'artist'],
                              profession_two=['teacher', 'artist', 'doctor'],
                              nsamples=25)

coref_hyp = editor.template('{male} is {a:profession}.',
                            male=['Frank', 'Richard', 'Samuel'],
                            profession=['doctor', 'teacher', 'artist'],
                            nsamples=25)

srl_prem = editor.template("{word} Danielle {action} Alyssa?", 
                           word=['Does', 'Is'], 
                           action=['support', 'supported by'],
                           nsamples=25,
                           remove_duplicates=True)

check = []

for i, j in zip(coref_prem['data'], coref_hyp['data']):
    check.append([i,j])

formatted_data = [{
    'premise': pair[0],
    'hypothesis': pair[1],
    'label': -1  # Placeholder for the label
    } for pair in check]


df = pd.DataFrame(formatted_data)

print(df)


def create_sentence_pairs():
    editor = Editor()

    # Coreference Resolution Templates
    coref_templates = [
        # from Ribeiro (2020)
        editor.template("If Joshua and Chloe were alone, do you think {pronounone} would reject {pronountwo}?", pronounone=['he', 'she'], pronountwo=['her', 'him']),
        editor.template("If Jack and Lindsey were married, do you think {person} family would be happy?", person=['Lindsey\'s', 'his']),
        # pronoun resolution
        editor.template("{person} went to the park. {person_pronoun} saw a bird.", person=['Alice', 'Bob'], person_pronoun=['she', 'he']),
        # nested phrases
        editor.template("The manager of {team}, who was recently hired, gave a speech.", team=['the team', 'the project']),
        # proper nouns and descriptions
        editor.template("{person}, a talented {profession}, played at the concert. {person_pronoun} was brilliant.", person=['John', 'Emily'], profession=['guitarist', 'pianist'], person_pronoun=['he', 'she']),
        # possessive pronouns
        editor.template("{person}'s brother said {person_pronoun} would come. {person_pronoun} arrived late.", person=['Mary', 'John'], person_pronoun=['he', 'she']),
        # ambiguity in pronouns
        editor.template("{personone} spoke to {persontwo} before {personone_pronoun} left.", personone=['Alex', 'Jordan'], persontwo=['Jordan', 'Alex'], personone_pronoun=['he', 'she'])
    ]

    # Semantic Role Labeling Templates
    srl_templates = [
        # from Ribeiro (2020)
        editor.template("Is {person} related to {person}?", person=['Jillian', 'Heather']),
        editor.template("{word} Danielle {action} Alyssa?", word=['Does', 'Is'], action=['support', 'supported by']),
        # agent-action-object
        editor.template("The {agent} cooked a {object}.", agent=['chef', 'baker'], object=['meal', 'cake']),
        # action with multiple objects
        editor.template("{agent} gave {indirect_object} a {direct_object}.", agent=['She', 'He'], indirect_object=['her friend', 'his brother'], direct_object=['gift', 'book']),
        # passive voice
        editor.template("The {object} was sung by the {agent}.", object=['song', 'poem'], agent=['artist', 'poet']),
        # instruments or means
        editor.template("The {object} was written with a {instrument}.", object=['letter', 'report'], instrument=['pen', 'typewriter']),
        # cause-effect relations
        editor.template("Due to {cause}, the {effect} was canceled.", cause=['heavy rain', 'snowstorm'], effect=['match', 'concert']),
        # temporal and locative roles
        editor.template("{agent} will speak at the {locative} {temporal}.", agent=['She', 'He'], locative=['conference', 'meeting'], temporal=['tomorrow', 'next week'])
    ]

    # Combining all templates
    all_templates = coref_templates + srl_templates

    return all_templates

