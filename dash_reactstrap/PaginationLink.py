# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PaginationLink(Component):
    """A PaginationLink component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string | number; optional)
- aria_label (string; optional)
- className (string; optional)
- cssModule (dict; optional)
- next (boolean; optional)
- previous (boolean; optional)
- tag (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, aria_label=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, next=Component.UNDEFINED, previous=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria_label', 'className', 'cssModule', 'next', 'previous', 'tag']
        self._type = 'PaginationLink'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'aria_label', 'className', 'cssModule', 'next', 'previous', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PaginationLink, self).__init__(children=children, **args)

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
            return ('PaginationLink(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'PaginationLink(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
