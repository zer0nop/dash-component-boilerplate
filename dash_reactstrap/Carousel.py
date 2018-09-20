# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Carousel(Component):
    """A Carousel component.


Keyword arguments:
- children (list; optional)
- id (string | number; optional)
- activeIndex (number; optional)
- keyboard (boolean; optional)
- pause (a value equal to: 'hover', false; optional)
- ride (a value equal to: 'carousel'; optional)
- interval (number | string | boolean; optional)
- slide (boolean; optional)
- cssModule (dict; optional)
- className (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, activeIndex=Component.UNDEFINED, next=Component.REQUIRED, previous=Component.REQUIRED, keyboard=Component.UNDEFINED, pause=Component.UNDEFINED, ride=Component.UNDEFINED, interval=Component.UNDEFINED, mouseEnter=Component.UNDEFINED, mouseLeave=Component.UNDEFINED, slide=Component.UNDEFINED, cssModule=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'activeIndex', 'keyboard', 'pause', 'ride', 'interval', 'slide', 'cssModule', 'className']
        self._type = 'Carousel'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'activeIndex', 'keyboard', 'pause', 'ride', 'interval', 'slide', 'cssModule', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['next', 'previous']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Carousel, self).__init__(children=children, **args)

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
            return ('Carousel(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Carousel(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
