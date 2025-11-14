🌑 TCDS — Evento Cero (Puebla–Morelos 2017) + Σ-metrics Termux Demo

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17605698.svg)](https://doi.org/10.5281/zenodo.17605698)
![Release](https://img.shields.io/github/v/release/geozunac3536-jpg/TCDS_EventoCero_tC_PueblaMorelos2017)
![Status](https://img.shields.io/badge/Status-Estable-%2300ffad)

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.17605698">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.17605698.svg" width="260">
  </a>
</p><p align="center">
  <img src="https://img.shields.io/badge/Framework-TCDS-%2300e5ff.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Q--driven-ENGINEERING-%23bb00ff.svg?style=for-the-badge">
</p>Bienvenido al repositorio oficial del Evento Cero TCDS, donde convergen:

El Índice t_C Regional aplicado al sismo M7.1 Puebla–Morelos (19/09/2017)

El motor Σ-metrics y el Filtro de Honestidad (E-Veto)

Una implementación Termux–Android, totalmente portátil, reproducible y auditable


Este repositorio está enlazado a Zenodo mediante el DOI oficial:

> 🔗 DOI: https://doi.org/10.5281/zenodo.17605698



Es un nodo FARO dentro del ecosistema TCDS.


---

🌒 Contenido del repositorio

📌 1. Evento Cero TCDS — Puebla–Morelos 2017

Incluye:

manifest_tC_PueblaMorelos2017.json — Manifiesto del evento

compute_tC_index.py — Motor Σ reducido

tC_index_PueblaMorelos2017.json — Resultado oficial

PDF técnico para expertos

Preprint científico asociado al DOI


Este evento representa la primera ejecución operacional del índice t_C.


---

📌 2. Σ-metrics Termux Demo — E-Veto sobre datos sintéticos

Versión v0.1.0, validación inicial del pipeline:

Cálculo de Σ-metrics (LI, R, RMSE_SL, κΣ)

Aplicación del E-Veto (ΔH < –0.2)

Demostración de un laboratorio Q-driven portátil en un Samsung S23


Base fundamental para el sistema sísmico TCDS.


---

🛡️ Badges técnicos

   


---

🌘 Descripción técnica

Este repositorio implementa el núcleo del marco Q–Σ–φ:

Cálculo del Índice t_C

Ventanas palíndromas A1–A2–B–C–D

Motor Σ determinista y portable

Análisis E-Veto evitando apofenia

Auditoría completa mediante JSON


✔ Resultado clave

Ventana	LI	R	ΔH	t_C

B (Pre)	0.88	0.92	–0.22	1.03


Interpretación:

Coherencia elevada antes del evento

Caída de entropía (ΔH < 0)

Incremento claro de t_C

Patrón consistente con tensión causal TCDS



---

📱 Instalación en Termux (Android)

pkg update && pkg upgrade
pkg install python
pip install numpy pandas

Clonar:

git clone https://github.com/geozunac3536-jpg/TCDS_EventoCero_tC_PueblaMorelos2017.git
cd TCDS_EventoCero_tC_PueblaMorelos2017

Ejecutar el índice t_C:

python scripts/compute_tC_index.py \
  --manifest manifest_tC_PueblaMorelos2017.json \
  --out results/tC_index_PueblaMorelos2017.json


---

🌕 Cómo citar

Carrasco, G. (2025). Evento Cero TCDS — Índice t_C Regional del Sismo  
M7.1 Puebla–Morelos (2017). Zenodo.  
https://doi.org/10.5281/zenodo.17605698


---

🌑 Licencias

Código: MIT

Documentación: CC BY 4.0

Marco TCDS: DOI oficial → https://doi.org/10.5281/zenodo.17520491



---

🛰️ Ecosistema TCDS

Este repositorio forma parte directa de:

Σ-metrics

ΣFET / SYNCTRON

Reloj Causal (t_C Engine)

CSL-H

Sistema Predictivo Sísmico TCDS



---

🎯 Estado actual

✔ Evento Cero completo
✔ t_C validado
✔ Motor Σ funcional en Termux
✔ DOI enlazado
✔ Documentación experta incluida
⬜ Integración multicanal real (TEC, Kp, Dst, sismogramas)


---
