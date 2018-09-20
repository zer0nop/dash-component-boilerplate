# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string | number; optional)
- isOpen (boolean; optional)
- autoFocus (boolean; optional)
- centered (boolean; optional)
- size (string; optional)
- keyboard (boolean; optional)
- role (string; optional)
- labelledBy (string; optional)
- backdrop (boolean | a value equal to: 'static'; optional)
- className (string; optional)
- wrapClassName (string; optional)
- modalClassName (string; optional)
- backdropClassName (string; optional)
- contentClassName (string; optional)
- external (a list of or a singular dash component, string or number; optional)
- fade (boolean; optional)
- cssModule (dict; optional)
- zIndex (number | string; optional)
- backdropTransition (optional)
- modalTransition (optional)
- innerRef (dict | string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, isOpen=Component.UNDEFINED, autoFocus=Component.UNDEFINED, centered=Component.UNDEFINED, size=Component.UNDEFINED, toggle=Component.UNDEFINED, keyboard=Component.UNDEFINED, role=Component.UNDEFINED, labelledBy=Component.UNDEFINED, backdrop=Component.UNDEFINED, onEnter=Component.UNDEFINED, onExit=Component.UNDEFINED, onOpened=Component.UNDEFINED, onClosed=Component.UNDEFINED, className=Component.UNDEFINED, wrapClassName=Component.UNDEFINED, modalClassName=Component.UNDEFINED, backdropClassName=Component.UNDEFINED, contentClassName=Component.UNDEFINED, external=Component.UNDEFINED, fade=Component.UNDEFINED, cssModule=Component.UNDEFINED, zIndex=Component.UNDEFINED, backdropTransition=Component.UNDEFINED, modalTransition=Component.UNDEFINED, innerRef=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'isOpen', 'autoFocus', 'centered', 'size', 'keyboard', 'role', 'labelledBy', 'backdrop', 'className', 'wrapClassName', 'modalClassName', 'backdropClassName', 'contentClassName', 'external', 'fade', 'cssModule', 'zIndex', 'backdropTransition', 'modalTransition', 'innerRef']
        self._type = 'Modal'
        self._namespace = 'dash_reactstrap'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'isOpen', 'autoFocus', 'centered', 'size', 'keyboard', 'role', 'labelledBy', 'backdrop', 'className', 'wrapClassName', 'modalClassName', 'backdropClassName', 'contentClassName', 'external', 'fade', 'cssModule', 'zIndex', 'backdropTransition', 'modalTransition', 'innerRef']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Modal, self).__init__(children=children, **args)

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
            return ('Modal(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Modal(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
