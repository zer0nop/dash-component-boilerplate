# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class UncontrolledCarousel(Component):
    """A UncontrolledCarousel component.


Keyword arguments:
- id (string | number; optional)
- items (list; required)
- indicators (boolean; optional)
- controls (boolean; optional)
- autoPlay (boolean; optional)
- activeIndex (number; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, items=Component.REQUIRED, indicators=Component.UNDEFINED, controls=Component.UNDEFINED, autoPlay=Component.UNDEFINED, activeIndex=Component.UNDEFINED, next=Component.UNDEFINED, previous=Component.UNDEFINED, goToIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'items', 'indicators', 'controls', 'autoPlay', 'activeIndex']
        self._type = 'UncontrolledCarousel'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'items', 'indicators', 'controls', 'autoPlay', 'activeIndex']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(UncontrolledCarousel, self).__init__(**args)

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
            return ('UncontrolledCarousel(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'UncontrolledCarousel(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
