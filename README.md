# TensorFlow TARNET Architecture for Economics Model

**From Classical Econometrics to Causal Machine Learning**

This project demonstrates the transition from classical Structural Vector Autoregression (SVAR) econometric methods to modern causal machine learning approaches for analyzing macroeconomic policy impacts. Using a Treatment-Agnostic Representation Network (TARNet), we estimate the causal effect of LTV (Loan-to-Value) tightening policies on housing price changes.

## Features

- **Nonlinear relationships** between macroeconomic variables
- **Heterogeneous treatment effects** across different regions and economic conditions
- **Counterfactual predictions** for policy evaluation
- **Individual Treatment Effects (ITE)** and **Average Treatment Effects (ATE)** estimation

## Project Structure

```
.
├── [1]BasicTensorFlow.ipynb          # Basic TensorFlow tutorial notebook
├── [2]TARNET-example.ipynb           # TARNET implementation example
├── TARNET_Project_Documentation.md   # Comprehensive project documentation
├── TARNET_Project_Documentation.pdf  # PDF version of documentation
├── data_exports/                     # Preprocessed data splits
│   ├── train_data.csv
│   ├── val_data.csv
│   ├── test_data.csv
│   └── README.md
├── generate_pdf_documentation.py     # Script to generate PDF documentation
└── README.md                         # This file
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install tensorflow pandas numpy scikit-learn matplotlib seaborn
   ```

2. **Run the notebooks:**
   - Start with `[1]BasicTensorFlow.ipynb` for TensorFlow basics
   - Then explore `[2]TARNET-example.ipynb` for the TARNET implementation

3. **Load the data:**
   ```python
   import pandas as pd
   
   train_df = pd.read_csv('data_exports/train_data.csv')
   val_df = pd.read_csv('data_exports/val_data.csv')
   test_df = pd.read_csv('data_exports/test_data.csv')
   ```

## Documentation

For detailed documentation, see:
- **Markdown:** `TARNET_Project_Documentation.md`
- **PDF:** `TARNET_Project_Documentation.pdf`
- **HTML:** `TARNET_Project_Documentation.html`

## Key Results

The model successfully estimates:
- **Average Treatment Effect (ATE)**: Overall policy impact
- **Individual Treatment Effects (ITE)**: Person-specific policy impacts
- **Conditional Average Treatment Effects (CATE)**: Treatment effects conditional on covariates

## Requirements

- Python 3.8+
- TensorFlow 2.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Author

**Dimas Widiantoro**

## License

This project is open source and available for educational and research purposes.

## Citation

If you use this code in your research, please cite:

```
TensorFlow TARNET Architecture for Economics Model
Author: Dimas Widiantoro
Repository: https://github.com/dimasmukhlas/TensorFlow-TARNET-arch-economics-model
```

