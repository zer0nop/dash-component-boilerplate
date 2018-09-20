# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Dropdown(Component):
    """A Dropdown component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- disabled (boolean; optional)
- dropup (optional)
- direction (a value equal to: 'up', 'down', 'left', 'right'; optional)
- group (boolean; optional)
- isOpen (boolean; optional)
- nav (boolean; optional)
- active (boolean; optional)
- addonType (boolean | a value equal to: 'prepend', 'append'; optional)
- size (string; optional)
- tag (string; optional)
- className (string; optional)
- cssModule (dict; optional)
- inNavbar (boolean; optional)
- setActiveFromChild (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, disabled=Component.UNDEFINED, dropup=Component.UNDEFINED, direction=Component.UNDEFINED, group=Component.UNDEFINED, isOpen=Component.UNDEFINED, nav=Component.UNDEFINED, active=Component.UNDEFINED, addonType=Component.UNDEFINED, size=Component.UNDEFINED, tag=Component.UNDEFINED, toggle=Component.UNDEFINED, className=Component.UNDEFINED, cssModule=Component.UNDEFINED, inNavbar=Component.UNDEFINED, setActiveFromChild=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'disabled', 'dropup', 'direction', 'group', 'isOpen', 'nav', 'active', 'addonType', 'size', 'tag', 'className', 'cssModule', 'inNavbar', 'setActiveFromChild']
        self._type = 'Dropdown'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'disabled', 'dropup', 'direction', 'group', 'isOpen', 'nav', 'active', 'addonType', 'size', 'tag', 'className', 'cssModule', 'inNavbar', 'setActiveFromChild']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Dropdown, self).__init__(children=children, **args)

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
            return ('Dropdown(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Dropdown(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
