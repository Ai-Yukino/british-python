# `grading.md`

tl;dr

- clone the repo
- install and activate conda environment via `fundamentals/01/01-env.yml`
- generate `01.ipynb` file from `01.py` using [jupytext](https://jupytext.readthedocs.io/en/latest/index.html)
- open notebook with JupyterLab

## Clone the repo

Run

```
git clone git@github.com:Ai-Yukino/british-python
```

in your terminal.

## Install conda/mamba environment

Run

```
cd british-python/fundamentals/04
conda env create -f 04-env.yml
```

## Activate conda/mamba environment

Run

```
conda activate 04-env
```

## Generate `04.ipynb` file

While inside `british-python/fundamentals/04`, run

```
jupytext --to py 04.py
```

See the [jupytext docs](https://jupytext.readthedocs.io/en/latest/index.html) if you'd like more details.

## Open `04.ipynb`

Run

```
jupyter-lab
```

If you prefer the traditional Jupyter Notebook environment instead of the newer JupyterLab environment, then you can add it to the `04-env` environment with

```
conda install notebook
```

and then run

```
jupyter-notebook
```
