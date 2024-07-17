Chapter-1/
  ├── 01_Introduction_to_Python/
  ├── 02_Python_Installation_and_Setup/
  ├── 03_Basic_Syntax_and_Data_Types/
  ├── 04_Control_Structures/
  ├── 05_Functions/
  ├── 06_Data_Structures/
  ├── 07_Input_and_Output/
  ├── 08_Error_Handling/
  ├── 09_Basic_Python_Libraries/

# Demo Python Scripts

This repository contains two Python scripts: one for basic data analysis and visualization, and another to demonstrate the power and versatility of Python through web scraping, data manipulation, and data visualization.

## Scripts

### Script 1: Educational Data Analysis Script

#### Features
- Load a dataset
- Perform basic data analysis
- Create and display visualizations (histogram, scatter plot, bar plot)
- Save visualizations as image files

#### Requirements
- Python 3.x
- Pandas
- Matplotlib

#### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo-name
   ```
3. Install the required libraries:
   ```sh
   pip install pandas matplotlib
   ```

#### Usage
1. Place your dataset (e.g., `data.csv`) in the project directory.
2. Modify the script to specify the correct column names for your dataset.
3. Run the script:
   ```sh
   python script.py
   ```

### Script 2: Powerful Language Demonstration Script

#### Features
- Fetch data from a web page
- Process and analyze the data
- Create and display visualizations
- Save visualizations as image files

#### Requirements
- Python 3.x
- Requests
- BeautifulSoup4
- Pandas
- Matplotlib

#### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo-name
   ```
3. Install the required libraries:
   ```sh
   pip install requests beautifulsoup4 pandas matplotlib
   ```

#### Usage
1. Run the script:
   ```sh
   python demo_script.py
   ```

#### Explanation
1. **Fetch Data from the Web**: The script uses the `requests` library to fetch the HTML content from the TIOBE index website.
2. **Parse the HTML Content**: Using `BeautifulSoup`, the script parses the HTML content to extract data on the top programming languages.
3. **Process and Analyze the Data**: The extracted data is converted into a Pandas DataFrame for easy manipulation and analysis. The script processes the data to clean it and convert the ratings to a numeric format.
4. **Visualize the Results**: The script uses `Matplotlib` to create a bar chart showing the popularity of the top programming languages. The chart is saved as an image file and also displayed.
