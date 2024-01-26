# Modelling Epidemics: The Efficacy of Contact Tracing

---
This project repository includes all the necessary code for conducting epidemic simulations and creating the graphs presented in the report. Please note that the raw data used for data visualization and analysis within the project is not included within this repository due to the excessive size of experimental results. However, experiments are reproducible using the code provided.

### Setting Up the Python Environment

To prepare the simulation environment, execute the following commands:

```bash
> virtualenv venv
> source venv/bin/activate
> pip install -r requirements.txt
````
Note that as of 01/01/2024 the epydemic synchronousdynamics.py contains issues with a revised version under the dev branch. Please use this version when running  simulations.

### Running Simulations

To run specific simulations, navigate to the directory containing the simulation and run the following command to execute the notebook:
```bash
jupyter nbconvert --execute --to notebook {NOTEBOOK-TO-RUN}.ipynb
```

Replace {NOTEBOOK-TO-RUN} with the name of the notebook you want to run. This will run the notebook and save the output to a new notebook. To view the output, open the new notebook.

Each experiment notebook will generate a subdirectory `/datasets` containing the data collected from the simulations. This data is then used for subsequent visualisation generation, processed by a corresponding `graph.ipynb` notebook
## Directory Structure

Each experiment section will have its own directory with corresponding parameters .py file setting the parameter space of the corrisponding simulation.

```
project
├── README.md
├── apx
│   └── a1
│       └── sir.ipynb
├── ch_2-background
│   ├── fig_2_2-sir-example
│   │   └── sir.ipynb
│   └── fig_2_4-seir-example
│       └── seir.ipynb
├── ch_6-implementation-and-verification
│   ├── fig_6_1_b-adaptive-seir-implmentation-and-verification
│   │   ├── adaptive-seir.ipynb
│   │   ├── fig_6_1.ipynb
│   │   └── parameters.py
│   └── fig_6_2-sirq-implmentation-and-verification
│       ├── fig_6_2.ipynb
│       ├── ks-test.ipynb
│       ├── limerick-data
│       │   └── ...
│       ├── parameters.py
│       ├── sirq.ipynb
├── ch_7-investigation
│   ├── sec_7_1_test_trace_and_isolate
│   │   ├── adaptive-seir.ipynb
│   │   ├── data-analysis.ipynb
│   │   ├── fig7_1.ipynb
│   │   ├── fig7_2.ipynb
│   │   ├── fig7_3.ipynb
│   │   └── parameters.py
│   ├── sec_7_2_preemptive_quarantine 
│   │   ├── fig_7_4.ipynb
│   │   ├── fig_7_5.ipynb
│   │   ├── parameters.py
│   │   └── sirq.ipynb
│   └── sec_7_3_test_trace_and_preemptively_isolate
│       ├── adaptive-seir.ipynb
│       ├── data-analysis.ipynb
│       ├── fig_7_7.ipynb
│       ├── graph.ipynb
│       └── parameters.py
└── requirements.txt

```


