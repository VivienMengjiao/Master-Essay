# A Digital Humanities Approach to Characterizing Murderers in Agatha Christie's Detective Novels

Repository accompanying the Master's thesis by Mengjiao Li, University of Stuttgart, Institute for Literary Studies, Digital Humanities (submitted 04.12.2025).

Supervisors: Dr. Anselm Küsters (first), Dr. Nora Ketschik (second).

## Contents

This repository contains the **derived data, scripts, and visualizations** produced for the thesis, including:

- CATMA annotations (Quoted Speeches, Mentions) exported as XML / CSV
- Network data (nodes and edges) in GEXF format for Gephi
- Modifier tables and sentiment scores (CSV)
- R scripts for statistical tests (t-test) and t-SNE visualization
- Word2Vec configuration and t-SNE plots
- Network and sentiment-network visualizations (PNG / SVG)

The **full texts of Agatha Christie's novels are not included** in this repository, as they remain under copyright in EU jurisdictions until approximately 2047. The original sources are documented in the thesis bibliography; see `Section 6.1 Primary Literature`.

## Licensing

This repository uses a **dual licensing scheme**, which is standard for open Digital Humanities projects:

| Component | License | File |
|-----------|---------|------|
| Source code (R scripts, etc.) | MIT License | [`LICENSE`](./LICENSE) |
| Data (annotations, CSV tables, network data, visualizations) | Creative Commons Attribution 4.0 International (CC BY 4.0) | [`LICENSE-DATA.md`](./LICENSE-DATA.md) |

In short:

- You are free to **use, modify, and redistribute** both code and data, including for commercial purposes.
- You must **give appropriate credit** by citing the author and linking to this repository.
- For data, you must **indicate if changes were made**.

### How to cite

> Li, Mengjiao (2025): *A Digital Humanities Approach to Characterizing Murderers in Agatha Christie's Detective Novels*. Master's Thesis, University of Stuttgart. Repository: https://github.com/VivienMengjiao/Master-Essay

## Tools used

CATMA 7, Gephi, ezlinavis, AntConc, R, Word2Vec, Lexicoder Sentiment Dictionary. See the thesis (Section 6.3) for full references.

## Contact

st183118@stud.uni-stuttgart.de
