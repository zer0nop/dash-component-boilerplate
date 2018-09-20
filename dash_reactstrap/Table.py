# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Table(Component):
    """A Table component.


Keyword arguments:
- id (string | number; optional)
- className (string; optional)
- cssModule (dict; optional)
- size (string; optional)
- bordered (boolean; optional)
- borderless (boolean; optional)
- striped (boolean; optional)
- inverse (optional)
- dark (boolean; optional)
- hover (boolean; optional)
- responsive (boolean | string; optional)
- tag (string; optional)
- responsiveTag (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, size=Component.UNDEFINED, bordered=Component.UNDEFINED, borderless=Component.UNDEFINED, striped=Component.UNDEFINED, inverse=Component.UNDEFINED, dark=Component.UNDEFINED, hover=Component.UNDEFINED, responsive=Component.UNDEFINED, tag=Component.UNDEFINED, responsiveTag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'cssModule', 'size', 'bordered', 'borderless', 'striped', 'inverse', 'dark', 'hover', 'responsive', 'tag', 'responsiveTag']
        self._type = 'Table'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'className', 'cssModule', 'size', 'bordered', 'borderless', 'striped', 'inverse', 'dark', 'hover', 'responsive', 'tag', 'responsiveTag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Table, self).__init__(**args)

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
            return ('Table(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Table(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
