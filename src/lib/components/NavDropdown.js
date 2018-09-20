import React from 'react';
import PropTypes from 'prop-types';
import { warnOnce, deprecated } from '../utils/utils';
import Dropdown from './Dropdown';

const propTypes = {
  disabled: PropTypes.bool,
  dropup: deprecated(PropTypes.bool, 'Please use the prop "direction" with the value "up".'),
  direction: PropTypes.oneOf(['up', 'down', 'left', 'right']),
  group: PropTypes.bool,
  isOpen: PropTypes.bool,
  nav: PropTypes.bool,
  active: PropTypes.bool,
  addonType: PropTypes.oneOfType([PropTypes.bool, PropTypes.oneOf(['prepend', 'append'])]),
  size: PropTypes.string,
  tag: PropTypes.string,
  toggle: PropTypes.func,
  children: PropTypes.node,
  className: PropTypes.string,
  cssModule: PropTypes.object,
  inNavbar: PropTypes.bool,
  setActiveFromChild: PropTypes.bool,
  children: PropTypes.node,
};

const defaultProps = {
  isOpen: false,
  direction: 'down',
  nav: false,
  active: false,
  addonType: false,
  inNavbar: false,
  setActiveFromChild: false
};

function NavDropdown(props) {
  warnOnce('The "NavDropdown" component has been deprecated.\nPlease use component "Dropdown" with nav prop.');
  return <Dropdown {...props} nav />;
}

NavDropdown.propTypes = propTypes;
NavDropdown.defaultProps = defaultProps;

export default NavDropdown
