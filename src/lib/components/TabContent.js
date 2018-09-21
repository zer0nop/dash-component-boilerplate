import React, { Component } from 'react';
import { polyfill } from 'react-lifecycles-compat';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { mapToCssModules, omit } from '../utils/utils';
import { TabContext } from '../contexts/TabContext'


const propTypes = {
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  activeTab: PropTypes.any,
  className: PropTypes.string,
  cssModule: PropTypes.object,
};

const defaultProps = {
  tag: 'div',
};

class TabContent extends Component {
  static getDerivedStateFromProps(nextProps, prevState) {
    if (prevState.activeTab !== nextProps.activeTab) {
      return {
        activeTab: nextProps.activeTab
      };
    }
    return null;
  }
  constructor(props) {
    super(props);
    this.state = {
      activeTab: this.props.activeTab
    };
  }

  render() {
    const {
      className,
      cssModule,
      tag: Tag,
      children
    } = this.props;

    const attributes = omit(this.props, Object.keys(propTypes));

    const classes = mapToCssModules(classNames('tab-content', className), cssModule);

    return (
      <Tag {...attributes} className={classes}>
        <TabContext.Provider value={{ activeTabId: this.state.activeTab }}>
          {children}
        </TabContext.Provider>
      </Tag>
    );
  }
}

polyfill(TabContent);
export default TabContent;

TabContent.propTypes = propTypes;
TabContent.defaultProps = defaultProps;
