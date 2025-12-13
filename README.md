[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group19.git/HEAD?urlpath=lab/tree/main.ipynb)


## Overview

This project uses a variety of text analysis and visualization techniques to study the inaugural addresses of all presidents of the United States. The scientific motivation behind this is to identify common words and themes, measure sentiment, and discover how tone and language have evolved over time. Using NLP methods, with tools such as spaCy, we perform text processing and a linguistic analysis. We have visualized our results in ways including bar charts and sentiment summaries to show patterns across presidencies and identify outliers, as well as how party affiliation influences speech content, sentiment, and themes. ## Dataset
The dataset used in this project is the [Airbnb Cleaned Europe Dataset](https://www.kaggle.com/dipeshkhemani/airbnb-cleaned-europe-dataset) available on Kaggle. The dataset contains listings information of Airbnb accommodations in various European cities. The dataset is cleaned and preprocessed, making it suitable for data analysis and modeling tasks.

## Dataset

The dataset consists of 4 columns and 55 rows. Each row represents an inaugural speech, and the columns contain various attributes related to the speech, including the president name, president number, date, and the text of the speech. We also join the original dataset to party affiliation for some analyses, creating a fifth column. 

To use this dataset, download the CSV file from the [UCSB site](https://www.presidency.ucsb.edu/documents/inaugural-address) or use our make_data.py script.

## Project Website
The project's Myst website can be accessed [here](https://stat159.datahub.berkeley.edu/user/clara_reckhorn/myst-build/final-group19/?_t=1765598538130)

## Repository Structure

The repository is structured as follows:

* `data/`: Contains the raw dataset
* `main.ipynb`: Main project notebook, providing an overview of the analysis and results
* `make_data.py`: Script to create dataset in `/data`
* `test_make_data.py`: Script to test the script which creates dataset in `/data`
* `part1.ipynb`: Notebook containing analysis to answer pt1 from main noteboook
* `part2.ipynb`: Notebook containing analysis to answer pt2 from main noteboook
* `part3.ipynb`: Notebook containing analysis to answer pt3 from main noteboook
* `part4.ipynb`: Notebook containing analysis to answer pt4 from main noteboook
* `environment.yml`: Environment file with required packages for the project
* `Makefile`: Makefile to build JupyterBook for the repository and manage other tasks

## Setup and Installation

1. Clone this repository:
```python
git clone https://github.com/UCB-stat-159-f25/final-group19.git
cd final-group19
```
2. Create and activate the inaugural-address environment:
```python
mamba env create -f environment.yml --name inaugural-address
conda activate inaugural-address
```
3. Install the IPython kernel with the inaugural-address environment:
```python
python -m ipykernel install --user --name inaugural-address --display-name "inaugural-address"
```
	
## Testing
To run tests, we have the test_make_data.py file.

## License

This project is licensed under the MIT License.

## Additional Information
For more detailed information about the analysis and results, please refer to the main narrative notebook available here [here](https://ucb-stat-159-s23.github.io/project-Group28/main.html).