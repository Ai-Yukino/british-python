# `grading.md`

tl;dr

- clone the repo
- install and activate conda environment via `fundamentals/08/08-env.yml`
- generate `08.ipynb` file from `08.py` using [jupytext](https://jupytext.readthedocs.io/en/latest/index.html)
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
cd british-python/fundamentals/08
conda env create -f 08-env.yml
```

## Activate conda/mamba environment

Run

```
conda activate 08-env
```

## Generate `08.ipynb` file

While inside `british-python/fundamentals/08`, run

```
jupytext --to py 08.py
```

See the [jupytext docs](https://jupytext.readthedocs.io/en/latest/index.html) if you'd like more details.

## Open `08.ipynb`

Run

```
jupyter-lab
```

If you prefer the traditional Jupyter Notebook environment instead of the newer JupyterLab environment, then you can add it to the `08-env` environment with

```
conda install notebook
```

and then run

```
jupyter-notebook
```
