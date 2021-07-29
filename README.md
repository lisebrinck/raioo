This project is part of the product RAIOO developed in collaboration with Vitec-MV.

The folders and files in this project consist of the following:

### testdata:
- **goldstandard (folder):** for manually annotated data in txt-files
- **input (folder):** for unanalysed data consisting of targetwords and their spellings in txt-files
- **jotform (folder):** for the raw data extracted from Jotform in csv-files
- **output (folder):** for automatically analysed data in txt-files

### util:
- **targetwords:**
  - **data (folder):** all the data needed for tagging targetwords with spelling rules
  - **data_formatting (script):** script for formatting the data in the data folder
  - **error_tagging (script):** script for tagging targetwords with rules
  - **targetwords_with_rules (script):** file of the tagged targetwords
- **convert_csv_to_txt (script):** script for converting the raw Jotform-file in testdata/jotform to the input file in testdata/input
- **formatting (script):** script for formatting the input, goldstandard and error-tagged targetword files for use in analysis and evaluation

### top-level:
- **error_analysis (script):** script for the models that analyse the input data
- **evaluate (script):** script for evaluating the precision and recall of the model
- **evaluation (file):** file for the results of the evaluation
- **run_analysis (script):** script for executing the error:analysis and writing the result to a file in testdata/output