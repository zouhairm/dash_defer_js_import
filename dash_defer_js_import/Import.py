# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Import(Component):
    """A Import component.
This component is based on the Import sub-component of dash-grasia
See original implementation here:
https://github.com/Grasia/grasia-dash-components/blob/master/src/components/Import.react.js

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- src (string; optional): local or external source of the javascript to import"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, src=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'src']
        self._type = 'Import'
        self._namespace = 'dash_defer_js_import'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'src']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Import, self).__init__(**args)
