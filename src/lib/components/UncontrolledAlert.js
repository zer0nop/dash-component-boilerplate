import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Alert from './Alert';
import Fade from './Fade';

const propTypes = {
  children: PropTypes.node,
  className: PropTypes.string,
  closeClassName: PropTypes.string,
  closeAriaLabel: PropTypes.string,
  cssModule: PropTypes.object,
  color: PropTypes.string,
  fade: PropTypes.bool,
  isOpen: PropTypes.bool,
  toggle: PropTypes.func,
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  transition: PropTypes.shape(Fade.propTypes),
  innerRef: PropTypes.oneOfType([
    PropTypes.object,
    PropTypes.string,
    PropTypes.func,
  ]),
};

const defaultProps = {
  color: 'success',
  isOpen: true,
  tag: 'div',
  closeAriaLabel: 'Close',
  fade: true,
  transition: {
    ...Fade.defaultProps,
    unmountOnExit: true,
  },
};

class UncontrolledAlert extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: true };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    return <Alert {...this.props} isOpen={this.state.isOpen} toggle={this.toggle}/>;
  }
}

UncontrolledAlert.propTypes = propTypes;
UncontrolledAlert.defaultProps = defaultProps;

export default UncontrolledAlert;
