# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.


Keyword arguments:
- id (string | number; optional)
- placement (optional)
- target (optional)
- container (optional)
- isOpen (boolean; optional)
- disabled (boolean; optional)
- hideArrow (boolean; optional)
- boundariesElement (string; optional)
- className (string; optional)
- innerClassName (string; optional)
- arrowClassName (string; optional)
- cssModule (dict; optional)
- autohide (boolean; optional)
- placementPrefix (string; optional)
- delay (optional): . delay has the following type: dict containing keys 'show', 'hide'.
Those keys have the following types: 
  - show (number; optional)
  - hide (number; optional) | number
- modifiers (dict; optional)
- offset (string | number; optional)
- innerRef (string | dict; optional)
- trigger (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, placement=Component.UNDEFINED, target=Component.UNDEFINED, container=Component.UNDEFINED, isOpen=Component.UNDEFINED, disabled=Component.UNDEFINED, hideArrow=Component.UNDEFINED, boundariesElement=Component.UNDEFINED, className=Component.UNDEFINED, innerClassName=Component.UNDEFINED, arrowClassName=Component.UNDEFINED, cssModule=Component.UNDEFINED, toggle=Component.UNDEFINED, autohide=Component.UNDEFINED, placementPrefix=Component.UNDEFINED, delay=Component.UNDEFINED, modifiers=Component.UNDEFINED, offset=Component.UNDEFINED, innerRef=Component.UNDEFINED, trigger=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'placement', 'target', 'container', 'isOpen', 'disabled', 'hideArrow', 'boundariesElement', 'className', 'innerClassName', 'arrowClassName', 'cssModule', 'autohide', 'placementPrefix', 'delay', 'modifiers', 'offset', 'innerRef', 'trigger']
        self._type = 'Tooltip'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'placement', 'target', 'container', 'isOpen', 'disabled', 'hideArrow', 'boundariesElement', 'className', 'innerClassName', 'arrowClassName', 'cssModule', 'autohide', 'placementPrefix', 'delay', 'modifiers', 'offset', 'innerRef', 'trigger']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tooltip, self).__init__(**args)

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
            return ('Tooltip(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Tooltip(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
