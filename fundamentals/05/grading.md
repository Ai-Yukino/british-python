# `grading.md`

tl;dr

- clone the repo
- install and activate conda environment via `fundamentals/05/05-env.yml`
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
cd british-python/fundamentals/05
conda env create -f 05-env.yml
```

## Activate conda/mamba environment

Run

```
conda activate 05-env
```

## Generate `05.ipynb` file

While inside `british-python/fundamentals/05`, run

```
jupytext --to py 05.py
```

See the [jupytext docs](https://jupytext.readthedocs.io/en/latest/index.html) if you'd like more details.

## Open `05.ipynb`

Run

```
jupyter-lab
```

If you prefer the traditional Jupyter Notebook environment instead of the newer JupyterLab environment, then you can add it to the `05-env` environment with

```
conda install notebook
```

and then run

```
jupyter-notebook
```
