# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python NLP research project for detecting early signals from emerging public health events. It implements three classifiers: animal/zoonotic exposures, other pathogen exposures (food, water, environmental), and public health authority communications. Work is associated with an academic publication.

## Environment Setup

```bash
conda env create -f python/environment.yml
conda activate emerging_public_health_nlp  # or the name in environment.yml
```

Key dependencies: Python 3.10, PyTorch (CUDA 11+), SetFit, MedSpacy, spaCy, Optuna, HuggingFace Transformers/Datasets.

## Architecture

Three detection approaches:

**SetFit classifiers** (animal exposures, other pathogen exposures):
- Base model: `paraphrase-mpnet-base-v2` fine-tuned with `CosineSimilarityLoss`
- Training data: synthetic sentences in `data/*.py`, generated via ChatGPT prompts documented in `prompts/prompts.md`
- 3-class output: `AFFIRMED`, `DENIED_OR_NEGATED`, `NO_MENTION`
- 80/20 stratified train/val split via scikit-learn
- Hyperparameter search with Optuna
- Trained checkpoint: `python/checkpoints/checkpoint-30/` (gitignored)

**Rule-based MedSpacy pipeline** (public health authority communications):
- Entity patterns in `resources/health_authority_target_rules.json`
- Attribute classification in `resources/health_authority_context_rules.json`

## Primary Entry Points

- `python/animal_exposure_evaluation.ipynb` — full training and evaluation pipeline for animal exposure classifier
- `data/animal_exposure_sentences.py` — training examples (affirmed/negated/no_mention)
- `data/other_exposure_sentences.py` — training examples for food/water/environmental exposures

## Data Pipeline

```
ChatGPT prompts → synthetic sentences in data/*.py
    → stratified 80/20 split
    → SetFit training (CosineSimilarityLoss)
    → checkpoint saved to python/checkpoints/
    → accuracy evaluation via HuggingFace evaluate
```

## Notes

- No formal test suite; notebooks are the primary executable artifacts
- Checkpoints are gitignored — retrain from notebooks if missing
- `prompts/prompts.md` documents the 3 ChatGPT prompt variations used for synthetic data generation
