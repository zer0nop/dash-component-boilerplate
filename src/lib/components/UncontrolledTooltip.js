import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Tooltip from './Tooltip';
import { PopperPlacements, targetPropType } from '../utils/utils';

const propTypes = {
  placement: PropTypes.oneOf(PopperPlacements),
  target: targetPropType.isRequired,
  container: targetPropType,
  isOpen: PropTypes.bool,
  disabled: PropTypes.bool,
  hideArrow: PropTypes.bool,
  boundariesElement: PropTypes.string,
  className: PropTypes.string,
  innerClassName: PropTypes.string,
  arrowClassName: PropTypes.string,
  cssModule: PropTypes.object,
  toggle: PropTypes.func,
  autohide: PropTypes.bool,
  placementPrefix: PropTypes.string,
  delay: PropTypes.oneOfType([
    PropTypes.shape({ show: PropTypes.number, hide: PropTypes.number }),
    PropTypes.number,
  ]),
  modifiers: PropTypes.object,
  offset: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]),
  innerRef: PropTypes.oneOfType([
    PropTypes.func,
    PropTypes.string,
    PropTypes.object
  ]),
  trigger: PropTypes.string,
};

const DEFAULT_DELAYS = {
  show: 0,
  hide: 250
};

const defaultProps = {
  isOpen: false,
  hideArrow: false,
  placement: 'top',
  placementPrefix: 'bs-tooltip',
  delay: DEFAULT_DELAYS,
  autohide: true,
  toggle: function () { }
};

class UncontrolledTooltip extends Component {
  constructor(props) {
    super(props);

    this.state = { isOpen: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({ isOpen: !this.state.isOpen });
  }

  render() {
    return <Tooltip {...this.props} isOpen={this.state.isOpen} toggle={this.toggle} />;
  }
}

UncontrolledTooltip.propTypes = propTypes;
UncontrolledTooltip.defaultProps = defaultProps;

export default UncontrolledTooltip;