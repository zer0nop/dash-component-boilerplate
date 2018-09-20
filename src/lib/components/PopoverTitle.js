import React from 'react';
import PropTypes from 'prop-types';
import PopoverHeader from './PopoverHeader';
import { warnOnce } from '../utils/utils';

const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  className: PropTypes.string,
  cssModule: PropTypes.object,
};

const defaultProps = {
  tag: 'h3'
};

function PopoverTitle(props) {
  warnOnce('The "PopoverTitle" component has been deprecated.\nPlease use component "PopoverHeader".');
  return <PopoverHeader {...props} />;
}

PopoverTitle.propTypes = propTypes;
PopoverTitle.defaultProps = defaultProps;

export default PopoverTitle