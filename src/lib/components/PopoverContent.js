import React from 'react';
import PropTypes from 'prop-types';
import PopoverBody from './PopoverBody';
import { warnOnce } from '../utils/utils';

const propTypes = {
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  className: PropTypes.string,
  cssModule: PropTypes.object,
};

const defaultProps = {
  tag: 'div'
};

function PopoverContent(props) {
  warnOnce('The "PopoverContent" component has been deprecated.\nPlease use component "PopoverBody".');
  return <PopoverBody {...props} />;
}

PopoverContent.propTypes = propTypes;
PopoverContent.defaultProps = defaultProps;

export default PopoverContent