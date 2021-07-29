This project is part of the product RAIOO developed for and in collaboration with Vitec-MV.
RAIOO is a tool for individual automatic configuration of a word prediction tool.
The folders and files in this project consist of the following:


### /testdata:
- **goldstandard _(folder)_:** for manually annotated data in txt-files
- **input _(folder)_:** for unanalysed data consisting of targetwords and their spellings in txt-files
- **jotform _(folder)_:** for the raw data extracted from Jotform in csv-files
- **output _(folder)_:** for automatically analysed data in txt-files


### /util:
- #### **targetwords _(folder)_:**
  - **data _(folder)_:** all the data needed for tagging targetwords with spelling rules
  - **data_formatting _(script)_:** script for formatting the data in the data folder
  - **error_tagging _(script)_:** script for tagging targetwords with rules
  - **targetwords_with_rules _(script)_:** file of the tagged targetwords
- **convert_csv_to_txt _(script)_:** script for converting the raw Jotform-file in testdata/jotform to the input file in testdata/input
- **formatting _(script)_:** script for formatting the input, goldstandard and error-tagged targetword files for use in analysis and evaluation


### The top level:
- **error_analysis _(script)_:** script for the models that analyse the input data
- **evaluate _(script)_:** script for evaluating the precision and recall of the model
- **evaluation _(file)_:** file for the results of the evaluation
- **run_analysis _(script)_:** script for executing the error_analysis and writing the result to a file in testdata/output