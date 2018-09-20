# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PopperContent(Component):
    """A PopperContent component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string | number; optional)
- className (string; optional)
- placement (string; optional)
- placementPrefix (string; optional)
- arrowClassName (string; optional)
- hideArrow (boolean; optional)
- tag (string; optional)
- isOpen (boolean; optional)
- cssModule (dict; optional)
- offset (string | number; optional)
- fallbackPlacement (string | list; optional)
- flip (boolean; optional)
- container (optional)
- target (optional)
- modifiers (dict; optional)
- boundariesElement (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, placement=Component.UNDEFINED, placementPrefix=Component.UNDEFINED, arrowClassName=Component.UNDEFINED, hideArrow=Component.UNDEFINED, tag=Component.UNDEFINED, isOpen=Component.UNDEFINED, cssModule=Component.UNDEFINED, offset=Component.UNDEFINED, fallbackPlacement=Component.UNDEFINED, flip=Component.UNDEFINED, container=Component.UNDEFINED, target=Component.UNDEFINED, modifiers=Component.UNDEFINED, boundariesElement=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'placement', 'placementPrefix', 'arrowClassName', 'hideArrow', 'tag', 'isOpen', 'cssModule', 'offset', 'fallbackPlacement', 'flip', 'container', 'target', 'modifiers', 'boundariesElement']
        self._type = 'PopperContent'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'className', 'placement', 'placementPrefix', 'arrowClassName', 'hideArrow', 'tag', 'isOpen', 'cssModule', 'offset', 'fallbackPlacement', 'flip', 'container', 'target', 'modifiers', 'boundariesElement']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PopperContent, self).__init__(children=children, **args)

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
            return ('PopperContent(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'PopperContent(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
