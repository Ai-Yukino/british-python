# `grading.md`

## Why are there so many instructions?

Jupyter notebooks (i.e. `.ipynb` files) are bad for version control.
I use a probably uncommon workflow with Jupyter notebooks (technically Jupyter Lab in my case) to mitigate this.
See the following links for more details

- https://goodresearch.dev/tidy.html#keep-jupyter-notebooks-tidy
- https://jupytext.readthedocs.io/en/latest/

---

## Clone this repo

Navidate to your desired grading folder, e.g. run

```
cd path/to/my/grading/folder
```

in your terminal. Then run

```
git clone git@github.com:Ai-Yukino/british-python
```

to clone this repo into that folder.

## Install conda/mamba environment for HW `01-py`

Run

```
cd british-python/fundamentals/01-py
conda env create -f 01-py.yml
conda activate 01-py
```

Then you can run

```
python --version
```

to make sure that you have successfully activated the environment, i.e. you should see

```
Python 3.10.2
```

as the output.

## Generate and view `01.ipynb`

Run

```
jupytext --sync 01.py
```

to recover the `01.ipynb` file. Then run

```
jupyter-lab
```

while you are in the `fundamentals/01` directory. Navigate to `01.ipynb` in JupyterLab to start grading.

## Remove conda/mamba environment for HW `01-py`

Run

```
conda deactivate 01-py
conda remove -n 01-py --all
```

Also run

```
conda clean -a
```

to clean your cahce. See the [conda docs](https://docs.conda.io/projects/conda/en/latest/commands/clean.html) for more info.

You can also run

```
conda info -e
```

to double-check that you have removed the `01-py` environment.
