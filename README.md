# Bioinformatics Sequence Analysis

Python and Biopython workflows for the computational analysis of biological sequences.

## Overview

This repository contains a collection of computational approaches for
analysing DNA sequences using Python and Biopython.

The project explores different aspects of sequence analysis, from basic
nucleotide composition and sequence statistics to motif detection,
mutation analysis, phylogenetics and pairwise sequence alignment.

The work was developed as part of a Master's programme in Bioinformatics
and focuses on applying programming techniques to common problems in
computational biology.

---

## Objectives

The main objectives of this project are:

- Analyse biological sequences programmatically.
- Extract nucleotide composition and sequence statistics.
- Identify sequence motifs and biologically relevant patterns.
- Analyse nucleotide substitutions and mutations.
- Calculate sequence similarity using different approaches.
- Perform basic phylogenetic analysis.
- Align biological sequences and visualise sequence similarity.
- Apply Python and Biopython to real biological data.

---

## Sequence analysis

### FASTA processing

The project works with DNA sequences stored in FASTA format.

The analysis includes:

- Reading multiple sequences from a FASTA file.
- Identifying individual sequences.
- Calculating sequence length.
- Counting nucleotide frequencies.
- Comparing sequence composition between different organisms.

---

### Nucleotide composition

For each DNA sequence, nucleotide composition is calculated for:

- Adenine (A)
- Cytosine (C)
- Guanine (G)
- Thymine (T)

Additional sequence statistics include:

- GC content
- Purine percentage
- Pyrimidine percentage
- Sequence length

The resulting information is organised into a tabular representation
using pandas.

---

### Sequence visualisation

Nucleotide composition is also represented graphically.

The project generates visualisations showing the relative proportion
of A, C, G and T within individual sequences.

These visualisations provide a simple way to compare nucleotide
composition across biological sequences.

---

## Sequence manipulation

### Reverse complement

DNA reverse complements are calculated using Biopython.

This operation provides a basic example of biological sequence
manipulation and is commonly used when analysing DNA sequences
from both strands.

---

### Restriction site analysis

The project includes analysis of restriction enzyme recognition sites.

For example, the recognition sequence for **EcoRV** is searched
within DNA sequences:

```text
GATATC
```
The identified restriction site can then be used to determine the
resulting DNA fragments.

---

### Stop codon detection

The project identifies stop codons within coding DNA sequences.

The three standard stop codon are considered: 

```text
TAA
TAG
TGA
```

Their positions within the sequence are identified programmatically. 

---

## Sequence comparison

### Hamming distance 

The Hamming distance is used to compare two sequences of equal length.

It represents the number of nucleotide positions at which the two
sequences differ.

For example:

```text
Sequence 1: CCGTA
Sequence 2: ACGTC
```

The Hamming distance between these sequences is 2.

---

### Motif searching 

A custom sequence-searching approach is used to identify occurrences
of a specific motif within a biological sequence.

The function returns the positions where the motif is found, allowing
sequence patterns to be located programmatically.

---

### Point mutations 

The project also analyses nucleotide substitutions between sequences.

Substitutions are classified into:

Transitions
Transversions

The transition/transversion ratio is then calculated to characterise
the nucleotide changes observed between sequences.

---

### Phylogenetic analysis

The project includes basic phylogenetic analysis using a tree stored
in Newick format.

Biopython is used to:

- Read the phylogenetic tree.
- Explore relationships between sequences.
- Identify common ancestors.
- Modify tree visualisation properties.
- Display the resulting phylogenetic tree.

This provides an introduction to computational analysis of evolutionary
relationships between biological sequences.

---

### Pairwise sequence alignment 

Pairwise alignment is performed using Biopython's
`PairwiseAligner`.

The alignment is used to compare two biological sequences and identify
matching and mismatching positions.

The alignment can subsequently be represented as a matrix, providing
a visual representation of sequence similarity.

---

### Technologies

- Python 3
- Biopython
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

### Main Python concepts

- Functionc
- Loops and conditionals
- Strings
- List and dictionaries
- File handling
- DataFrames
- Sequence manipulation
- Data visualisation

---

## Repository structure 

```text
bioinformatics-sequence-analysis/
│
├── README.md
│
├── src/
│   ├── fasta_analysis.py
│   ├── sequence_analysis.py
│   ├── motifs.py
│   └── alignment.py
│
├── figures/
│   └── composicion_bases_AM711902-1.png
│   └── composicion_bases_NC_001802-1.png
│   └── composicion_bases_NC_019843-3.png
│   └── composicion_bases_NC_024512-1.png
│   └── composicion_bases_NT_004356-4.png
│   └── composicion_bases_NT_033779-5.png
│
└── notebooks/
    └── sequence_analysis.ipynb
```
--- 

## Workflow 

The analyses can be organised into the following workflow:

```text
FASTA sequences
       │
       ▼
Sequence parsing
       │
       ├── Nucleotide composition
       ├── GC content
       ├── Purine / pyrimidine content
       └── Sequence length
              │
              ▼
      Sequence analysis
              │
       ├── Motif detection
       ├── Restriction sites
       ├── Stop codons
       └── Mutations
              │
              ▼
     Sequence comparison
              │
       ├── Hamming distance
       ├── Pairwise alignment
       └── Phylogenetic analysis
```

---

## Skills demonstrated 

### Bioinformatics
- FASTA sequence analysis
- Nucleotide composition
- GC-content analysis
- Motif detection
- Restriction site analysis
- Codon analysis
- Mutation analysis
- Sequence comparison
- Phylogenetics
- Pairwise sequence alignment
### Programming & data analysis
- Python
- Biopython
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Biological data processing
- Data visualisation

---

## Academic context

This project was developed as part of a Master's programme in
Bioinformatics.

It focuses on applying Python programming and computational methods
to fundamental problems in biological sequence analysis.

---

## Author

### Sara Álvarez 

Master's Degree in Bioinformatics and Biostatistics| Bachelor's Degree in Genetics 

- Github: https://github.com/saraalv
- LinkedIn: www.linkedin.com/in/saraalvarezestevez

---

## License 

This project is intended for educational and portfolio purposes.
