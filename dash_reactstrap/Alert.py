# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Alert(Component):
    """A Alert component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string | number; optional)
- className (string; optional)
- closeClassName (string; optional)
- closeAriaLabel (string; optional)
- cssModule (dict; optional)
- color (string; optional)
- fade (boolean; optional)
- isOpen (boolean; optional)
- tag (string; optional)
- transition (optional)
- innerRef (dict | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, closeClassName=Component.UNDEFINED, closeAriaLabel=Component.UNDEFINED, cssModule=Component.UNDEFINED, color=Component.UNDEFINED, fade=Component.UNDEFINED, isOpen=Component.UNDEFINED, toggle=Component.UNDEFINED, tag=Component.UNDEFINED, transition=Component.UNDEFINED, innerRef=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'closeClassName', 'closeAriaLabel', 'cssModule', 'color', 'fade', 'isOpen', 'tag', 'transition', 'innerRef']
        self._type = 'Alert'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'className', 'closeClassName', 'closeAriaLabel', 'cssModule', 'color', 'fade', 'isOpen', 'tag', 'transition', 'innerRef']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Alert, self).__init__(children=children, **args)

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
            return ('Alert(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Alert(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
