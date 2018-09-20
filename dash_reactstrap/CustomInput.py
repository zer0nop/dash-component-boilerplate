# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CustomInput(Component):
    """A CustomInput component.


Keyword arguments:
- children (a list of or a singular dash component, string or number | list; optional)
- className (string; optional)
- id (string | number; required)
- type (string; required)
- label (a list of or a singular dash component, string or number; optional)
- inline (boolean; optional)
- valid (boolean; optional)
- invalid (boolean; optional)
- bsSize (string; optional)
- cssModule (dict; optional)
- innerRef (dict | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, className=Component.UNDEFINED, id=Component.REQUIRED, type=Component.REQUIRED, label=Component.UNDEFINED, inline=Component.UNDEFINED, valid=Component.UNDEFINED, invalid=Component.UNDEFINED, bsSize=Component.UNDEFINED, cssModule=Component.UNDEFINED, innerRef=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'className', 'id', 'type', 'label', 'inline', 'valid', 'invalid', 'bsSize', 'cssModule', 'innerRef']
        self._type = 'CustomInput'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'className', 'id', 'type', 'label', 'inline', 'valid', 'invalid', 'bsSize', 'cssModule', 'innerRef']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id', 'type']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CustomInput, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('CustomInput(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'CustomInput(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
