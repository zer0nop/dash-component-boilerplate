# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popover(Component):
    """A Popover component.


Keyword arguments:
- id (string | number; optional)
- placement (optional)
- target (optional)
- container (optional)
- boundariesElement (string; optional)
- isOpen (boolean; optional)
- disabled (boolean; optional)
- hideArrow (boolean; optional)
- className (string; optional)
- innerClassName (string; optional)
- placementPrefix (string; optional)
- cssModule (dict; optional)
- delay (optional): . delay has the following type: dict containing keys 'show', 'hide'.
Those keys have the following types: 
  - show (number; optional)
  - hide (number; optional) | number
- modifiers (dict; optional)
- offset (string | number; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, placement=Component.UNDEFINED, target=Component.UNDEFINED, container=Component.UNDEFINED, boundariesElement=Component.UNDEFINED, isOpen=Component.UNDEFINED, disabled=Component.UNDEFINED, hideArrow=Component.UNDEFINED, className=Component.UNDEFINED, innerClassName=Component.UNDEFINED, placementPrefix=Component.UNDEFINED, cssModule=Component.UNDEFINED, toggle=Component.UNDEFINED, delay=Component.UNDEFINED, modifiers=Component.UNDEFINED, offset=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'placement', 'target', 'container', 'boundariesElement', 'isOpen', 'disabled', 'hideArrow', 'className', 'innerClassName', 'placementPrefix', 'cssModule', 'delay', 'modifiers', 'offset']
        self._type = 'Popover'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'placement', 'target', 'container', 'boundariesElement', 'isOpen', 'disabled', 'hideArrow', 'className', 'innerClassName', 'placementPrefix', 'cssModule', 'delay', 'modifiers', 'offset']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Popover, self).__init__(**args)

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
            return ('Popover(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Popover(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
