# PLL Scoring for Protein Sequences (ESM2)

This tool calculates the **Pseudo Log-Likelihood (PLL)** and **Pseudo-Perplexity (PPPL)** of protein sequences using [Meta AI's ESM2 model](https://github.com/facebookresearch/esm). These scores help quantify how "natural" a protein looks to a protein language model. Making it useful for evaluating designed sequences like antibodies or binders.

---

## Usage

Score a FASTA file containing a single protein sequence (binder only):

```bash
python pll_score.py --fasta example_binder.fasta
```

### Example Output

```
Reading sequences from example_binder.fasta
Scoring: Cradle_EGFR_241aa (length: 241)
PLL: -301.2522
Avg Log-Likelihood: -1.2500
PPPL: 3.4904
```

---


## Installation

### 1. Create a Conda Environment (Recommended)

```bash
conda create -n pll_env python=3.8
conda activate pll_env
```

### 2. Install Dependencies

```bash
pip install fair-esm torch biopython
```

Requires Python 3.8+. A GPU is recommended (but CPU works for short sequences).


## Files

- `pll_score.py` – script to score PLL and PPPL using a sequence from a FASTA file
- `example_binder.fasta` – example input binder sequence from Adaptyv Bio challenge

---

## Citation

If you use this tool, please cite [Meta AI's ESM2 models](https://github.com/facebookresearch/esm).

---
