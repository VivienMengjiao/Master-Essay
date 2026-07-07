# A Digital Humanities Approach to Characterizing Murderers in Agatha Christie's Detective Novels

This repository includes the data used and the visualizations created for the master thesis:
*"A Digital Humanities Approach to Characterizing Murderers in Agatha Christie's Detective Novels."*

The thesis argues that the results from distant reading align with Agatha Christie's conception of murderers found in previous research (through close reading) and reflect her moderate feminism.

Master's thesis by **Mengjiao Li**, University of Stuttgart, Institute for Literary Studies, Digital Humanities (submitted 04.12.2025).
Supervisors: Dr. Anselm Küsters (first), Dr. Nora Ketschik (second).

## Repository Content

The content of this GitHub repository is organized as follows:

1. **Primary Literature**
   * The eight selected novels by Agatha Christie are *not* included in this repository for copyright reasons (see Licensing section below). The bibliographic references can be found in the thesis.

2. **Visualizations of SNA**
   * Social network analysis visualizations created using Gephi

3. **Bar plots** of speech/appearance rates using R, with code in `R.data` format

4. **Character Modifiers**
   * Modifiers of murderers and detectives

5. **Sentiment Analysis**
   * Sentiment scores in CSV format
   * Visualizations of sentiment networks

6. **Linguistic Representations**
   * Linguistic representation data
   * Visualizations of linguistic representation

7. **t-SNE Visualizations**
   * Combination of all 8 novels with the names of target characters standardized
   * t-SNE visualizations of the murderers in these eight novels

8. **ontology design, Sparql Query and shinyAPP**
   * These are the new methodologies the author is learning to represent the relationships between the characters and their attributes.                

The data and visualizations are provided for further analysis and reuse in related research projects.

## Tools used

CATMA 7, Gephi, ezlinavis, AntConc, R, Word2Vec, Lexicoder Sentiment Dictionary (Young & Soroka, 2012). Full references are documented in the thesis.

## Licensing

This repository uses a **dual licensing scheme**, which is standard for open Digital Humanities projects:

| Component | License | File |
|-----------|---------|------|
| Source code (R scripts, etc.) | MIT License | [`LICENSE`](./LICENSE) |
| Data (annotations, CSV tables, network data, visualizations) | Creative Commons Attribution 4.0 International (CC BY 4.0) | [`LICENSE-DATA.md`](./LICENSE-DATA.md) |

In short:

- You are free to **use, modify, and redistribute** both the code and the data, including for commercial purposes.
- You must **give appropriate credit** by citing the author and linking to this repository.
- For the data, you must **indicate if changes were made**.

**Note on the primary texts:** Agatha Christie's novels remain under copyright in EU jurisdictions until approximately 2047. They are therefore *not* redistributed in this repository. Only the derived data (annotations, modifier tables, sentiment scores, network data, visualizations) created by the author are released under the licenses above.

## How to cite

> Li, Mengjiao (2025): *A Digital Humanities Approach to Characterizing Murderers in Agatha Christie's Detective Novels*. Master's Thesis, University of Stuttgart. Repository: https://github.com/VivienMengjiao/Master-Essay

## Contact

st183118@stud.uni-stuttgart.de
