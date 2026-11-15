# AI & Machine Learning Ecosystem & Hardware Verification
import sys
import numpy as np
import pandas as pd
import sklearn
import torch

def verify_ml_ecosystem():
    environment_specs = {
        "python_version": sys.version.split()[0],
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "sklearn_version": sklearn.__version__,
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "active_device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU"
    }
    print("=== AI & MACHINE LEARNING RUNTIME STATUS ===")
    for component, status in environment_specs.items():
        print(f"[{component}]: {status}")
    return environment_specs

if __name__ == "__main__":
    specs = verify_ml_ecosystem()
    assert specs["numpy_version"] is not None, "NumPy must be installed"
