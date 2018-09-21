import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { mapToCssModules } from '../utils/utils';
import { withTabContext } from '../contexts/TabContext'

const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  className: PropTypes.string,
  cssModule: PropTypes.object,
  tabId: PropTypes.any,
};

const defaultProps = {
  tag: 'div',
};

function TabPaneBase(props) {
  const {
    className,
    cssModule,
    tabId,
    tag: Tag,
    context,
    ...attributes
  } = props;
  const classes = mapToCssModules(classNames('tab-pane', className, { active: tabId === context.activeTabId }), cssModule);
  return (
    <Tag {...attributes} className={classes} />
  );
}
TabPaneBase.propTypes = propTypes;
TabPaneBase.defaultProps = defaultProps;

const TabPane = withTabContext(TabPaneBase)

export default TabPane