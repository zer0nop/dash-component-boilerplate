import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { Popper } from 'react-popper';
import { mapToCssModules } from '../utils/utils';
import { withDropDownContext } from '../contexts/DropDownContext';

const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  children: PropTypes.node,
  tag: PropTypes.string,
  right: PropTypes.bool,
  flip: PropTypes.bool,
  modifiers: PropTypes.object,
  className: PropTypes.string,
  cssModule: PropTypes.object,
  persist: PropTypes.bool,
};

const defaultProps = {
  tag: 'div',
  flip: true,
};

const noFlipModifier = { flip: { enabled: false } };

const directionPositionMap = {
  up: 'top',
  left: 'left',
  right: 'right',
  down: 'bottom',
};

const DropdownMenuBase = (props) => {
  const { className, cssModule, right, tag, flip, modifiers, persist, context, ...attrs } = props;
  const classes = mapToCssModules(classNames(
    className,
    'dropdown-menu',
    {
      'dropdown-menu-right': right,
      show: context.isOpen,
    }
  ), cssModule);

  let Tag = tag;

  if (persist || (context.isOpen && !context.inNavbar)) {
    Tag = Popper;

    const position1 = directionPositionMap[context.direction] || 'bottom';
    const position2 = right ? 'end' : 'start';
    attrs.placement = `${position1}-${position2}`;
    attrs.component = tag;
    attrs.modifiers = !flip ? {
      ...modifiers,
      ...noFlipModifier,
    } : modifiers;
  }

  return (
    <Tag
      {...attrs}
      tabIndex="-1"
      role="menu"
      aria-hidden={!context.isOpen}
      className={classes}
      x-placement={attrs.placement}
    />
  );
};

DropdownMenuBase.propTypes = propTypes;
DropdownMenuBase.defaultProps = defaultProps;

const DropdownMenu = withDropDownContext(DropdownMenuBase)

export default DropdownMenu;
