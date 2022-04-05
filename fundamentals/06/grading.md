# `grading.md`

tl;dr

- clone the repo
- install and activate conda environment via `fundamentals/06/06-env.yml`
- generate `06.ipynb` file from `06.py` using [jupytext](https://jupytext.readthedocs.io/en/latest/index.html)
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
cd british-python/fundamentals/06
conda env create -f 06-env.yml
```

## Activate conda/mamba environment

Run

```
conda activate 06-env
```

## Generate `06.ipynb` file

While inside `british-python/fundamentals/06`, run

```
jupytext --to py 06.py
```

See the [jupytext docs](https://jupytext.readthedocs.io/en/latest/index.html) if you'd like more details.

## Open `06.ipynb`

Run

```
jupyter-lab
```

If you prefer the traditional Jupyter Notebook environment instead of the newer JupyterLab environment, then you can add it to the `06-env` environment with

```
conda install notebook
```

and then run

```
jupyter-notebook
```
