This workflow will produce a sample metadata file with minimum information filled.
1. Clone this repository
```shell
git clone https://github.com/SichongP/EVA_Instrumentality
cd EVA_Instrumentality
```

2. Test if you have *python* and *openpyxl* installed
```python
python2
>>> from openpyxl import Workbook
```
You should not see any error message if you have them available on your machine. Otherwise run the following code to install *openpyxl*:
**Only run the following code if you don't have *openpyxl* installed**
```
pip install openpyxl
```

3. Take a look at sample_structure directory which demostrates how to organize your files
```shell
find sample_structure
```

4. Take a look at user_info.config file which demostrates how to make your own config file
```shell
less src/user_info.config
```

5. Run mkmetadata with user_info.config file:
```shell
chmod +x mkmetadata
./mkmetadata --user src/user_info.config --out test.xlsx ./sample_structure
```
You should see output like this:
```
No project info file found in sample_structure/equine_IMM, be sure you input them manually
No analysis info file found in sample_structure/equine_IMM/IMM_CGAS, be sure you input them manually
equine_NAD_CGAS
No analysis info file found in sample_structure/equine_NAD_CGAS/CGAS_analysis, be sure you input them manually
Unrecognized file project_info.config, ignoring...
No analysis info file found in sample_structure/equine_NAD_CGAS/WGAS_analysis, be sure you input them manually
```
You are seeing theses warnings because we don't have many of the config files available for the program to use. You thus need to input these data once you have test.xlsx
