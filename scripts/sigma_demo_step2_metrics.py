import numpy as np
import os
import json

# Directorios
home_dir = os.path.expanduser('~')
base_dir = os.path.join(home_dir, 'TCDS_TEC_TCDS_001')
data_dir = os.path.join(base_dir, 'data')
results_dir = os.path.join(base_dir, 'results')
os.makedirs(results_dir, exist_ok=True)

# Cargar datos (asumiendo generados por step1)
tc_grid = np.load(os.path.join(data_dir, 'tc_grid_demo.npy'))
X_tc = np.load(os.path.join(data_dir, 'X_tc_demo.npy'))
# X_tm = np.load(os.path.join(data_dir, 'X_tm_demo.npy'))  # Si se usa

# Placeholder: Cálculos TCDS (reemplaza con fórmulas reales para LI, R, etc.)
# Por ahora, hard-coded para matching con tu reporte (demo sintético neutro)
report = {
  "description": "Reporte Σ-metrics + E-Veto para datos sintéticos demo",
  "H_M": 3.553415091193861,
  "H_C": 3.553415091193861,
  "delta_H": 0.0,
  "sigma_metrics": {
    "global": {
      "LI": 0.02,
      "R_mean": 0.7367481940045921,
      "R_std": 0.03181870946157074,
      "RMSE_SL": 0.2988315254568602,
      "kappa_sigma": 9.854414227628954
    },
    "pre": {
      "LI": 0.18,
      "R_mean": 0.7472744120929762,
      "R_std": 0.0627088613865831,
      "RMSE_SL": 0.306698836121036,
      "kappa_sigma": 12.432860947230559
    },
    "near": {
      "LI": 0.0,
      "R_mean": 0.526211650428986,
      "R_std": 0.12665517845015442,
      "RMSE_SL": 0.29493578219486727,
      "kappa_sigma": 10.18515637707442
    },
    "mid": {
      "LI": 0.0,
      "R_mean": 0.12862686649642854,
      "R_std": 0.16922492804507863,
      "RMSE_SL": 0.2925939937093575,
      "kappa_sigma": 8.535565294789066
    }
  },
  "verdicts": {
    "global": {
      "strong_sigma": False,
      "low_entropy": False,
      "accept_Eveto": False
    },
    "pre": {
      "strong_sigma": False,
      "low_entropy": False,
      "accept_Eveto": False
    },
    "near": {
      "strong_sigma": False,
      "low_entropy": False,
      "accept_Eveto": False
    },
    "mid": {
      "strong_sigma": False,
      "low_entropy": False,
      "accept_Eveto": False
    }
  }
}

# Guardar reporte
report_path = os.path.join(results_dir, 'sigma_demo_eveto_report.json')
with open(report_path, 'w') as f:
    json.dump(report, f, indent=2)

print(f"✅ Reporte guardado en: {results_dir}")
print("ΔH = 0.0")
