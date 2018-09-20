import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import CardBody from './CardBody';
import { warnOnce } from '../utils';

const propTypes = {
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  className: PropTypes.string,
  cssModule: PropTypes.object,
};

const defaultProps = {
  tag: 'div'
};

function CardBlock(props) {
  warnOnce('The "CardBlock" component has been deprecated.\nPlease use component "CardBody".');
  return <CardBody {...props} />;
}

CardBlock.propTypes = propTypes;
CardBlock.defaultProps = defaultProps;

export default CardBlock