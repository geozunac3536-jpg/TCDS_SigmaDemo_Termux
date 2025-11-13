import numpy as np
import os

# Directorios
home_dir = os.path.expanduser('~')
base_dir = os.path.join(home_dir, 'TCDS_TEC_TCDS_001')
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# Parámetros
N_GRID = 200
tc_grid = np.linspace(0.0, 1.0, N_GRID)

# Generar datos sintéticos (placeholder: forma sinusoidal + ruido para Σ_base)
base_shape = np.sin(2 * np.pi * tc_grid)  # Forma base común (ajusta a tu Σ_base TCDS)
noise = np.random.normal(0, 0.1, N_GRID)  # Ruido controlado
X_tc = base_shape + noise
X_tm = base_shape - noise  # Placeholder para X_tm

# Guardar
np.save(os.path.join(data_dir, 'tc_grid_demo.npy'), tc_grid)
np.save(os.path.join(data_dir, 'X_tc_demo.npy'), X_tc)
np.save(os.path.join(data_dir, 'X_tm_demo.npy'), X_tm)

print(f"✅ Datos sintéticos generados en: {data_dir}")
