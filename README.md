# 🚀 Cost-Optimized Infrastructure as Code (IaC) using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/github/license/summeet95/cost-optimization)
![Last Commit](https://img.shields.io/github/last-commit/summeet95/cost-optimization)
![Repo Size](https://img.shields.io/github/repo-size/summeet95/cost-optimization)
![Issues](https://img.shields.io/github/issues/summeet95/cost-optimization)

This project demonstrates how to combine **Machine Learning (ARIMA & LSTM)** with **Infrastructure as Code (Terraform)** to dynamically forecast cloud resource usage and automatically provision infrastructure.

It is the practical implementation of a postgraduate dissertation project at the University of West London.

---

## 📌 Features

- ⏱️ Time-series forecasting of cloud usage (CPU, memory)
- 🤖 ML models: ARIMA & LSTM
- ⚙️ Automatic Terraform `.tf` file generation from forecast
- 🌩️ Deployment-ready for AWS EC2 instances
- 📉 Cost comparison between static vs ML-based provisioning
- 🧪 Fully testable with unit tests and mock data

---

## 📁 Project Structure

```bash
ML-IaC-Cloud-Provisioning/
├── data/                   # Raw & cleaned cloud usage datasets
│   ├── raw/                # Unprocessed source data (e.g., AWS CUR, Google traces)
│   └── processed/          # Cleaned time-series for ML training
├── models/                # Saved ML model files (.h5, .pkl)
├── middleware/            # Python scripts to convert forecast → Terraform
│   ├── forecast_to_tf.py   # Main script to convert JSON → .tf
│   └── utils.py            # Helper functions
├── terraform/             # Static & generated Terraform configs
│   ├── main.tf             # Example base configuration
│   └── generated_tf_files/ # ML-driven autoscaling.tf output
├── notebooks/             # Jupyter notebooks for experimentation
│   └── model_training.ipynb
├── tests/                 # Unit tests
│   └── unit_tests.py
├── reports/               # Dissertation PDF or findings
├── train_arima.py         # ARIMA model trainer
├── train_lstm.py          # LSTM model trainer
├── requirements.txt       # All Python dependencies
└── README.md              # This file
```
🧠 Academic Context
This project is part of a Master's dissertation on:
“Cost-Optimized Infrastructure as Code: Dynamic Resource Allocation Using Machine Learning”
University of West London, 2025

📜 License
This project is open-source and available under the MIT License.

👨‍🎓 Author
Summeet Pokhrel
Postgraduate Student, MSc Software Engineering
University of West London
GitHub: @summeet95
