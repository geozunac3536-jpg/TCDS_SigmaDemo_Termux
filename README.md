# TCDS Σ-metrics Termux Demo + Evento Cero t_C Puebla–Morelos 2017

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17605698.svg)](https://doi.org/10.5281/zenodo.17605698)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6358--9910-green.svg)](https://orcid.org/0009-0005-6358-9910)

Este paquete integra:

- La **demo Σ-metrics en Termux** (datos sintéticos + E-Veto).
- El **Evento Cero TCDS**: índice t_C regional alrededor del sismo **M7.1 Puebla–Morelos (19/09/2017)**.
- La **landing page** ultraoscura para GitHub Pages.
- Scripts de cómputo y visualización, manifiesto t_C, resultados JSON y figuras PNG.

## Estructura

- `index.html`, `styles.css`, `banner_tcds_reloj_causal.svg`: landing híbrida (GitHub Pages).
- `manifest_tC_PueblaMorelos2017.json`: definición del Evento Cero y ventanas A1–A2–B–C–D.
- `scripts/compute_tC_index.py`: cálculo de t_C por ventana.
- `scripts/plot_sigma_demo.py`, `scripts/plot_tc_puebla_morelos.py`: generación de figuras.
- `results/tC_index_PueblaMorelos2017.json`: resultado consolidado del índice t_C.
- `docs/*.png`: plots listos para embeber en README o PDFs.
- `tests/*.py`: tests básicos (pytest) para validar comportamiento.

## Requisitos mínimos

```bash
pkg update && pkg upgrade
pkg install python git
pip install --upgrade pip
pip install numpy matplotlib pandas pytest
```

## Ejecución rápida (Termux o PC)

```bash
python scripts/compute_tC_index.py   --manifest manifest_tC_PueblaMorelos2017.json   --out results/tC_index_PueblaMorelos2017.json

python scripts/plot_sigma_demo.py
python scripts/plot_tc_puebla_morelos.py
```

## Citación

Carrasco, G. (2025).
*Evento Cero TCDS — Índice t_C Regional del Sismo M7.1 Puebla–Morelos (2017).* Zenodo.
https://doi.org/10.5281/zenodo.17605698
