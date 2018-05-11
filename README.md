# EVA_Instrumentality
This project is aimed at helping researchers submit to European Variant Archive with ease by aiding completion of metadata required by the archive.

What you will need:
* All your variant files (vcf, gff, bed, etc.) organized as instructed below
* *python2*
* python module *openpyxl*
  * To install openpyxl, run the following code:
     ```shell
     pip install openpyxl
     ```
  * You can check if you have *openpyxl* available by doing the following:
    ```
    python2
    >>> from openpyxl import Workbook
    ```
  * Once you have *openpyxl* installed, this should run without errors issued.
  * Visit [openpyxl website](https://openpyxl.readthedocs.io/en/stable/) for more information and help
* (Optional) user_info.config file
* (Optional) project_info.config file
* (Optional) analysis_info.config file


Get started:

Copy this repository to your local machine:
```shell
git clone https://github.com/SichongP/EVA_Instrumentality
cd EVA_Instrumentality
```

Organize your files:

The program relies on your file structure to determine the relationships between your projects, analyses, and files. Thus, it is crucial that you organize your files correctly for the program to generate correct metadata file.

*Alternatively, you can refer to FAQ to make your own metadata file if you do not wish to re-organize your files*

You should have a folder for each project. 

All analyses associated with such project should be put in their own folder under the project folder. 

Variant files associated with each analysis should be put under the analysis folder.

info.config file should be put directly under the project/analysis folder they belong to.

See below structure (trailing slash ```\``` indicates a directory instead of a file)

* project1/
   * project_info.config (optional)
   * analysis1/
      * analysis_info.config (optional)
      * file1_1.vcf
      * file1_2.vcf
    * analysis2/
      * analysis_info.config (optional)
      * file2_1.vcf
      * file2_2.vcf
* project2/
   * project_info.config (optional)
   * analysis3/
      * analysis_info.config (optional)
      * file3_1.vcf
      * file3_2.vcf
    * analysis4/
      * analysis_info.config (optional)
      * file4_1.vcf
      * file4_2.vcf
