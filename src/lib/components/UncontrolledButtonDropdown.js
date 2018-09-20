import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ButtonDropdown from './ButtonDropdown';

const propTypes = {
  children: PropTypes.node,
};

class UncontrolledButtonDropdown extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    return <ButtonDropdown {...this.props} isOpen={this.state.isOpen} toggle={this.toggle} />;
  }
}

UncontrolledButtonDropdown.propTypes = propTypes;

export default UncontrolledButtonDropdown;
