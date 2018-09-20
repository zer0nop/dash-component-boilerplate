# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Fade(Component):
    """A Fade component.


Keyword arguments:
- children (list | a list of or a singular dash component, string or number; optional)
- tag (string; optional)
- baseClass (string; optional)
- baseClassActive (string; optional)
- className (string; optional)
- cssModule (dict; optional)
- innerRef (dict | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, tag=Component.UNDEFINED, baseClass=Component.UNDEFINED, baseClassActive=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, innerRef=Component.UNDEFINED, timeout=Component.UNDEFINED, appear=Component.UNDEFINED, enter=Component.UNDEFINED, exit=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'tag', 'baseClass', 'baseClassActive', 'className', 'cssModule', 'innerRef']
        self._type = 'Fade'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'tag', 'baseClass', 'baseClassActive', 'className', 'cssModule', 'innerRef']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Fade, self).__init__(children=children, **args)

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
            return ('Fade(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Fade(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
