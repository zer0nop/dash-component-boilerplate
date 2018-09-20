import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';
import { deprecated } from '../utils/utils';

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

class UncontrolledDropdown extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle(e) {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    const { children, ...otherProps } = this.props;
    return (
      <Dropdown {...otherProps} isOpen={this.state.isOpen} toggle={this.toggle}>
        {children}
      </Dropdown>
    );
  }
}

UncontrolledDropdown.propTypes = propTypes;
UncontrolledDropdown.defaultProps = defaultProps;

export default UncontrolledDropdown