import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';

const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  children: PropTypes.node,
};

// TODO: notify dash of dropdown state

class ButtonDropdown extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    return (<Dropdown group {...this.props} isOpen={this.state.isOpen} toggle={this.toggle} />);
  }
}

ButtonDropdown.propTypes = propTypes;

export default ButtonDropdown;
