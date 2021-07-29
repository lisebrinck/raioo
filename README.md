This project is part of the product RAIOO developed for and in collaboration with Vitec-MV.
RAIOO is a tool for individual automatic configuration of a word prediction tool.
The folders and files in this project consist of the following:


### `/testdata`:
- **`goldstandard`** _(folder)_: for manually annotated data in txt-files
- **`input`** _(folder)_: for unanalysed data consisting of targetwords and their spellings in txt-files
- **`jotform`** _(folder)_: for the raw data extracted from Jotform in csv-files
- **`output`** _(folder)_: for automatically analysed data in txt-files


### `/util`:
- #### **`targetwords`** _(folder)_:
  - **`data`** _(folder)_: all the data needed for tagging targetwords with spelling rules
  - **`data_formatting`** _(script)_: formats the data in the data folder
  - **`error_tagging`** _(script)_: tags targetwords with spelling rules
  - **`targetwords_with_rules`** _(file)_: contains the targetwords tagged with spelling rules
- **`convert_csv_to_txt`** _(script)_: converts the raw Jotform-file in testdata/jotform to the input file in testdata/input
- **`formatting`** _(script)_: formats the input, goldstandard and error-tagged targetword files for use in analysis and evaluation


### The top level:
- **`error_analysis`** _(script)_: the models that analyse the input data
- **`evaluate`** _(script)_: evaluates the precision and recall of the model
- **`evaluation`** _(file)_: contains the results of the evaluation
- **`run_analysis`** _(script)_: executes the error_analysis and writes the result to a file in testdata/output
