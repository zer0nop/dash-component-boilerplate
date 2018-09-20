# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CardImg(Component):
    """A CardImg component.


Keyword arguments:
- id (string | number; optional)
- tag (string; optional)
- top (boolean; optional)
- bottom (boolean; optional)
- className (string; optional)
- cssModule (dict; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, tag=Component.UNDEFINED, top=Component.UNDEFINED, bottom=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'tag', 'top', 'bottom', 'className', 'cssModule']
        self._type = 'CardImg'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'tag', 'top', 'bottom', 'className', 'cssModule']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CardImg, self).__init__(**args)

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
            return ('CardImg(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'CardImg(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
