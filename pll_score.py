import esm
import torch
import torch.nn.functional as F
import argparse
from Bio import SeqIO

def calculate_pppl(sequence: str, model, alphabet):
    batch_converter = alphabet.get_batch_converter()
    data = [("seq", sequence)]
    _, _, tokens = batch_converter(data)
    tokens = tokens.cuda()

    seq_len = tokens.shape[1] - 2
    log_likelihood = 0.0

    for i in range(1, seq_len + 1):
        masked_tokens = tokens.clone()
        masked_tokens[0, i] = alphabet.mask_idx

        with torch.no_grad():
            logits = model(masked_tokens)["logits"]

        log_probs = F.log_softmax(logits[0, i], dim=-1)
        target_idx = tokens[0, i]
        log_likelihood += log_probs[target_idx].item()

    avg_ll = log_likelihood / seq_len
    pppl = torch.exp(torch.tensor(-avg_ll))

    return float(log_likelihood), float(avg_ll), pppl.item()

def main():
    parser = argparse.ArgumentParser(description="Compute PLL/PPPL scores from a FASTA file")
    parser.add_argument("--fasta", required=True, help="Path to input FASTA file")
    args = parser.parse_args()

    print("Loading ESM2 model...")
    model, alphabet = esm.pretrained.load_model_and_alphabet("esm2_t33_650M_UR50D")
    model = model.cuda().eval()

    print(f"Reading sequences from {args.fasta}")
    for record in SeqIO.parse(args.fasta, "fasta"):
        name = record.id
        seq = str(record.seq).strip().replace("*", "").upper()

        print(f"\nScoring {name} (length: {len(seq)}):")
        pll, avg_ll, pppl = calculate_pppl(seq, model, alphabet)
        print(f"PLL: {pll:.4f}")
        print(f"Avg Log-Likelihood: {avg_ll:.4f}")
        print(f"PPPL: {pppl:.4f}")

if __name__ == "__main__":
    main()
