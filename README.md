# Insurance Expenses Linear Regression Project

This project aims to predict medical expenses using demographic and lifestyle data through a linear regression model. The dataset is sourced from a public insurance dataset.

## Project Structure

- **data/**: Contains the dataset used for the project.
  - `insurance.csv`: The primary dataset containing insurance information.

- **notebooks/**: Contains Jupyter notebooks for data analysis and model building.
  - `insurance_data_notebook.ipynb`: Jupyter notebook with steps for data analysis, data cleaning, exploratory data analysis (EDA), and model implementation.

- **scripts/**: Contains Python scripts for various steps of the project.
  - `data_cleaning.py`: Script for data cleaning.
  - `model_training.py`: Script for training the model.
  - `model_evaluation.py`: Script for evaluating the model.

## Project Workflow

### Step 1: Data Gathering

The data is sourced from the `insurance.csv` file, which contains the following columns:
- `age`: Age of the primary beneficiary
- `sex`: Gender of the primary beneficiary (male/female)
- `bmi`: Body Mass Index of the primary beneficiary
- `children`: Number of children/dependents covered by insurance
- `smoker`: Whether the beneficiary is a smoker (yes/no)
- `region`: Region of the beneficiary in the US
- `expenses`: Individual medical costs billed by health insurance

### Step 2: Data Cleaning

Clean the dataset to handle any missing values, encode categorical variables, and normalize numerical features. Refer to the `data_cleaning.py` script for detailed steps.

### Step 3: Exploratory Data Analysis (EDA)

Analyze the data to understand the relationships between different variables and the target variable (`expenses`). This step is detailed in the Jupyter notebook.

### Step 4: Model Building

Build and train a linear regression model using the cleaned dataset. The training process includes splitting the data into training and testing sets, fitting the model, and tuning hyperparameters. This step is covered in both the Jupyter notebook and the `model_training.py` script.

### Step 5: Model Evaluation

Evaluate the performance of the trained model using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. The evaluation process is documented in the Jupyter notebook and the `model_evaluation.py` script.

## Installation

To run the project, ensure you have Python installed along with the necessary libraries. You can install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt

## Usage
1. Clone the repository:

```bash
git clone https://github.com/yourusername/insurance-linear-regression.git

2. Navigate to the project directory:

```bash
cd insurance-linear-regression

3. Run the Jupyter notebook or individual scripts for different stages of the project.```

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License.
