# PLL Scoring for Protein Sequences (ESM2)

This tool calculates the **Pseudo Log-Likelihood (PLL)** and **Pseudo-Perplexity (PPPL)** of protein sequences using [Meta AI's ESM2 model](https://github.com/facebookresearch/esm). These scores help quantify how "natural" a protein looks to a protein language model, making it useful for evaluating designed sequences like antibodies or binders.

---

## Example Output

```
Reading sequences from example_binder.fasta

Scoring: Cradle_EGFR_241aa (length: 241)
PLL: -301.2522
Avg Log-Likelihood: -1.2500
PPPL: 3.4904
```

---

## Installation

### 1. Install Dependencies

```bash
pip install fair-esm torch biopython
```

> Requires Python 3.8+, and a GPU is recommended (but CPU works for short sequences).

---

## Usage

### 1. Save your protein sequences in FASTA format

Example (`example_binder.fasta`):

```
>Cradle_EGFR_241aa
QVQLQQSGPGLVQPSQSLSITCTVSGFSLTNYGVHWVRQSPGKGLEWLGVIWSGGNTDYNTPFTSRLSISRDTSKSQVFFKMNSLQTDDTAIYYCARALTYYDYEFAYWGQGTLVTVSAGGGGSGGGGSGGGGSDILLTQSPVILSVSPGERVSFSCRASQSIGTNIHWYQQRTNGSPKLLIRYASESISGIPSRFSGSGSGTDFTLSINSVDPEDIADYYCQQNNNWPTTFGAGTKLELK
```

### 2. Run the script

```bash
python pll_score.py --fasta example_binder.fasta
```

---

## Files in this Repository

| File                   | Description                                  |
|------------------------|----------------------------------------------|
| `pll_score.py`         | Script for PLL/PPPL scoring using ESM2       |
| `example_binder.fasta` | Sample binder sequence from Adaptyv Bio      |
| `LICENSE`              | MIT License                                  |

---

## License

MIT License — free to use, modify, and share.
