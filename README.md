# Custom Higher-Order Functions for Data Analysis in Python

This project demonstrates the creation and use of custom higher-order functions for data analysis in Python. It provides reusable functional programming tools tailored for analyzing tabular data, such as sales records.

## Features
- Custom implementations of map, filter, reduce, and groupby functions
- Example usage with a real-world dataset (`1kSalesRec.csv`)
- Modular and extensible code for data transformation and aggregation
- Jupyter notebook (`project_guideline.ipynb`) for interactive exploration

## Files
- `project.py`: Main Python script containing custom higher-order functions and example usage
- `1kSalesRec.csv`: Sample sales records dataset for analysis
- `project_guideline.ipynb`: Notebook with project guidelines, explanations, and code walkthroughs

## Getting Started
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Custom-Higher-Order-Functions-for-Data-Analysis-in-Python
   ```
2. Install required Python packages (if any):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python project.py
   ```
4. Explore the notebook for interactive examples:
   Open `project_guideline.ipynb` in Jupyter or VS Code.

## Usage Example
```python
# Example: Using a custom filter function
def custom_filter(func, data):
    return [item for item in data if func(item)]

# Filter sales records with amount > 1000
filtered = custom_filter(lambda x: x['Amount'] > 1000, sales_data)
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
