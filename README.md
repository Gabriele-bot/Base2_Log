# Base2_Log  

 ## Code 

The repository is organized as follows:
- **`code_generator.py`**: script that automatically generates the verilog file of an AXI4-stream compliant base2 logarithm;
- **`LUT_LOG.v`**: output verilog file;
- **`LOG_tests.ipynb`**: notebook which contains some tests;  
- **`PYNQ_overlays_files`**: files thal will be loaded in the PYNQ-Z2 board;
- **`PYNQ_notebook`**: python notebook with some tests on the PYNQ board;  
- - **`report`**: results of three different methods for computing the log2; 

In the future the PYNQ project will be added, in which some random inputs will be sent to the PL via a DMA, then the log will be computed and the result array will be sent back (via DMA again) and the error will be evaluated.  

<center>
    <img src="report/Images/PYNQ_LUT_res.png" alt="Drawing" style="width: 500px"/>
</center>

<center>
    <img src="report/Images/PYNQ_TE_res.png" alt="Drawing" style="width: 500px"/>
</center>

<center>
    <img src="report/Images/PYNQ_POLY_res.png" alt="Drawing" style="width: 500px"/>
</center>
