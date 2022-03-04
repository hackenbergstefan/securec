# SecureC helpers

This repository was created and is maintained along lectures hold at [HSA](https://www.hs-augsburg.de/) using ChipWhisperer as side-channel analysis toolkit.
Although the [ChipWhisperer Python Framework](https://github.com/newaetech/chipwhisperer) included powerful batteries, downloading and capturing of traces is mainly done by Jupyter-Notebooks.
Especially for educational purposes it is often better to abstract the parts which are not focus of examination.

Thus, this repository was created. It aims the needs of the lecture and does not provide an universal claim.
It contains code for

- Compiling and downloading firmware code to ChipWhisperer Lite ARM and XMEGA
- Performing efficient CPA (Correlation Power Analysis) computations
- Creating plots related to CPA using [bokeh](https://bokeh.org/)

## Disclaimer and TODOs

Unfortunately this repository has to be improved. It lacks at least:

- Style check of code
- Continuous integration
