# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CarouselCaption(Component):
    """A CarouselCaption component.


Keyword arguments:
- captionHeader (string; optional)
- captionText (string; required)
- cssModule (dict; optional)
- className (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, captionHeader=Component.UNDEFINED, captionText=Component.REQUIRED, cssModule=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['captionHeader', 'captionText', 'cssModule', 'className']
        self._type = 'CarouselCaption'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['captionHeader', 'captionText', 'cssModule', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['captionText']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CarouselCaption, self).__init__(**args)

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
            return ('CarouselCaption(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'CarouselCaption(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
