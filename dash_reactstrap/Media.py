# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Media(Component):
    """A Media component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string | number; optional)
- body (boolean; optional)
- bottom (boolean; optional)
- className (string; optional)
- cssModule (dict; optional)
- heading (boolean; optional)
- left (boolean; optional)
- list (boolean; optional)
- middle (boolean; optional)
- object (boolean; optional)
- right (boolean; optional)
- tag (string; optional)
- top (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, body=Component.UNDEFINED, bottom=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, heading=Component.UNDEFINED, left=Component.UNDEFINED, list=Component.UNDEFINED, middle=Component.UNDEFINED, object=Component.UNDEFINED, right=Component.UNDEFINED, tag=Component.UNDEFINED, top=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'body', 'bottom', 'className', 'cssModule', 'heading', 'left', 'list', 'middle', 'object', 'right', 'tag', 'top']
        self._type = 'Media'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'body', 'bottom', 'className', 'cssModule', 'heading', 'left', 'list', 'middle', 'object', 'right', 'tag', 'top']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Media, self).__init__(children=children, **args)

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
            return ('Media(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Media(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
