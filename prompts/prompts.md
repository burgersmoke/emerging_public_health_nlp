Two of the capabilities in this work (Zoonotic Exposures and Other Pathogen exposures) used a LLM (ChatGPT 4).

None of the generation parameters were changed as these prompts were directly manually into the web interface for ChatGPT.  This was all manual with no  code used.  The prompts for these were comprised of three total varations:

Prompt #1:
Write 50 more sentences similar to this one:
[Example Sentence]

Prompt #2:
Provide example sentences that could be found in a clinical document where the patient was in contact with an animal or insect.

Prompt #3:
Provide example sentences that could be found in a clinical document where the patient may have contracted a condition due to exposure to food, water, people or the environment.

Prompt #2 and #3 were used verbatim as shown above.

Prompt #1 varied only by a user adding an example sentence and getting responses to review and add to training data.

Examples of some of these sentences can be seen in ../data/animal_exposure_sentences.py and ../data/other_exposure_sentences.py