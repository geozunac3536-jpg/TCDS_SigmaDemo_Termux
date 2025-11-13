# TCDS Σ-metrics Termux Demo — E-Veto sobre datos sintéticos (v0.1.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6358--9910-green.svg)](https://orcid.org/0009-0005-6358-9910)

## Descripción
Implementación mínima y auditable del motor Σ-metrics y del Filtro de Honestidad (E-Veto) de la Teoría de la Cromodinámica Sincrónica (TCDS) sobre datos sintéticos, ejecutada en un entorno Termux (Android). El avance consiste en: 
1. Calibrar Python+NumPy en un dispositivo móvil (Samsung S23).
2. Generar un conjunto sintético de eventos X_tc(t_C) con una forma Σ_base común y ruido controlado.
3. Definir un pipeline reproducible para calcular Σ-metrics (R_mean, LI, RMSE_SL, κΣ) en ventanas de t_C.
4. Aplicar un E-Veto entrópico (ΔH) que verifica que el sistema no declare coherencia Σ válida cuando no hay reducción real de entropía.

En este estado, el demo confirma que el filtro E-Veto no produce falsos positivos y que el entorno Termux funciona como laboratorio Q-driven portátil para futuros experimentos TCDS con datos sísmicos reales.

**Identificador:** tcds:sigma-demo-termux-v0.1.0  
**Versión:** 0.1.0  
**Fecha:** 2025-11-13  
**Parte de:** [Teoría de la Cromodinámica Sincrónica (TCDS)](https://doi.org/10.5281/zenodo.17520491)  
**Creador:** Genaro Carrasco Ozuna ([ORCID](https://orcid.org/0009-0005-6358-9910))  
**Keywords:** Teoría de la Cromodinámica Sincrónica, TCDS, Σ-metrics, Filtro de Honestidad, E-Veto, ΣFET, coherencia, t_C, Termux, Android, datos sintéticos, sistemas complejos, entropía, ΔH, Q-driven, φ-driven, Diseño Entrópico.

## Instalación
### En Termux (Android)
1. Instala Termux desde F-Droid o Google Play.
2. Ejecuta:
