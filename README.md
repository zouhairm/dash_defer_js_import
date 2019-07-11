# Dash Defer JS Import

Dash Defer JS Import is a Dash component library.

Its purpose is to defer loading JS scripts until after the Dash React elements have loaded.

# Installation

The package has been released to pypi and npm.
Easy thing is to install using pip:
```
pip install dash_defer_js_import
``` 

To install from source, clone the repo and

```
npm install
npm run build:all
python setup.py sdist
pip install dist/dash_defer_js_import-0.0.1.tar.gz
```
Note: his assumes you have the requirements already installed, if not, see requirements.txt
Might want to use venv to not mess up your own repo ...)

# Usage:
```
import dash_defer_js_import as dji

# Dash server initi and layout setup
# ...

app.layout = html.Article(dji.Import(src="./path/to/script.js"))

```

# Credits 
This component is based on the [grasia-dash-component](https://github.com/Grasia/grasia-dash-components)

It was initialized using cookiecutter thanks to the [https://github.com/plotly/dash-component-boilerplate.git](das-component-boilerplate) cookiecutter .



