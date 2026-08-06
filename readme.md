# folder structure of Email_spam_model

Email_spam_model/
├── .github/               # CI/CD workflows (e.g., GitHub Actions)
├── config/                # Hyperparameters and environment settings
│   └── train_config.yaml  
├── data/                  # Data storage (git-ignored except placeholders)
│   ├── raw/               # Immutable, original datasets
│   ├── processed/         # Cleaned and engineered features
│   └── external/          # Third-party or auxiliary data
├── models/                # Saved artifacts and binary weights
│   ├── checkpoints/       # Intermediate training epoch saves
│   └── production/        # Final serialized production models
├── notebooks/             # Jupyter notebooks for EDA and prototyping
│   └── 01_exploratory.ipynb
├── src/                   # Production-grade core Python packages
│   ├── __init__.py        
│   ├── data_loader.py     # Script to ingest and split data
│   ├── preprocess.py      # Feature engineering and cleaning logic
│   ├── model.py           # Neural network or model architecture definitions
│   └── utils.py           # Metrics, logging setups, and helpers
├── tests/                 # Unit tests for codebase stability
│   └── test_preprocess.py
├── .gitignore             # Strict filtering to block data/weights from Git
├── README.md              # Setup instructions and pipeline execution guide
├── requirements.txt       # Frozen environment dependencies
└── train.py               # Main execution script to launch training loops
