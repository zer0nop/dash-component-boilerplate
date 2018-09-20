import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';

const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  addonType: PropTypes.oneOf(['prepend', 'append']).isRequired,
  children: PropTypes.node,
};

// TODO: notify dash of dropdown state

class InputGroupButtonDropdown extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    return (<Dropdown {...this.props} isOpen={this.state.isOpen} toggle={this.toggle} />);
  }
}

InputGroupButtonDropdown.propTypes = propTypes;

export default InputGroupButtonDropdown;
